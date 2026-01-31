import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Filter Gold members
gold_members = merged_df[merged_df['membership'] == 'Gold']

# Group by city and sum revenue
city_revenue_gold = gold_members.groupby('city')['total_amount'].sum().reset_index()
print("Revenue by city for Gold members:")
print(city_revenue_gold)

# Find the city with highest revenue
top_city = city_revenue_gold.loc[city_revenue_gold['total_amount'].idxmax()]
print(f"Top revenue city for Gold members: {top_city['city']} (₹{top_city['total_amount']:.2f})")

# Count orders in that city
orders_in_top_city = len(gold_members[gold_members['city'] == top_city['city']])
print(f"Number of orders in {top_city['city']}: {orders_in_top_city}")