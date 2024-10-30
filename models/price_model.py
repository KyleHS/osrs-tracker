import pandas as pd

def find_top_crashes(latest_prices):
    # Convert latest prices dictionary to a DataFrame
    df = pd.DataFrame.from_dict(latest_prices, orient="index")
    df["price_drop"] = (df["high"] - df["low"]) / df["high"]

    # Sort by the largest drop and get the top 3
    top_crashes = df.nlargest(3, "price_drop").reset_index()
    top_crashes.columns = ["ItemID", "HighPrice", "HighTime", "LowPrice", "LowTime", "PriceDrop"]
    return top_crashes
