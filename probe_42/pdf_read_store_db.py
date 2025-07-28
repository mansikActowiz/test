import fitz  # PyMuPDF
import os
from sqlalchemy import create_engine, Table, Column, Integer, String, Text, MetaData
from sqlalchemy.exc import SQLAlchemyError

# Database credentials
user = "root"
password = "Actowiz"
host = "localhost"
database_name = "probe24"  # <-- replace this

# Create SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database_name}', echo=False)
metadata = MetaData()

# Define table schema
pdf_pages = Table(
    'pdf_pages', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('pdf_name', String(255)),
    Column('page_number', Integer),
    Column('content', Text)
)

# Create table if it doesn't exist
metadata.create_all(engine)

def extract_and_save_pdf_text(pdf_path):
    pdf_name = os.path.basename(pdf_path)
    doc = fitz.open(pdf_path)
    print(f"📄 Total pages: {len(doc)}\n")

    with engine.begin() as connection:  # ensures commit
        for i, page in enumerate(doc):
            text = page.get_text()
            print(f"\n=== 📃 Page {i + 1} ===")
            print(text[:200])  # Preview first 200 characters
            print("=" * 50)

            try:
                insert_stmt = pdf_pages.insert().values(
                    pdf_name=pdf_name,
                    page_number=i + 1,
                    content=text
                )
                connection.execute(insert_stmt)
            except SQLAlchemyError as e:
                print(f"❌ Error inserting page {i + 1}: {str(e)}")

    print("\n✅ PDF content saved to MySQL database successfully.")



#
# def extract_and_save_pdf_text(pdf_path):
#     pdf_name = os.path.basename(pdf_path)
#     doc = fitz.open(pdf_path)
#     print(f"📄 Total pages: {len(doc)}\n")
#
#     with engine.connect() as connection:
#         for i, page in enumerate(doc):
#             text = page.get_text()
#             print(f"\n=== 📃 Page {i + 1} ===")
#             print(text[:200])  # Preview first 200 characters
#             print("=" * 50)
#
#             try:
#                 insert_stmt = pdf_pages.insert().values(
#                     pdf_name=pdf_name,
#                     page_number=i + 1,
#                     content=text
#                 )
#                 connection.execute(insert_stmt)
#             except SQLAlchemyError as e:
#                 print(f"❌ Error inserting page {i + 1}: {str(e)}")
#
#     print("\n✅ PDF content saved to MySQL database successfully.")


if __name__ == "__main__":
    pdf_file = r"C:\Users\Madri.Gadani\Desktop\madri\probe42\U28993MH1932PLC001828.pdf"
    extract_and_save_pdf_text(pdf_file)























# import fitz  # PyMuPDF
# from sqlalchemy import create_engine, Table, Column, Integer, String, Text, MetaData
# from sqlalchemy.exc import SQLAlchemyError
# import os
#
#
#
# def extract_and_print_pdf_text(pdf_path):
#     doc = fitz.open(pdf_path)
#     print(f"📄 Total pages: {len(doc)}\n")
#
#     for i, page in enumerate(doc):
#         text = page.get_text()
#         print(f"\n=== 📃 Page {i + 1} ===")
#         print(text)
#         print("=" * 50)
#
# if __name__ == "__main__":
#     pdf_file = r"C:\Users\Madri.Gadani\Desktop\madri\probe42\U28993MH1932PLC001828.pdf"
#     extract_and_print_pdf_text(pdf_file)


