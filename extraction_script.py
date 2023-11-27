import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect('customer_data.db')
# Extract data
query = "SELECT * FROM customers"
data = pd.read_sql(query, conn)
# Save data to CSV
data.to_csv('customer_data.csv', index=False)
# Close the database connection
conn.close()

print("hello")

print("shrikant")

