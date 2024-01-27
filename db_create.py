import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="fb6g90(*du(OCHv7{:AEd9",
    database="bitprices"
)

my_cursor = conn.cursor()

# Create the "auction" table
my_cursor.execute("""
    CREATE TABLE auction (
        id INT PRIMARY KEY AUTO_INCREMENT,
        item_name VARCHAR(255) NOT NULL,
        item_id INT NOT NULL,
        uuid VARCHAR(36) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")

# Create the "bazaar" table
my_cursor.execute("""
    CREATE TABLE bazaar (
        id INT PRIMARY KEY AUTO_INCREMENT,
        item_name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        amount INT NOT NULL,
        orders INT NOT NULL,
        type VARCHAR(4) NOT NULL CHECK (type IN ('buy', 'sell')),
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
  
conn.commit()
conn.close()