import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Filter for Hyderabad
hyderabad_orders = merged_df[merged_df['city'] == 'Hyderabad']
print(f"Orders in Hyderabad: {len(hyderabad_orders)}")

# Sum total_amount
total_revenue = hyderabad_orders['total_amount'].sum()
rounded_revenue = round(total_revenue)
print(f"Total revenue from Hyderabad: ₹{rounded_revenue}")