import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mwangiemms@2006", 
    database="hospital_db"
)

# SQL query
query = "SELECT * FROM payments"

# Load into pandas
df = pd.read_sql(query, conn)

# Show data
print(df)

conn.close()