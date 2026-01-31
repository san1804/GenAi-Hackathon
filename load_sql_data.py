import sqlite3
import pandas as pd

# Create a SQLite database file
conn = sqlite3.connect('restaurants.db')

# Read the SQL file and execute it
with open('restaurants.sql', 'r') as f:
    sql_script = f.read()

conn.executescript(sql_script)
print("Restaurants data loaded into SQLite database (restaurants.db).")

# Query the restaurants table
restaurants_df = pd.read_sql_query("SELECT * FROM restaurants", conn)
print(f"Shape: {restaurants_df.shape}")
print(restaurants_df.head())

# Close the connection
conn.close()