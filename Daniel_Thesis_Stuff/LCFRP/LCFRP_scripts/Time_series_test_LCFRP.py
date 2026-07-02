import pandas as pd
import matplotlib.pyplot as plt

###first steps
##CREATE A VIRTUAL ENVIRONMENT
#Cmd + Shift + P
#Python: Select Interpreter
#Create a Virtual Environment
#Venv
#Python 3.13.3
#which python (should bring back "/Users/daniel/Desktop/Thesis Stuff/COAST-Lab.github.io-1/.venv/bin/python")
##if above step does not work, try to activate virtual environment
#in terminal: pip install pandas matplotlib
from pathlib import Path

project_dir = Path(__file__).parent.parent
data_dir = project_dir / "LCFRP_data"

df = pd.read_csv(data_dir / "B9790000.csv", skiprows=10)

# Create one datetime column
df["measurement_time"] = pd.to_datetime(
    df["date"] + " " + df["time"]
)

# Keep only the columns we need
df = df[[
    "measurement_time",
    "Temperature(C)",
    "Conductivity(umhos/cm)"
]]

# Plot
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(df["measurement_time"],
         df["Temperature(C)"],
         color="red",
         label="Temperature")
ax1.set_ylabel("Temperature (°C)", color="red")

ax2 = ax1.twinx()
ax2.plot(df["measurement_time"],
         df["Conductivity(umhos/cm)"],
         color="blue",
         label="Conductivity")
ax2.set_ylabel("Conductivity (µmhos/cm)", color="blue")

# Add a faint dotted line at January 1st of each year
start_year = df["measurement_time"].dt.year.min()
end_year = df["measurement_time"].dt.year.max()

for year in range(start_year, end_year + 1):
    ax1.axvline(
        pd.Timestamp(f"{year}-01-01"),
        color="gray",
        linestyle=":",
        linewidth=0.8,
        alpha=0.5
    )

plt.title("Temperature and Conductivity Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()