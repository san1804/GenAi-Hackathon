import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Filter Gold members
gold_members = merged_df[merged_df['membership'] == 'Gold']
print(f"Gold member orders: {len(gold_members)}")

# Average order value
avg_order_value = gold_members['total_amount'].mean()
rounded_avg = round(avg_order_value, 2)
print(f"Average order value for Gold members: ₹{rounded_avg}")