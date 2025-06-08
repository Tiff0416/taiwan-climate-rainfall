import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("north_taiwan_rainfall_cleaned.csv")

# Replace station codes with full names
station_name_map = {
    "C1A9N0": "Xindian",
    "C1AC50": "Taipei",
    "C1C510": "Taoyuan",
    "C1D400": "Hsinchu"
}
df['Station'] = df['StationCode'].map(station_name_map)

# Create image directory if not exists
os.makedirs("image", exist_ok=True)

# === Plot 1: Annual Total Rainfall Trend ===
annual_rainfall = df.groupby(['Year', 'Station'])['MonthlyRainfall_mm'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=annual_rainfall, x='Year', y='MonthlyRainfall_mm', hue='Station', marker='o')
plt.title("Annual Total Rainfall Trend by Location")
plt.xlabel("Year")
plt.ylabel("Total Rainfall (mm)")
plt.legend(title="Location")
plt.tight_layout()
plt.savefig("image/annual_total_rainfall_trend.png")  # Overwrite
plt.close()

# === Plot 2: Annual Rainy Days Trend ===
annual_rainy_days = df.groupby(['Year', 'Station'])['RainyDays'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=annual_rainy_days, x='Year', y='RainyDays', hue='Station', marker='o')
plt.title("Annual Rainy Days Trend by Location")
plt.xlabel("Year")
plt.ylabel("Rainy Days")
plt.legend(title="Location")
plt.tight_layout()
plt.savefig("image/annual_rainy_days_trend.png")  # Overwrite
plt.close()

# === Plot 3: Max Daily Rainfall Distribution (Box Plot) ===
max_daily = df[['Year', 'Station', 'MaxDailyRainfall_mm']].dropna()

plt.figure(figsize=(12, 6))
sns.boxplot(data=max_daily, x='Year', y='MaxDailyRainfall_mm')
plt.title("Max Daily Rainfall Distribution per Year")
plt.xlabel("Year")
plt.ylabel("Max Daily Rainfall (mm)")
plt.tight_layout()
plt.savefig("image/max_daily_rainfall_distribution.png")  # Overwrite
plt.close()

# === Plot 4: Total Rainfall by Station Over 10 Years ===
total_rainfall_by_station = df.groupby('Station')['MonthlyRainfall_mm'].sum().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(data=total_rainfall_by_station, x='Station', y='MonthlyRainfall_mm', palette='muted')
plt.title("Total Rainfall by Location (2013–2023)")
plt.xlabel("Location")
plt.ylabel("Total Rainfall (mm)")
plt.tight_layout()
plt.savefig("image/total_rainfall_by_location_bar.png")  # Overwrite
plt.close()
