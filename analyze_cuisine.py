import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Calculate distinct restaurants per cuisine
distinct_restaurants = merged_df.groupby('cuisine')['restaurant_id'].nunique().reset_index()
distinct_restaurants.columns = ['cuisine', 'distinct_restaurants']
print("Distinct restaurants per cuisine:")
print(distinct_restaurants)

# Calculate total revenue per cuisine
revenue_per_cuisine = merged_df.groupby('cuisine')['total_amount'].sum().reset_index()
revenue_per_cuisine.columns = ['cuisine', 'total_revenue']
print("\nTotal revenue per cuisine:")
print(revenue_per_cuisine)

# Merge the two
cuisine_stats = pd.merge(distinct_restaurants, revenue_per_cuisine, on='cuisine')
print("\nCuisine stats:")
print(cuisine_stats)

# Find the minimum number of distinct restaurants
min_restaurants = cuisine_stats['distinct_restaurants'].min()
print(f"\nMinimum distinct restaurants: {min_restaurants}")

# Filter cuisines with the minimum distinct restaurants
low_count_cuisines = cuisine_stats[cuisine_stats['distinct_restaurants'] == min_restaurants]
print("Cuisines with lowest distinct restaurants:")
print(low_count_cuisines)

# Among them, find the one with the highest revenue
if len(low_count_cuisines) > 1:
    best_cuisine = low_count_cuisines.loc[low_count_cuisines['total_revenue'].idxmax()]
else:
    best_cuisine = low_count_cuisines.iloc[0]

print(f"\nCuisine with lowest distinct restaurants but highest revenue: {best_cuisine['cuisine']} (Restaurants: {best_cuisine['distinct_restaurants']}, Revenue: ₹{best_cuisine['total_revenue']:.2f})")