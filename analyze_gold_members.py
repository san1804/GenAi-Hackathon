import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Filter for Gold members
gold_members = merged_df[merged_df['membership'] == 'Gold']
print(f"Gold members data: {gold_members.shape[0]} orders")

# Group by city and calculate average order value
city_avg = gold_members.groupby('city')['total_amount'].mean().reset_index()
print("Average order values by city for Gold members:")
print(city_avg)

# Find the city with the highest average
max_avg_city = city_avg.loc[city_avg['total_amount'].idxmax()]
print(f"\nCity with the highest average order value among Gold members: {max_avg_city['city']} (₹{max_avg_city['total_amount']:.2f})")