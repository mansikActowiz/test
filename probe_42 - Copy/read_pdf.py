import fitz  # PyMuPDF



def extract_and_print_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    print(f"📄 Total pages: {len(doc)}\n")

    for i, page in enumerate(doc):
        text = page.get_text()
        print(f"\n=== 📃 Page {i + 1} ===")
        print(text)
        print("=" * 50)

if __name__ == "__main__":
    pdf_file = r"C:\Users\Madri.Gadani\Desktop\madri\probe42\U28993MH1932PLC001828.pdf"
    extract_and_print_pdf_text(pdf_file)


