import google.genai as genai
from google.genai import types

input_page=r"C:\Users\Madri.Gadani\Desktop\madri\probe42\pages_text\page_4.txt"
# input_page=r"C:\Users\Madri.Gadani\Desktop\madri\probe42\pages_text\page_6.txt"


with open(input_page,"r") as f:
    raw=f.read()
    # print(raw) #will print from text file

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
You are a data extraction assistant.

From the raw business document below, extract all meaningful structured data in JSON format. Use section headers, labels, or bolded phrases as keys, and their corresponding values as values.

Instructions:
- Infer keys dynamically based on headings or bolded labels (like "Name", "Net Revenue", "Auditor", etc.)
- If values are grouped under a heading, create a nested dictionary using that heading as the parent key
- Use arrays for repeated items (e.g., transactions, directors, business activities)
- Preserve the original wording as much as possible
- Include all factual numeric and textual data — ignore disclaimers, footers, page numbers
- Do NOT make up or guess values. Only use what is provided.
- Return only valid, compact JSON without markdown or extra text.
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
json_path = r"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\json_file\output_page4.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Saved JSON to {json_path}")



# # Flatten nested dicts and lists
# def flatten_for_rows(d, parent_key=''):
#     rows = []
#     if isinstance(d, dict):
#         for k, v in d.items():
#             full_key = f"{parent_key}.{k}" if parent_key else k
#             rows.extend(flatten_for_rows(v, full_key))
#     elif isinstance(d, list):
#         value = ', '.join(map(str, d))  # Flatten list
#         rows.append((parent_key, value))
#     else:
#         rows.append((parent_key, d))
#     return rows
#
# # Flatten the data
# flat_rows = flatten_for_rows(data)
#
# # Split compound keys into separate columns
# split_rows = []
# for full_key, value in flat_rows:
#     parts = full_key.split('.', 1)
#     if len(parts) == 2:
#         section, field = parts
#     else:
#         section = parts[0]
#         field = ""  # e.g. About The Company may not have a second part
#     split_rows.append((section, field, value))
#
# # Create DataFrame
# df = pd.DataFrame(split_rows, columns=["Section", "Field", "Value"])
#
# # Save to Excel
# excel_path = "output_page4_split_columns.xlsx"
# df.to_excel(excel_path, index=False)
#
# print(f"✅ Excel saved as: {excel_path}")







