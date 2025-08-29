import pandas as pd
import os

import pandas as pd
import os
import re

def natural_sort_key(s):
    # Extract numbers from filenames for natural ordering
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

def merge_csvs_rowwise_in_order(input_folder, output_file):
    all_dfs = []

    # List and sort CSV files using natural order (e.g., page4 < page10)
    files = [f for f in os.listdir(input_folder) if f.endswith(".csv")]
    sorted_files = sorted(files, key=natural_sort_key)

    for file in sorted_files:
        file_path = os.path.join(input_folder, file)
        df = pd.read_csv(file_path)
        df['Source File'] = file  # Optional: track source file
        all_dfs.append(df)

    merged_df = pd.concat(all_dfs, ignore_index=True)
    merged_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"✅ Merged CSV saved at: {output_file}")

# 🔁 Set your paths:
# input_csv_folder = r"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\json_file\csvs"
# output_csv_path = r"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\json_file\merged_all.csv"

input_csv_folder = fr"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\csv_file"
# input_csv_folder = r"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\json_file\csvs"  # Folder with all CSVs
output_csv_path = r"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\csv_file\merged_all1.csv"

merge_csvs_rowwise_in_order(input_csv_folder, output_csv_path)



#
#
# def merge_csvs_rowwise(input_folder, output_file):
#     all_dfs = []
#
#     for file in os.listdir(input_folder):
#         if file.endswith(".csv"):
#             file_path = os.path.join(input_folder, file)
#             df = pd.read_csv(file_path)
#             df['Source File'] = file  # Optional: track source file
#             all_dfs.append(df)
#
#     merged_df = pd.concat(all_dfs, ignore_index=True)
#     merged_df.to_csv(output_file, index=False, encoding='utf-8')
#     print(f"✅ Merged CSV saved at: {output_file}")
#
# # 🔁 Replace these paths:
# input_csv_folder = fr"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\csv_file"
# # input_csv_folder = r"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\json_file\csvs"  # Folder with all CSVs
# output_csv_path = r"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\csv_file\merged_all.csv"
#
# merge_csvs_rowwise(input_csv_folder, output_csv_path)
