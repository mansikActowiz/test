
import pandas as pd
from sqlalchemy import create_engine


def dump_csv_to_sql(csv_path):

    df = pd.read_csv(csv_path)
    print(df)
    user = 'root'
    password = 'Actowiz'  # e.g., 'Actowiz'
    host = 'localhost'
    database = 'burger_king_store_locator'  # <-- your correct DB name

    # Create SQLAlchemy engine
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    # Create table if not exists and insert data
    df.to_sql('bk_store_locator', con=engine, if_exists='replace', index=False) #write your table name here

    print("Data inserted successfully into 'store_locator' table in 'bk' database.")

dump_csv_to_sql( r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_try.csv')

