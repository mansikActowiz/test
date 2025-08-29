import json
import pandas as pd

def process_json_to_custom_rows(data):
    rows = []

    for key, value in data.items():
        if isinstance(value, dict):
            # Special case: nested by sub-keys (e.g., date)
            for sub_key, sub_val in value.items():
                if isinstance(sub_val, (dict, list)):
                    rows.append([key, sub_key, json.dumps(sub_val, indent=2, ensure_ascii=False)])
                else:
                    rows.append([key, sub_key, sub_val])
        elif isinstance(value, list):
            if all(isinstance(i, (dict, list)) for i in value):
                rows.append([key, "", json.dumps(value, indent=2, ensure_ascii=False)])
            else:
                rows.append([key, "", ", ".join(map(str, value))])
        else:
            rows.append([key, "", value])
    return rows

# Paths
json_file_lst=[4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in json_file_lst:


    json_path = fr"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\json_file\output_json_page_{i}.json"
    print(json_path)

    csv_path = fr"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\csv_file\output_csv_page_page_{i}.csv"


# Read JSON and process
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # Convert to custom rows
    rows = process_json_to_custom_rows(json_data)

# Write to CSV
    df = pd.DataFrame(rows, columns=["Key", "Sub-Key", "Value"])
    df.to_csv(csv_path, index=False, encoding='utf-8')
    print(f"✅ CSV saved to: {csv_path}")
