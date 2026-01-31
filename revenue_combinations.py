import pandas as pd

# Load the merged data
merged_df = pd.read_csv('merged_data.csv')
print("Merged data loaded.")

# Define the combinations
combinations = [
    ("Gold", "Indian"),
    ("Gold", "Italian"),
    ("Regular", "Indian"),
    ("Regular", "Chinese")
]

results = []

for membership, cuisine in combinations:
    filtered = merged_df[(merged_df['membership'] == membership) & (merged_df['cuisine'] == cuisine)]
    revenue = filtered['total_amount'].sum()
    results.append((membership, cuisine, revenue))
    print(f"{membership} + {cuisine}: ₹{revenue:.2f}")

# Find the one with highest revenue
best = max(results, key=lambda x: x[2])
print(f"\nHighest revenue combination: {best[0]} + {best[1]} (₹{best[2]:.2f})")