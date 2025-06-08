# Taiwan Climate Rainfall Project

##  Project Description

This project analyzes **ten years of rainfall data (2013–2023)** from **four weather stations in northern Taiwan**: Xindian, Taipei, Taoyuan, and Hsinchu. The objective is to examine **whether rainfall in northern Taiwan has increased over the past decade**, by evaluating:

- Annual total rainfall
- Number of rainy days per year
- Maximum daily rainfall per year
- Rainfall distribution across locations

This project fulfills the final portfolio requirement for the climate data analysis module.

---

## Data

- **Source**: Taiwan Central Weather Bureau (CWB)
- **Format**: Monthly summary data from four stations
- **Variables Used**:
  - Monthly rainfall (mm)
  - Rainy days per month
  - Max daily rainfall per month
  - Timestamp of max daily rainfall

> The cleaned CSV file is named: `north_taiwan_rainfall_cleaned.csv`

---

##  Folder Structure
```bash
Project03/
├── C1A9N0/                       # Raw station data: Xindian
├── C1AC50/                       # Raw station data: Taipei
├── C1C510/                       # Raw station data: Taoyuan
├── C1D400/                       # Raw station data: Hsinchu
├── image/                        # Final graphs (PNG format)
├── north_taiwan_rainfall_cleaned.csv
├── clean_rainfall_data.py
├── plot.py
├── report.md
└── README.md
```

---

##  How to Run

1. Install required Python packages:
```bash
pip install pandas matplotlib seaborn
```

2. Run data cleaning:
```bash
python clean_rainfall_data.py
```

3. Generate visualizations:
```bash
python plot.py
```

## Visualizations
All graphs can be found in the `image/` folder:

- annual_rainy_days_trend.png

- annual_total_rainfall_trend.png

- max_daily_rainfall_distribution.png

- total_rainfall_by_location_bar.png

## Report

See `report.md` for detailed analysis, findings, and interpretation of graphs.

## Author

Name: Caroline Kuo

GitHub: https://github.com/Tiff0416


