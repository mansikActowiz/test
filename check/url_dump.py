from sqlalchemy import create_engine
import mysql.connector
import time

url = 'https://store.croma.com/'
multiple_url = [url] * 1000
print(multiple_url)

# Step 1: Create MySQL Database
def create_mysql_database(database_name, user, password, host='localhost'):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"MySQL database '{database_name}' created or already exists.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Step 2: Create Table
def create_mysql_table(database_name, user, password, table_name, host='localhost'):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database_name)
        cursor = conn.cursor()
        create_table_sql = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            url_link VARCHAR(255) NOT NULL
        );
        '''
        cursor.execute(create_table_sql)
        print(f"Table '{table_name}' created in database '{database_name}'.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")



import requests


def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""





# Step 3: Insert URL data
def insert_urls(database_name, user, password, table_name, urls, host='localhost'):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database_name)
        cursor = conn.cursor()
        insert_query = f"INSERT INTO {table_name} (url_link) VALUES (%s)"

        start_time=time.time()
        cursor.executemany(insert_query, [(u,) for u in urls])
        conn.commit()
        end_time=time.time()

        total_time=end_time-start_time

        print(f" Inserted {len(urls)} URLs into '{table_name}'.")
        print(f'time taken by sync process : {total_time:.4f} seconds')
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


import asyncio
import aiomysql
import time

async def insert_urls_async(database_name, user, password, table_name, urls, host='localhost'):
    try:
        conn = await aiomysql.connect(user=user, password=password, host=host, db=database_name)
        cursor = await conn.cursor()
        insert_query = f"INSERT INTO {table_name} (url_link) VALUES (%s)"

        start_time = time.time()

        await cursor.executemany(insert_query, [(u,) for u in urls])
        await conn.commit()

        end_time = time.time()

        total_time=end_time-start_time

        print(f"Inserted {len(urls)} URLs into '{table_name}' (async).")
        print(f"time taken by Async process : {total_time:.4f} seconds")

        await cursor.close()
        conn.close()
    except Exception as e:
        print(f"Async Error: {e}")

# Run async function
asyncio.run(insert_urls_async('url_database', 'root', 'Actowiz', 'url_table', multiple_url, host='localhost'))



# Run everything
create_mysql_database('url_database', 'root', 'Actowiz', host='localhost')
create_mysql_table('url_database', 'root', 'Actowiz', 'url_table', host='localhost')
insert_urls('url_database', 'root', 'Actowiz', 'url_table', multiple_url, host='localhost')
