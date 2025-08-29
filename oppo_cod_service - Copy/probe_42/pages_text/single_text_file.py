import google.genai as genai
from google.genai import types
import os
# page=r"C:\Users\Madri.Gadani\Desktop\madri\probe42\pages_text"
# page=r"C:\Users\Madri.Gadani\Desktop\madri\probe42\pages_text\page_9.txt"
page=r"C:\Users\Madri.Gadani\Desktop\madri\probe42\pages_text\page_4.txt"


with open(page,"r") as f:
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

content="""
You are a data extraction assistant. Your task is to parse the following text and extract all meaningful key-value pairs in a structured format.

Identify all distinct keys (e.g., line items, labels, or categories) and their corresponding numerical or textual values .
If multiple time periods or columns exist (like years or quarters), map each value accordingly.
Ensure numbers are extracted accurately, preserving decimals and negative signs if present.
Ignore general descriptions, footers, page numbers, and disclaimer text unless they contain valuable key-value information.
Return the output strictly in JSON format without markdown.
"""
print(format_raw(raw))