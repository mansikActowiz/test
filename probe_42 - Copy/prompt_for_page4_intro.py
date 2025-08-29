import google.genai as genai
from google.genai import types

input_page=r"C:\Users\Madri.Gadani\Desktop\madri\probe42\pages_text\page_4.txt"



with open(input_page,"r") as f:
    raw=f.read()

def format_raw(raw_text):
    client = genai.Client(api_key='AIzaSyCpdfsogCuSZpE4sfi6-yzHAJT0vdeyVRw')
    # print(random.choice(keys))
    full_prompt = [raw_text + content]
    response = client.models.generate_content(
        # model='gemini-2.5-flash-lite-preview-06-17',
        # model='gemini-2.0-flash',
        model='gemma-3-4b-it',
        contents=full_prompt,
        config=genai.types.GenerateContentConfigDict(
            temperature = 0,
        )
    )
    return response.text









content = """
You are a data extraction assistant. Your task is to extract structured data from the following document text.

Please return the data in this JSON structure:

{
  "Key Statistics": {
    "company name": "",
    "Registered Address": "",
    "Business Address": "",
    "Date of Incorporation": "",
    "Company Type": "",
    "Listing Status": "",
    "Website": "",
    "Email": [],
    "Phone Numbers": [],
    "CIN": "",
    "PAN": "",
    "Paid Up Capital": "",
    "Authorized Capital": "",
    "Sum of Charges": "",
    "Company Status": "",
    "Active Compliance": "",
    "Date of Last AGM": "",
    "LEI": ""
  },
  "About The Company": "",
  "Industry And Segment(s)": {
    "Agro": "",
    "Consumer Durables": "",
    "Manufacturing": "",
    "Real Estate": ""
  },
  "Principal Business Activities - 31 Mar, 2024": [
    {
      "Main Activity Group Code": "",
      "Description of Main Activity Group": "",
      "Business Activity Code": "",
      "Description of Business Activity": "",
      "% of Turnover": ""
    }
  ]
}

Instructions:
- Use only the provided raw document content to fill in this structure.
- Return only a valid JSON. Do not include any explanation, markdown, or additional text.
"""



print(format_raw(raw))


import json

# Get model output as string
output = format_raw(raw)

# Remove markdown if present
if output.strip().startswith("```json"):
    output = output.strip()[7:-3].strip()

# Convert string to Python dict
try:
    data = json.loads(output)
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
    exit()

# Save as .json
json_path = "output_page4.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Saved JSON to {json_path}")

import pandas as pd



import json
import pandas as pd

# Load JSON data
with open("output_page4.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Flatten nested dicts and format lists
def flatten_for_rows(d, parent_key=''):
    rows = []
    if isinstance(d, dict):
        for k, v in d.items():
            full_key = f"{parent_key}.{k}" if parent_key else k
            rows.extend(flatten_for_rows(v, full_key))
    elif isinstance(d, list):
        # Join list items as comma-separated string
        value = ', '.join(map(str, d))
        rows.append((parent_key, value))
    else:
        rows.append((parent_key, d))
    return rows

# Flatten and convert to DataFrame
rows = flatten_for_rows(data)
df = pd.DataFrame(rows, columns=["Key", "Value"])

# Save to Excel
excel_path = "output_page4_key_value.xlsx"
df.to_excel(excel_path, index=False)

print(f"✅ Excel saved as: {excel_path}")