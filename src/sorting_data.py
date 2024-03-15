from get_a_b_data import *

# Prices are already sorted lmao, no quicksort required
sorted_auction_data = (retrieve_auction_data())

print(*vars(sorted_auction_data[0]).values(), sep=', ') # Cheapest Auction item
print(retrieve_bazaar_data("sell"))
print(retrieve_bazaar_data("buy"))


# Average price of first 12 items in auction, use for future when doing cost analysis
# page_of_items = 12
# average_price = 0.0

# for i in range(1, page_of_items):
#     average_price += float(sorted_auction_data[i].price/(page_of_items - 1))
# print(average_price) # Average price of auction item

# Calculate how many heat cores are within the range of about 20% from the cheapest heat core
# Identify the quantity as well
# Calculate average of all these heat cores