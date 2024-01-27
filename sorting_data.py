from get_a_b_data import *

def quicksort(arr, key_func):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if key_func(x) <= key_func(pivot)]
        greater = [x for x in arr[1:] if key_func(x) > key_func(pivot)]
        return quicksort(less, key_func) + [pivot] + quicksort(greater, key_func)

def sort_by_price(class_objects_list, key_func = lambda x: x.price):
    key_func = key_func if callable(key_func) else lambda x: x.price
    return quicksort(class_objects_list, key_func)

input_item_name = input("Enter item name for bazaar data here: ")
sorted_auction_data = sort_by_price(retrieve_auction_data())
sorted_insta_sell = sort_by_price(retrieve_bazaar_data("sell", input_item_name))
sorted_insta_buy = sort_by_price(retrieve_bazaar_data("buy", input_item_name))
page_of_items = 12
average_price = 0.0

for i in range(1, page_of_items):
    average_price += float(sorted_auction_data[i].price/(page_of_items - 1))

print(*vars(sorted_auction_data[0]).values(), sep=', ') # Cheapest Auction item
print(average_price) # Average price of auction item
print(*vars(sorted_insta_sell[0]).values(), sep=', ') # Cheapest Bazaar Item to Instant Sell
print(*vars(sorted_insta_buy[0]).values(), sep=', ') # Cheapest Bazaar Item to Instant Buy


# Calculate how many heat cores are within the range of about 20% from the cheapest heat core
# Identify the quantity as well
# Calculate average of all these heat cores