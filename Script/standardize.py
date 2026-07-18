# STABDARDIZE MERCHANT NAMES
import pandas as pd
import re


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

    # Ride
    if "UBER" in merchant:
        return "UBER"
    if "OLA" in merchant:
        return "OLA"
    
    # Cash Withdrawal
    if merchant == "CASH WITHDRAWAL":
     return "CASH WITHDRAWAL"
    
    # Fuel
    if (
        "PETROL" in merchant
        or "FUEL" in merchant
        or "DIESEL" in merchant
        or "INDIAN" in merchant
        or "HPCL" in merchant
        or "IOC" in merchant
        or "BPCL" in merchant
    ):
        return "FUEL"

    return merchant

def standardize_parsed_data():
    # Load file
    file_path = "output/parsed_transactions.xlsx"
    df = pd.read_excel(file_path)
    # Apply function
    df["Merchant"] = df["Merchant"].apply(standardize_merchant)
    df.to_excel("output/parsed_transactions.xlsx", index=False)