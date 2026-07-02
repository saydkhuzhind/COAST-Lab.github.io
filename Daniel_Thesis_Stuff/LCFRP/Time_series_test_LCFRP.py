import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV
df = pd.read_csv("B9490000.csv", header=8)

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