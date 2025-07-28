import google.genai as genai
from google.genai import types

import json


def format_raw(raw_text):
    client = genai.Client(api_key='AIzaSyCpdfsogCuSZpE4sfi6-yzHAJT0vdeyVRw')

    full_prompt = [raw_text + content]

    # full_prompt = [content + "\n\n" + raw_text]

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




content="""
You are a structured document extraction assistant.

You are given text from a formatted PDF that follows this consistent structure:

- Each section starts with a **blue heading row** — treat this as the top-level key (e.g., "Profit and Loss - AOC-4 (Rs. Crore)")
- The second column of the heading (usually a date like "31 Mar, 2024") should be treated as the second-level key
- Each **bold line or row** below that is a category or heading — treat that as a third-level key (e.g., "Operating Cost", "Other Expenses")
- Below each third-level key are **key-value pairs**: the left side is the sub-label, the right side is the value (these may align vertically or be grouped)

---

### Your task:
1. Extract all data and structure it as clean, nested JSON.
2. Use this pattern:

```json
{
  "Section Name (blue header)": {
    "Date (column 2)": {
      "Subsection Label (bold line)": {
        "Metric Label 1": "Value 1",
        "Metric Label 2": "Value 2"
      },
      ...
    }
  }
}
⚠️ IMPORTANT JSON FORMATTING RULES:
- Return only valid JSON.
- Ensure every key and value is properly enclosed in double quotes.
- Do NOT use markdown code fences like ```json
- Do NOT include any explanation, commentary, or extra text.
- No trailing commas at the end of objects or arrays.
- Your entire response must be just one valid JSON object.

"""
# page_list=[6,7,8,9,10,]

for i in range(26,35):


    input_page=fr"C:\Users\Madri.Gadani\Desktop\madri\probe42\pages_text\page_{i}.txt"


    with open(input_page,"r") as f:
        raw=f.read()


    print(format_raw(raw))
    print(f'------------------page:{i}------------------------')



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
    json_path = fr"C:\Users\Madri.Gadani\PycharmProjects\PythonProject\probe_42\json_file\output_json_page_{i}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved JSON to {json_path}")


