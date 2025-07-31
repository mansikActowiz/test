import pandas as pd
from sqlalchemy import create_engine

def export_database_to_csv(database_table_name, database_name, csv_path):
    user = "root"
    password = "Actowiz"
    host = "localhost"

    # Create engine for MySQL
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database_name}')

    try:
        # Read from database
        query = f"SELECT * FROM {database_table_name}"
        df = pd.read_sql(query, engine)

        # Save to CSV with headers
        df.to_csv(csv_path, index=False)

        print(f"Data from table '{database_table_name}' exported successfully to '{csv_path}'")
        return csv_path
    except Exception as e:
        print("Error:", e)
        return None

csv_output = r"C:\Users\Madri.Gadani\Desktop\madri\stay_vista\stay_vista_table_outputttttttt.csv"
# export_database_to_csv("stay_vista_table", "stay_vista", csv_output)

import pandas as pd
from sqlalchemy import create_engine

def export_selected_columns_to_csv(database_table_name, database_name, csv_path, selected_columns):
    """
    selected_columns should be a list of column names, e.g., ['name', 'price', 'rating']
    """
    user = "root"
    password = "Actowiz"
    host = "localhost"

    # Create engine
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database_name}')

    try:
        # Create column string for SQL
        column_string = ", ".join(selected_columns)
        query = f"SELECT {column_string} FROM {database_table_name}"

        # Read only selected columns
        df = pd.read_sql(query, engine)

        # Save to CSV
        df.to_csv(csv_path, index=False)

        print(f"Selected columns from '{database_table_name}' exported successfully to '{csv_path}'")
        return csv_path
    except Exception as e:
        print("Error:", e)
        return None
csv_output = r"C:\Users\Madri.Gadani\Desktop\madri\stay_vista\stay_vista_table_selected_col.csv"
export_selected_columns_to_csv("stay_vista_table", "stay_vista", csv_output, ['checkin_date','checkout_date','no_of_pax'])