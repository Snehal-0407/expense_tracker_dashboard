# STABDARDIZE MERCHANT NAMES
import pandas as pd
import re

# Load file
file_path = "output/parsed_transactions.csv"
df = pd.read_csv("output/parsed_transactions.csv")

# Function
def standardize_merchant(merchant):
    merchant = str(merchant).strip().upper()

    # Food Delivery
    if "SWIGGY" in merchant:
        return "SWIGGY"
    if "ZOMATO" in merchant:
        return "ZOMATO"

    # Shopping
    if "AMAZON" in merchant:
        return "AMAZON"

    if "FLIPKART" in merchant:
        return "FLIPKART"

    if "MEESHO" in merchant:
        return "MEESHO"

    # Recharge
    if "JIO" in merchant:
        return "JIO"

    if "AIRTEL" in merchant:
        return "AIRTEL"

    if "VI" in merchant or "VODAFONE" in merchant:
        return "VI"

    # Ride
    if "UBER" in merchant:
        return "UBER"

    return merchant
# Apply function
df["Merchant"] = df["Merchant"].apply(standardize_merchant)


