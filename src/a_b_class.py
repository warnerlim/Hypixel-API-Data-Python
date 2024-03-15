class auction_data:
    def __init__(self,item_name,uuid,command,price):
        self.item_name = item_name
        self.uuid = uuid
        self.command = command
        self.price = price

class bazaar_data:
    def __init__(self, item_name, price, amount, orders, summary):
        self.item_name = item_name
        self.price = price
        self.amount = amount
        self.orders = orders
        self.summary = summary
        
# Bazaar class would be item_name, 