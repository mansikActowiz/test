import pandas as pd
from sqlalchemy import create_engine


'''  it dump csv file into mysql database.you have to create database only in sqlyog.
     you don't need to create table there as this code creates tables itself'''
def dump_csv_to_database(csv_path, database_table_name, database_name):
    # df = pd.read_csv(csv_path)
    # df = pd.read_csv(csv_path, encoding='ISO-8859-1')
    df = pd.read_csv(csv_path, encoding='ISO-8859-1', keep_default_na=False, na_values=[""])

    user = "root"
    password = "Actowiz"
    host = "localhost"

    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database_name}')

    try:
        connection = engine.connect()
        print("✅ Connection successful.")

        df.to_sql(name=database_table_name, con=engine, if_exists='replace', index=False)
        print(f"✅ Data inserted successfully into '{database_table_name}' table in '{database_name}' database.")

        connection.close()
        return csv_path, database_table_name, database_name

    except Exception as e:
        print(f"❌ Error: {e}")
        return None

csv_path = r'C:\Users\Madri.Gadani\Desktop\madri\OCM\OEM_final_csv_24.csv'
# csv_path = r'C:\Users\Madri.Gadani\Desktop\madri\OCM\OEM_FSL_FINAL_QA_07.csv'

database_name = 'oem_fls'
database_table_name = 'fls_16'

dump_csv_to_database(csv_path, database_table_name, database_name)





