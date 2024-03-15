from mysql_db import *

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