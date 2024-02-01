import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="fb6g90(*du(OCHv7{:AEd9",
    database="bitprices"
)

my_cursor = conn.cursor()

# Create the "Type" table for buy/sell types
my_cursor.execute("""
    CREATE TABLE Type (
        id INT PRIMARY KEY AUTO_INCREMENT,
        type_name VARCHAR(4) UNIQUE NOT NULL
    )
""")

# Insert initial buy/sell types into the "Type" table
my_cursor.execute("""
    INSERT INTO Type (type_name) VALUES ('buy'), ('sell')
""")

# Create the "ItemNames" table
my_cursor.execute("""
    CREATE TABLE ItemNames (
        id INT PRIMARY KEY AUTO_INCREMENT,
        item_name VARCHAR(255) UNIQUE NOT NULL
    )
""")

# Create the "Auction" table
my_cursor.execute("""
    CREATE TABLE Auction (
        id INT PRIMARY KEY AUTO_INCREMENT,
        item_id INT,
        uuid VARCHAR(36) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (item_id) REFERENCES ItemNames(id)
    )
""")

# Create the "Bazaar" table
my_cursor.execute("""
    CREATE TABLE Bazaar (
        id INT PRIMARY KEY AUTO_INCREMENT,
        item_id INT,
        price DECIMAL(10, 2) NOT NULL,
        amount INT NOT NULL,
        orders INT NOT NULL,
        type_id INT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (item_id) REFERENCES ItemNames(id),
        FOREIGN KEY (type_id) REFERENCES Type(id)
    )
""")
  
conn.commit()
conn.close()