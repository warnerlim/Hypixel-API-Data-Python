class auction_data:
    def __init__(self,item_name,item_id,uuid,command,price):
        self.item_name = item_name
        self.item_id = item_id
        self.uuid = uuid
        self.command = command
        self.price = price

class bazaar_data:
    def __init__(self, item_name, price, amount, orders):
        self.item_name = item_name
        self.price = price
        self.amount = amount
        self.orders = orders
        
# Bazaar class would be item_name, 