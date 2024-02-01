import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="fb6g90(*du(OCHv7{:AEd9",
    database="bitprices"
)

my_cursor = conn.cursor()

table_name = 'Bazaar'

# Select all rows from the ItemNames table
my_cursor.execute(f'DELETE FROM {table_name}')

conn.commit()

# Close the connection
conn.close()