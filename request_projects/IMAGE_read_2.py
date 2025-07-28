import pytesseract
from PIL import Image
import requests
from io import BytesIO
import re
import csv
# Set path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Madri.Gadani\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Load image from URL
url="https://b.zmtcdn.com/data/menus/194/18902194/54a40140bacf4d61da8b307dbb80c651.jpg?output-format=webp"
# url = "https://b.zmtcdn.com/data/menus/194/18902194/0d00360194db65479f8895058126366e.jpg?output-format=webp"
response = requests.get(url)

img = Image.open(BytesIO(response.content))
image_path = r'C:\Users\Madri.Gadani\Desktop\madri\converted_image_2.png'
img.save(image_path)

# Load image

img = Image.open(image_path)

# Use better OCR layout config
custom_config = r'--psm 6'
# custom_config = r'--psm 4'
text = pytesseract.image_to_string(img, lang='eng', config=custom_config)
print(text)


# Clean unwanted characters using regex
cleaned_text = re.sub(r'[^\w\s.,:/()%&+-]', '', text)  # Keep alphanum + selected symbols
cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)    # Replace multiple spaces with a single space
cleaned_text = re.sub(r'\n{2,}', '\n', cleaned_text)   # Remove multiple blank lines


lines = cleaned_text.strip().split('\n')

# Try to parse each line into 3 columns: Item, 30ML, Bottle
data = []
for line in lines:
    parts = line.strip().split()
    # If the last 2 parts are numbers (price), treat them as 30ML and BOTTLE
    if len(parts) >= 3 and parts[-2].isdigit() and parts[-1].isdigit():
        item = ' '.join(parts[:-2])
        glass = parts[-2]
        bottle = parts[-1]
        data.append([item, glass, bottle])
    else:
        data.append([line])  # If format doesn't match, just keep whole line

# Save to CSV
csv_path = r'C:\Users\Madri.Gadani\Desktop\madri\menu_2.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Item', '30ML', 'Bottle'])
    writer.writerows(data)


with open(r'C:\Users\Madri.Gadani\Desktop\madri\menu_2.txt', 'w', encoding='utf-8') as f:
    f.write(cleaned_text)

print("Extracted Text:\n", cleaned_text)
exit(0)
