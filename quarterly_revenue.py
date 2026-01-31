import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Convert order_date to datetime
merged_df['order_date'] = pd.to_datetime(merged_df['order_date'], format='%d-%m-%Y')
print("Dates converted.")

# Extract month
merged_df['month'] = merged_df['order_date'].dt.month

# Define quarter
def get_quarter(month):
    if month <= 3:
        return 'Q1'
    elif month <= 6:
        return 'Q2'
    elif month <= 9:
        return 'Q3'
    else:
        return 'Q4'

merged_df['quarter'] = merged_df['month'].apply(get_quarter)

# Group by quarter and sum revenue
quarter_revenue = merged_df.groupby('quarter')['total_amount'].sum().reset_index()
print("Quarterly revenue:")
print(quarter_revenue)

# Find the quarter with highest revenue
max_revenue_quarter = quarter_revenue.loc[quarter_revenue['total_amount'].idxmax()]
print(f"\nQuarter with highest revenue: {max_revenue_quarter['quarter']} (₹{max_revenue_quarter['total_amount']:.2f})")