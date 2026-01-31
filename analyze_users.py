import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Group by user_id and sum the total_amount
user_totals = merged_df.groupby('user_id')['total_amount'].sum().reset_index()
print("User totals calculated.")

# Filter users where total_amount > 1000
high_value_users = user_totals[user_totals['total_amount'] > 1000]
print("Filtered users with total orders > ₹1000.")

# Count distinct users
distinct_count = high_value_users['user_id'].nunique()
print(f"Number of distinct users who placed orders worth more than ₹1000 in total: {distinct_count}")

# Optional: Show some details
print(high_value_users.head())