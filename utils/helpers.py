import requests

def get_latest_prices():
    url = "https://prices.runescape.wiki/api/v1/osrs/latest"
    response = requests.get(url)
    response.raise_for_status()  # Ensures it raises an error if the request fails
    data = response.json()
    return data["data"]  # Returns latest prices mapped by item ID

def get_item_mappings():
    url = "https://prices.runescape.wiki/api/v1/osrs/mapping"
    response = requests.get(url)
    response.raise_for_status()  # Ensures it raises an error if the request fails
    data = response.json()
    return {item["id"]: item for item in data}  # Maps item IDs to item details

def format_crash_output(top_crashes, item_mappings):
    formatted = []
    print("Top Crashes DataFrame:")
    print(top_crashes)
    print("Item Mappings:")
    print(item_mappings.keys())  # Print available item IDs for debugging

    for _, row in top_crashes.iterrows():
        item_id = row["ItemID"]
        # Check if the item ID exists in item_mappings
        if item_id in item_mappings:
            item_name = item_mappings[item_id]["name"]
            formatted.append(f"Item: {item_name}, Price Drop: {row['PriceDrop']:.2%}")
        else:
            print(f"Warning: Item ID {item_id} not found in item mappings.")  # Warning if the ID is missing

    return "\n".join(formatted)
