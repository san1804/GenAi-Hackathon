import pandas as pd
import json

# Load transactional order data from CSV
orders_df = pd.read_csv('orders.csv')
print("Orders data loaded successfully.")
print(f"Shape: {orders_df.shape}")
print(orders_df.head())

# Load user master data from JSON
with open('users.json', 'r') as f:
    users_data = json.load(f)

users_df = pd.DataFrame(users_data)
print("\nUsers data loaded successfully.")
print(f"Shape: {users_df.shape}")
print(users_df.head())

# Optional: Load restaurants data from SQL
import sqlite3

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Read the SQL file and execute it
with open('restaurants.sql', 'r') as f:
    sql_script = f.read()

conn.executescript(sql_script)
print("\nRestaurants data loaded into SQLite database.")

# Query the restaurants table
restaurants_df = pd.read_sql_query("SELECT * FROM restaurants", conn)
print(f"Shape: {restaurants_df.shape}")
print(restaurants_df.head())

# Close the connection
conn.close()