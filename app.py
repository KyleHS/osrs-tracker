from models.price_model import find_top_crashes
from utils.helpers import format_crash_output, get_latest_prices, get_item_mappings

if __name__ == "__main__":
    latest_prices = get_latest_prices()
    item_mappings = get_item_mappings()
    
    top_crashes = find_top_crashes(latest_prices)
    output = format_crash_output(top_crashes, item_mappings)
    
    print("Top 3 Price Crashes:")
    print(output)
