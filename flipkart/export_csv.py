import pandas as pd
import pymysql

connection=pymysql.connect(user='root',host='localhost',password='actowiz',database='flipkart_saree')
df=pd.read_sql('SELECT * from links',connection )
df.to_csv('flipkart_saree_link.csv',index=False)