#Detilas parser

import pandas as pd
file_path = "output/cleaned_data.xlsx"
df = pd.read_excel(file_path)

df["TXN_Type"] = ""
df["Mode"] = ""
df["Merchant"] = ""


import re

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


df[["TXN_Type", "Mode", "Merchant"]] = df["Details"].apply(parse_details)

df.to_csv("output/parsed_transactions.csv", index=False)