import pandas as pd
import sqlite3

# Load transactional order data from CSV
orders_df = pd.read_csv('orders.csv')
print("Orders data loaded.")

# Load user master data from JSON
users_df = pd.read_json('users.json')
print("Users data loaded.")

# Load restaurants data from SQLite database
conn = sqlite3.connect('restaurants.db')
restaurants_df = pd.read_sql_query("SELECT * FROM restaurants", conn)
conn.close()
print("Restaurants data loaded.")

# Perform left joins
# First, join orders with users on user_id
merged_df = pd.merge(orders_df, users_df, on='user_id', how='left')

# Then, join the result with restaurants on restaurant_id
merged_df = pd.merge(merged_df, restaurants_df, on='restaurant_id', how='left')

print("Data merged successfully using left joins.")
print(f"Merged DataFrame shape: {merged_df.shape}")
print(merged_df.head())

# Optionally, save to CSV
merged_df.to_csv('merged_data.csv', index=False)
print("Merged data saved to merged_data.csv")