from a_b_class import *
bazaar_requirements = {
    "Plasma Bucket": {"item_name": "PLASMA_BUCKET", "price_limit": 999999999},
    "Magma Bucket": {"item_name": "MAGMA_BUCKET", "price_limit": 999999999},
    "E-Coal Block": {"item_name": "ENCHANTED_COAL_BLOCK", "price_limit": 999999999},
    "E-Coal": {"item_name": "ENCHANTED_COAL", "price_limit": 999999999},
    "E-Iron": {"item_name": "ENCHANTED_IRON", "price_limit": 999999999},
    "Coal": {"item_name": "COAL", "price_limit": 999999999},
    "Iron": {"item_name": "IRON", "price_limit": 999999999},
    "Booster Cookie": {"item_name": "BOOSTER_COOKIE", "price_limit": 999999999},
    "Hyper Catalyst": {"item_name": "HYPER_CATALYST", "price_limit": 999999999},
    "Catalyst": {"item_name": "CATALYST", "price_limit": 999999999},
    "Crystal Fragments": {"item_name": "CRYSTAL_FRAGMENT", "price_limit": 999999999},
    "ANOTHER_ITEM": {"item_name": "ANOTHER_ITEM", "price_limit": 999999999}
}

def bazaar_items(bazaar_item, input_item, summary_type):
    # First Case checks input_item variable to keys in bazaar_requirements
    # Second Case then intakes the value of the item name, item_name and checks the website
    # for a potential matching item name
    # Third Case checks if there is any data on the item, 
    # Sell_summary is used for instant buying on the bazaar
    # Buy_summary is used for instant selling on the bazaar
    if input_item not in bazaar_requirements \
            or bazaar_requirements[input_item]["item_name"] not in bazaar_item \
            or f"{summary_type}_summary" not in bazaar_item[bazaar_requirements[input_item]["item_name"]]:
        return (False, f"Not all requirements are fulfilled")

    current_requirements = bazaar_requirements[input_item]
    item_data = bazaar_item[current_requirements["item_name"]]

    entries = [bazaar_data(input_item, int(entry["pricePerUnit"]), int(entry["amount"]), int(entry["orders"])) 
               for entry in item_data[f"{summary_type}_summary"]]

    return True, entries