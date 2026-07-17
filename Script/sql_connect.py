from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd

def load_data_to_mysql():

    # MySQL Connection
    connection_url = URL.create(
        drivername="mysql+pymysql",
        username="root",
        password="Snehal@04",
        host="localhost",
        port=3306,
        database="expense_tracker"
    )

    engine = create_engine(connection_url)
    df = pd.read_excel("Output/final_transactions.xlsx")
    # Load data into MySQL
    df.to_sql(
        "transactions",
        con=engine,
        if_exists="replace",
        index=False
    )
    print("✅ Data loaded into MySQL successfully!")