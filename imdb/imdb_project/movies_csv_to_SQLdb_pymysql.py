
#code starts
import pandas as pd
import pymysql

path=r'C:\Users\Madri.Gadani\Desktop\madri\imdb\imdb_top_250.csv'
df=pd.read_csv(path)
print(df)

conn=pymysql.connect(
    host='localhost',
    user='root',
    passwd='Actowiz',
    db='imdb_top_250_movies',
    charset='utf8',
    port=3306
)

cursor=conn.cursor()
insert_query = '''
                INSERT INTO imdb_top_movies (Title,Image_path,URL_path,Rating,Duration)
                VALUES (%s, %s, %s,%s,%s)

'''
for index, row in df.iterrows():
    print(index,row)
    cursor.execute(insert_query, (
        row['Title'],
        row['Image_path'],
        row['URL_path'],
        row['Rating'],
        row['Duration']

    ))


conn.commit()
cursor.close()
conn.close()

print("All CSV rows inserted into 'imdb_top_movies' table successfully!")
#code ends
