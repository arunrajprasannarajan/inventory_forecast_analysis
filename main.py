# %% Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# %% Load the dataset
df = pd.read_csv("retail_store_inventory.csv")

# %% Basic inspection
print("Shape of the dataset:", df.shape)
print("\nColumn names:\n", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())

# %% Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# %% Check for duplicate rows
duplicate_rows = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicate_rows}")

# %% Preview unique values in categorical fields
print("\nUnique values in 'Weather Condition':", df['Weather Condition'].unique())
print("Unique values in 'Seasonality':", df['Seasonality'].unique())

# %% Show only columns with missing values
missing = df.isnull().sum()
missing = missing[missing > 0]
print("\nColumns with missing values:")
print(missing)

# %% Count rows with any missing values
rows_with_na = df.isnull().any(axis=1).sum()
print(f"\nRows with at least one missing value: {rows_with_na}")

# %% Drop rows with any missing values
df_cleaned = df.dropna()
print("\nNew dataset shape after dropping missing rows:", df_cleaned.shape)

# %% Convert 'Date' column to datetime format
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], format='%Y-%m-%d', errors='coerce')
print("\nDate column type after conversion:", df_cleaned['Date'].dtype)
print("Date range:", df_cleaned['Date'].min(), "to", df_cleaned['Date'].max())

# %% Extract month from the date
df_cleaned['Month'] = df_cleaned['Date'].dt.to_period('M')

# %% Group by Month and include row count to detect incomplete months
monthly_summary = df_cleaned.groupby('Month').agg({
    'Units Sold': 'sum',
    'Demand Forecast': 'sum',
    'Inventory Level': 'mean',
    'Date': 'count'
}).rename(columns={'Date': 'Row Count'}).reset_index()

# %% Filter out months with low data or zero values
monthly_summary = monthly_summary[(monthly_summary['Row Count'] > 100) &
                                  (monthly_summary['Units Sold'] > 0) &
                                  (monthly_summary['Demand Forecast'] > 0)]

monthly_summary['Month'] = monthly_summary['Month'].astype(str)

# %% Calculate Forecast Accuracy (MAE and MAPE)
# Calculate MAE
monthly_summary['MAE'] = abs(monthly_summary['Units Sold'] - monthly_summary['Demand Forecast'])

# Calculate MAPE (avoid divide by zero)
monthly_summary['MAPE'] = (monthly_summary['MAE'] / monthly_summary['Units Sold']) * 100

# Print summary metrics
print("\nForecast Accuracy:")
print(monthly_summary[['Month', 'MAE', 'MAPE']])

# %% Plot the results
plt.figure(figsize=(12, 6))
plt.plot(monthly_summary['Month'], monthly_summary['Units Sold'], marker='o', label='Actual Sales')
plt.plot(monthly_summary['Month'], monthly_summary['Demand Forecast'], marker='o', label='Forecast')
plt.plot(monthly_summary['Month'], monthly_summary['Inventory Level'], marker='o', label='Avg Inventory Level')
plt.title('Monthly Sales vs Forecast vs Inventory Level')
plt.xlabel('Month')
plt.ylabel('Units')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
