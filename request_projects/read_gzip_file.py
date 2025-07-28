import gzip
gz_file_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_response.html.gz'

# Read and decode the content
with gzip.open(gz_file_path, 'rt', encoding='utf-8') as f:
    html_content = f.read()

# Print or use the HTML content
print(html_content)