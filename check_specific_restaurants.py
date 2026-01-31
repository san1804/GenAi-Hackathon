import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# List of restaurant names to check
restaurants_to_check = [
    "Grand Cafe Punjabi",
    "Grand Restaurant South Indian",
    "Ruchi Mess Multicuisine",
    "Ruchi Foods Chinese"
]

for name in restaurants_to_check:
    # Filter for the restaurant
    rest_data = merged_df[merged_df['restaurant_name_x'] == name]
    if not rest_data.empty:
        order_count = len(rest_data)
        avg_value = rest_data['total_amount'].mean()
        print(f"{name}: Orders = {order_count}, Avg = ₹{avg_value:.2f}")
        if order_count < 20:
            print(f"  -> Qualifies (avg: {avg_value:.2f})")
        else:
            print("  -> Does not qualify (<20 orders)")
    else:
        print(f"{name}: Not found")

print("\nFrom previous analysis, the top is Restaurant_294 with 13 orders and avg ₹1040.22")