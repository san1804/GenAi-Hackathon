import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Filter for rating >= 4.5
high_rating_orders = merged_df[merged_df['rating'] >= 4.5]
order_count = len(high_rating_orders)
print(f"Number of orders for restaurants with rating ≥ 4.5: {order_count}")