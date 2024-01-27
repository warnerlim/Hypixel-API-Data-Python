import requests
import json
from check_auction_item import *
from check_bazaar_item import *
from a_b_class import *

url_base_auction = f"https://api.hypixel.net/skyblock/auctions"
url_base_bazaar = f"https://api.hypixel.net/skyblock/bazaar?page=0"
auction_final = []

def fetch_page(url):
    response = requests.get(url)
    return response.text

def retrieve_auction_data():
    all_pages = requests.get(url_base_auction)
    data = json.loads(all_pages.content)
    
    total_pages = data['totalPages']
    print(f"Total Pages found: {total_pages}")
    
    if(data["success"]):
        
        # Get items from all pages from 0 to total_pages-1
        for current_page in range(total_pages):
            current_page_url = f"{url_base_auction}?page={current_page}"
            page_content = fetch_page(current_page_url)
            page_data = json.loads(page_content)
            
            for auction_item in page_data["auctions"]:
                try:
                    item_ans = check_auction_item(auction_item)
                    
                    # Passed filter
                    if item_ans[0]:
                        auction_final.append(item_ans[1])
                        
                    # Failed filter
                    else:
                        pass
                    
                except Exception as e:
                    print(f"An error occurred: {e}")
                    
    # Unsuccessful GET request
    else:
        print(f"Failed GET request: {data['cause']}")
        
    class_data = [auction_data(*x) for x in auction_final]
    
    return class_data

def retrieve_bazaar_data(summary_type, input_item):
    data_retrieve = requests.get(url_base_bazaar)
    data = data_retrieve.json().get("products", {})
    success, item_instances = bazaar_items(data, input_item, summary_type)
    if success:
        return item_instances
    else:
        return []