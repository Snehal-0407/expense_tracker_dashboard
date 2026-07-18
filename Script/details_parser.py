#Detilas parser

import pandas as pd
import re

def read_clean_data():
    file_path = "output/cleaned_data.xlsx"
    df = pd.read_excel(file_path)
    return df


def parse_details(details):
    details = str(details).strip()

    txn_type = ""
    mode = ""
    merchant = ""

    # Transaction Type
    if "/DR/" in details:
        txn_type = "Debit"
    elif "/CR/" in details:
        txn_type = "Credit"

    # Payment Mode
    modes = ["UPI", "ATM", "IMPS", "NEFT", "RTGS", "POS", "CHEQUE", "CASH"]

    for m in modes:
        if m in details.upper():
            mode = m
            break

    # Merchant
    match = re.search(r"/\d+/([A-Za-z0-9 .&_-]+?)/", details)

    if match:
        merchant = match.group(1).strip().upper()

    return pd.Series([txn_type, mode, merchant])

def parse_clean_data():
    df = read_clean_data()

    df["TXN_Type"] = ""
    df["Mode"] = ""
    df["Merchant"] = ""


    df[["TXN_Type", "Mode", "Merchant"]] = df["Details"].apply(parse_details)

    # Fill Merchant for ATM withdrawals
    df.loc[
    df["Details"].str.contains("ATM WDL|ATM CASH|POS ATM|YONO CASH|YONO WDL|YONO CASH ATM", case=False, na=False),
    "Merchant"
    ] = "CASH WITHDRAWAL"

    # Save parsed file (optional)
    df.to_excel("output/parsed_transactions.xlsx", index=False)