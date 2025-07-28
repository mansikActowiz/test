import pandas as pd
from sqlalchemy import create_engine


csv_path= r"C:\Users\Madri.Gadani\Desktop\madri\database_programs\personal_data1.csv"
def dump_csv_to_sql(csv_path):

    df = pd.read_csv(csv_path)
    print(df)
    user = 'root'
    password = 'Actowiz'  # e.g., 'Actowiz'
    host = 'localhost'
    database = 'persona_data'  # <-- your correct DB name

    # Create SQLAlchemy engine
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    # Create table if not exists and insert data
    df.to_sql('personal_data_table', con=engine, if_exists='replace', index=False) #write your table name here

    print("Data inserted successfully into 'store_locator' table in 'bk' database.")

dump_csv_to_sql(csv_path)