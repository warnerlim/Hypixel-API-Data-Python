from mysql_db import conn

my_cursor = conn.cursor()

table_name = 'Bazaar'

# Select all rows from the ItemNames table
my_cursor.execute(f'DELETE FROM {table_name}')

conn.commit()

# Close the connection
conn.close()