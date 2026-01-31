import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Count distinct users
distinct_users = merged_df['user_id'].nunique()
print(f"Number of distinct users who placed at least one order: {distinct_users}")