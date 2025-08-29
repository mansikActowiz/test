from sqlalchemy import create_engine, Table, MetaData, select

# DB Config
user = "root"
password = "Actowiz"
host = "localhost"
database_name = "probe24"

# Create engine
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database_name}')
metadata = MetaData()

# Reflect the table (correct way in SQLAlchemy 2.0+)
pdf_pages = Table('pdf_pages', metadata, autoload_with=engine)

# Query all rows
with engine.connect() as connection:
    stmt = select(pdf_pages)
    result = connection.execute(stmt).mappings()

    for row in result:
        pdf_name = row['pdf_name']
        page_number = row['page_number']
        content = row['content']

        print(f"\n=== 📄 PDF: {pdf_name} | Page {page_number} ===")
        print(content)  # Replace with actual extraction logic
        print("=" * 80)
