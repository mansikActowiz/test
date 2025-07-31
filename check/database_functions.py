import pandas as pd
from sqlalchemy import create_engine

import mysql.connector

def create_mysql_database(database_name):
    try:
        # Connect to MySQL server (without specifying a database name)
        conn = mysql.connector.connect(user='root', password='Actowiz', host='localhost')
        cursor = conn.cursor()

        # Create database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"MySQL database '{database_name}' created or already exists.")

        # Cleanup
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

create_mysql_database('database_check')


def create_mysql_table(database_name,table_name):
    try:
        # Connect to the specific database
        conn = mysql.connector.connect(user='root', password='Actowiz', host='localhost', database=database_name)
        cursor = conn.cursor()

        # query  for table creation
        create_table_sql = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
        
            id INT AUTO_INCREMENT PRIMARY KEY,            
            person_name VARCHAR(500),
            email VARCHAR(500),
            phone VARCHAR(30),         
            dob DATE,
            city VARCHAR(1000),
            state VARCHAR(1000),
            country VARCHAR(1000),
            zip VARCHAR(20),          
            company VARCHAR(1000),
            job VARCHAR(500),
            salary FLOAT,
            join_date DATE,
            last_login DATETIME,
            is_active BOOLEAN           
            );
            '''
        cursor.execute(create_table_sql)
        print(f"Table '{table_name}' created in database '{database_name}'.")

        # Cleanup
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

create_mysql_table('database_check','database_check_table')


csv_path= r"C:\Users\Madri.Gadani\Desktop\madri\database_programs\personal_data1.csv"

def dump_csv_to_sql(csv_output_path,database_name,database_table_name):

    df = pd.read_csv(csv_output_path)
    print(df)
    user = 'root'
    password = 'Actowiz'  # e.g., 'Actowiz'
    host = 'localhost'
    database = database_name  #'swiggy' your correct DB name

    # Create SQLAlchemy engine
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    # Create table if not exists and insert data
    df.to_sql(database_table_name, con=engine, if_exists='replace', index=False) #swiggy_table

    print(f"Data inserted successfully into table  {database_table_name} in {database_name} database.")

dump_csv_to_sql(csv_path,'swiggy','swiggy_table')







