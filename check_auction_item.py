
auc_requirements = {"Heat_Core": {"item_name": "Heat Core", "tier": "SPECIAL", "category": "misc", "price": 999999999}}

def check_auction_item(auction_item):
    
    # Check if item is BIN
    if("bin" not in auction_item):
        return (False, "Not BIN")

    # Check if item is already claimed
    if(auction_item["claimed"] == True):
        return (False, "Already claimed")

    # For unique obj ruleset
    for id in auc_requirements:

        # Start as valid item
        valid = True

        # For every rule in obj ruleset
        for req in auc_requirements[id]:

            # Make sure rule isn't price
            if(req != "price"):

                # Make sure it follows the rule
                if(auc_requirements[id][req] not in auction_item[req]):

                    # No longer valid
                    valid = False
                    break

        # Found a potential match with a filter!
        if(valid):
            
            # Found a match with a filter AND price! (Success)
            if(auction_item["starting_bid"] < auc_requirements[id]["price"]):
                dashed_uuid = auction_item['uuid'][:8] + '-' + auction_item['uuid'][8:12] + '-' + auction_item['uuid'][12:16]
                dashed_uuid += '-' + auction_item['uuid'][16:20] + '-' + auction_item['uuid'][20:]
                return (True, (auction_item["item_name"], dashed_uuid, f"/viewauction {dashed_uuid}", auction_item['starting_bid']))
   
    # Broke on one of the requirements
    return (False, "Not all requirements met")