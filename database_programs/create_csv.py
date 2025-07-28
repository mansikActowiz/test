import pandas as pd
from faker import Faker
import random

fake = Faker()

# Customize number of rows and columns
num_rows = 10000

# Define your columns
def generate_row():
    return {
        "person_name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=90),
        "city": fake.city(),
        "state": fake.state(),
        "country": fake.country(),
        "zip": fake.zipcode(),
        "company": fake.company(),
        "job": fake.job(),
        "salary": round(random.uniform(30000, 150000), 2),
        "join_date": fake.date_this_decade(),
        "last_login": fake.date_time_this_year(),
        "is_active": random.choice([True, False])
    }

# Generate dataset
data = [generate_row() for _ in range(num_rows)]
df = pd.DataFrame(data)
print(df.columns)

csv_output_path=r"C:\Users\Madri.Gadani\Desktop\madri\database_programs\personal_data1.csv"
# Save to CSV
df.to_csv(csv_output_path, index=False)

print(" Generated fake_data.csv with 10,000 rows.")
