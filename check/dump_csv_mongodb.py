import pandas as pd
import sys
from pymongo import MongoClient

csv_output_path=r"C:\Users\Madri.Gadani\Desktop\madri\database_programs\personal_data1.csv"
df = pd.read_csv(csv_output_path)
print(df)



'''connect to mongodb'''

client = MongoClient("mongodb://localhost:27017/")  # or use your Mongo URI
db = client["example"]  # replace with your database name
collection = db["example_collection"]   # replace with your collection name

print('hhhhhhhhhhhhhhhh')

print(client)


print("Total documents in collection:", collection.count_documents({}))

# Optionally: print first 5 documents
#for doc in collection.find().limit(5):
#    print(doc)


data = df.to_dict(orient="records")
collection.insert_many(data)

print("Data inserted successfully into MongoDB!")