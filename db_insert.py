import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="fb6g90(*du(OCHv7{:AEd9",
    database="bitprices"
)

my_cursor = conn.cursor()

new_items = ["Coal","E-Coal","E-Coal Block","Iron","E-Iron","Booster Cookie","Heat Core","Crystal Fragment","Catalyst","Hyper Catalyst","E-Lava Bucket","Magma Bucket","Plasma Bucket"]

query = "INSERT INTO ItemNames (item_name) VALUES (%s)"
data = [(item,) for item in new_items]

my_cursor.executemany(query, data)
conn.commit()
conn.close()