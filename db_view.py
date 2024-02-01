import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="fb6g90(*du(OCHv7{:AEd9",
    database="bitprices"
)

my_cursor = conn.cursor()

# Select all rows from the ItemNames table
my_cursor.execute("SELECT * FROM ItemNames")

# Fetch all rows
result = my_cursor.fetchall()

# Print the result
for row in result:
    print(row)

# Close the connection
conn.close()