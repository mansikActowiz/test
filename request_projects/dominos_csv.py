import pandas as pd
import csv
import json

json_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\dominos\dominos_json.json'


csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\dominos\dominos_csv.csv'
df=pd.read_json(json_output_path)
df.to_csv(csv_output_path,index=False)
