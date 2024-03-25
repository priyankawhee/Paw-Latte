import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="admin",
    password="pri123!!",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Execute SQL queries
cur.execute("SELECT * FROM your_table")
rows = cur.fetchall()

# Process the results
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
