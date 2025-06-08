import pandas as pd
import os
import re

# Path to your main project folder
base_dir = "/Users/tiffanykuo/Desktop/AAE 718/Project03"

# Mapping of station codes to readable station names
station_map = {
    "C1A9N0": "Xindian",
    "C1AC50": "Taipei",
    "C1C510": "Taoyuan",
    "C1D400": "Hsinchu"
}

# Container for all processed data
all_data = []

# Iterate through each station folder
for station_code, station_name in station_map.items():
    station_folder = os.path.join(base_dir, station_code)
    if not os.path.isdir(station_folder):
        print(f"Directory not found: {station_folder}")
        continue

    for file in os.listdir(station_folder):
        match = re.match(rf"{station_code}-(\d{{4}})\.csv", file)
        if match:
            year = int(match.group(1))
            file_path = os.path.join(station_folder, file)
            try:
                df = pd.read_csv(file_path, encoding="utf-8")
                df = df.iloc[1:]  # Skip the second-row Chinese headers
                df.columns = [
                    "Month",
                    "MonthlyRainfall_mm",
                    "RainyDays",
                    "MaxDailyRainfall_mm",
                    "MaxDailyRainfallDateTime"
                ]
                df["Month"] = df["Month"].astype(int)
                df["MonthlyRainfall_mm"] = pd.to_numeric(df["MonthlyRainfall_mm"], errors="coerce")
                df["RainyDays"] = pd.to_numeric(df["RainyDays"], errors="coerce")
                df["MaxDailyRainfall_mm"] = pd.to_numeric(df["MaxDailyRainfall_mm"], errors="coerce")
                df["Year"] = year
                df["Station"] = station_name
                df["StationCode"] = station_code
                all_data.append(df)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

# Combine all dataframes and export
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    output_file = os.path.join(base_dir, "north_taiwan_rainfall_cleaned.csv")
    combined_df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to: {output_file}")
else:
    print("No data was successfully processed.")
