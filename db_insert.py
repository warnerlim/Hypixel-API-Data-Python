import mysql.connector
from get_a_b_data import *

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="fb6g90(*du(OCHv7{:AEd9",
    database="bitprices"
)
my_cursor = conn.cursor()

def get_item_id(item_name):
    # Check if the item_name exists in ItemNames
    my_cursor.execute('SELECT id FROM ItemNames WHERE item_name = %s', (item_name,))
    result = my_cursor.fetchone()

    if result:
        # If the item_name exists, return its id
        return result[0]
    
def insert_data_into_db(item_name, data):
    item_id = get_item_id(item_name)

    if data:
            entry = data[0]  # Access the first element
            if entry.summary == "buy":
                summary_id = 1
            elif entry.summary == "sell":
                summary_id = 2
                
            my_cursor.execute('''
                INSERT INTO Bazaar (item_id, price, amount, orders, type_id)
                VALUES (%s, %s, %s, %s, %s)
            ''', (item_id, entry.price, entry.amount, entry.orders, summary_id))

    conn.commit()
    
bazaar_buy = retrieve_bazaar_data("buy")
bazaar_sell = retrieve_bazaar_data("sell")

for input_item, (success, data) in bazaar_buy.items():
    if success:
        insert_data_into_db(input_item, data)  # 1 represents "buy"

for input_item, (success, data) in bazaar_sell.items():
    if success:
        insert_data_into_db(input_item, data)  # 2 represents "sell"

conn.close()