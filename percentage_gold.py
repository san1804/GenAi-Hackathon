import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Total orders
total_orders = len(merged_df)
print(f"Total orders: {total_orders}")

# Orders by Gold members
gold_orders = len(merged_df[merged_df['membership'] == 'Gold'])
print(f"Orders by Gold members: {gold_orders}")

# Percentage
percentage = (gold_orders / total_orders) * 100
rounded_percentage = round(percentage)
print(f"Percentage of total orders by Gold members: {rounded_percentage}%")