import pandas as pd
import re


#CATEGORIZE TRANSACTIONS

def categorize_transaction(merchant, debit , TXN_Type):
    merchant = str(merchant).upper().strip()

    # Credit Transactions
    if TXN_Type == "Credit":
        return "Income"
    
    #Cash Withdrawal
    if TXN_Type == "ATM":
        return "Cash Withdrawal"

    # Food
    elif merchant in ["SWIGGY", "ZOMATO"]:
        return "Food"

    # Shopping
    elif merchant in ["AMAZON", "FLIPKART", "MEESHO"]:
        return "Shopping"

    # Bills Payment
    elif merchant in ["JIO", "AIRTEL", "RECHARGE", "BILL PAYMENT" , "ELECTRICITY BILL"]:
        return "Bills Payment"

    # Transport
    elif merchant in ["UBER", "OLA"]:
        return "Transport"

    # Fuel
    elif merchant in ["PETROL PUMP", "FUEL STATION", "HPCL", "IOC", "BPCL", "Fuel", "PETROL", "INDIAN", "INDIAN OIL"]:
        return "Fuel"
    
    #Groceries
    elif merchant in ["GROCERY STORE", "SUPERMARKET", "BIG BAZAAR", "DMART", "SPAR", "GROCERY", "BLINKIT",]:
        return "Groceries"
    
    
    #Tea and Coffee
    elif debit >0 and debit <= 30:
        return "Tea/Coffee"
    
    #Daily EXP
    elif debit >30 and debit <= 100:
        return "Daily Exp"
    
    #Default
    else:
        return "Others"

def categorize_standardize_data():
    # Load file
    file_path = "output/parsed_transactions.csv"
    df = pd.read_csv("output/parsed_transactions.csv")

    df["Month"] = pd.to_datetime(df["Date"]).dt.month_name()
    df["Year"] = pd.to_datetime(df["Date"]).dt.year
    df["Day"] = pd.to_datetime(df["Date"]).dt.day
    df["Weekday"] = pd.to_datetime(df["Date"]).dt.day_name()

    print(df.head(10))
    print(df.columns)
    print(df.isnull().sum())
    print(df.columns.tolist())

    # Create Category column
    df["Category"] = df.apply(
        lambda row: categorize_transaction(
            row["Merchant"],
            row["Debit"],
            row["TXN_Type"]
        ),
        axis=1
    )
    print(df["Category"].value_counts())

    df.to_excel("output/final_transactions.xlsx", index=False)
    print("Final transactions saved to output/final_transactions.xlsx")
   
    print("ok categorize")