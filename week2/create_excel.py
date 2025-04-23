import openpyxl
from faker import Faker
import random

# Initialize Faker for generating random data
fake = Faker()

# Create a new workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Define column headers
headers = ["First Name", "Middle Name", "Last Name", "Age", "City", "Country", "Zip Code", "Job"]
sheet.append(headers)

# Generate 100 random rows
for _ in range(100):
    first_name = fake.first_name()
    middle_name = fake.first_name()  # Using first_name for middle name variety
    last_name = fake.last_name()
    age = random.randint(18, 80)  # Random age between 18 and 80
    city = fake.city()
    country = fake.country()
    zip_code = fake.zipcode()
    job = fake.job()
    
    # Append row to sheet
    sheet.append([first_name, middle_name, last_name, age, city, country, zip_code, job])

# Save the workbook
workbook.save("random_people_data.xlsx")
print("Excel file 'random_people_data.xlsx' created successfully with 100 rows.")