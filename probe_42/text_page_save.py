import fitz  # PyMuPDF
import os


def save_pdf_pages_as_text(pdf_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)
    print(f"📄 Total pages: {len(doc)}")

    for i, page in enumerate(doc):
        text = page.get_text()
        filename = os.path.join(output_folder, f"page_{i + 1}.txt")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ Saved: {filename}")

    print("\n✅ All pages saved as .txt files.")


if __name__ == "__main__":
    pdf_file = r"C:\Users\Madri.Gadani\Desktop\madri\probe42\U28993MH1932PLC001828.pdf"
    output_dir = r"C:\Users\Madri.Gadani\Desktop\madri\probe42\pages_text"
    save_pdf_pages_as_text(pdf_file, output_dir)
