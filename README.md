# Inventory Forecast Analysis (Retail/QSR)

This project analyses store-level inventory and demand trends using real-world-style retail data. It demonstrates how Python can be used to measure forecast accuracy and support stock management decisions.

## Dataset Summary

Simulated inventory dataset with:
- Daily records across multiple stores and product categories
- Fields include: `Units Sold`, `Demand Forecast`, `Inventory Level`, `Price`, `Promotion`, `Weather`, and `Competitor Pricing`

## Project Highlights

- Cleaned and preprocessed over 73,000 rows using Pandas
- Aggregated monthly sales and forecasts for visual trend comparison
- Calculated key forecast accuracy metrics:
  - MAE (Mean Absolute Error)
  - MAPE (Mean Absolute Percentage Error)
- Created a trend chart showing Actual Sales vs Forecast vs Inventory
- Exported results as `.ipynb` and `.html` for review and sharing

## Tools Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook / VS Code
- GitHub

## Key Takeaways

- Forecasting was consistently within approximately 3.5% MAPE, indicating high accuracy
- Inventory levels remained stable with no extreme fluctuations
- This type of MIS reporting is ideal for QSR or retail operational planning

## Files in This Repository

| File                      | Description                            |
|---------------------------|----------------------------------------|
| `inventory_forecast.ipynb`| Full notebook with cleaning and visuals |
| `main.py`                 | Script-based version of the same logic |
| `inventory_forecast.html`| Rendered version of the notebook       |
| `retail_store_inventory.csv` | Dataset (simulated)                 |

## Status

- Completed
- Ready for portfolio
- Publicly visible and reusable

This project was built to showcase applied data analytics and business insight skills in inventory and supply chain contexts.
