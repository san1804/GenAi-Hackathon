import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Group by restaurant_id and calculate count and average order value
restaurant_stats = merged_df.groupby('restaurant_id').agg(
    order_count=('order_id', 'count'),
    avg_order_value=('total_amount', 'mean'),
    restaurant_name=('restaurant_name_y', 'first')  # Assuming restaurant_name_y is the master name
).reset_index()

print("Restaurant stats calculated.")
print(restaurant_stats.head())

# Filter restaurants with less than 20 total orders
filtered_restaurants = restaurant_stats[restaurant_stats['order_count'] < 20]
print(f"Restaurants with less than 20 orders: {len(filtered_restaurants)}")

# Find the one with the highest average order value
if not filtered_restaurants.empty:
    top_restaurant = filtered_restaurants.loc[filtered_restaurants['avg_order_value'].idxmax()]
    print(f"\nRestaurant with highest average order value (<20 orders): {top_restaurant['restaurant_name']} (ID: {top_restaurant['restaurant_id']}, Avg: ₹{top_restaurant['avg_order_value']:.2f}, Orders: {top_restaurant['order_count']})")
else:
    print("No restaurants with less than 20 orders found.")