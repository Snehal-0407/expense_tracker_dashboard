import pandas as pd
from details_parser import parse_details, parse_clean_data
from standardize import standardize_merchant, standardize_parsed_data
from categorize_txn import categorize_transaction, categorize_standardize_data
from sql_connect import load_data_to_mysql

def read_input_file():
    file_path = "input/April.xlsx"

    df = pd.read_excel(file_path)

    print(df.head())
    print(df.columns)
    print(df.info())
    print(df.isnull().sum())
    return df

def clean_input_data(df):

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Replace blank Debit with 0
    df["Debit"] = df["Debit"].fillna(0)

    # Replace blank Credit with 0
    df["Credit"] = df["Credit"].fillna(0)
    # Delete the "Ref No/Cheque No" column
    df = df.drop(columns=["Ref No/Cheque No"])
    print(df.isnull().sum())

    df["Details"] = df["Details"].str.strip()

    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

    df.to_excel("output/cleaned_data.xlsx", index=False)

    print(df.columns)





# Start the process

input_df = read_input_file()
clean_input_data(input_df)
parse_clean_data()
standardize_parsed_data()
categorize_standardize_data()
load_data_to_mysql()