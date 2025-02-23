import psycopg2
import os
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Get environment variables
DB_CONFIGS = {
    "store_1_db": {
        "dbname": os.getenv("STORE_1_DB_NAME"),
        "user": os.getenv("STORE_1_DB_USER"),
        "password": os.getenv("STORE_1_DB_PASSWORD"),
        "host": os.getenv("STORE_1_DB_HOST"),
        "port": os.getenv("STORE_1_DB_PORT"),
    },
    "store_2_db": {
        "dbname": os.getenv("STORE_2_DB_NAME"),
        "user": os.getenv("STORE_2_DB_USER"),
        "password": os.getenv("STORE_2_DB_PASSWORD"),
        "host": os.getenv("STORE_2_DB_HOST"),
        "port": os.getenv("STORE_2_DB_PORT"),
    },
}

PRODUCTS = [
    ("Apple", "Groceries"), ("Banana", "Groceries"), ("Milk", "Groceries"),
    ("Laptop", "Electronics"), ("Smartphone", "Electronics"), ("T-shirt", "Clothing"),
]

def generate_sales_data(store_id, num_records=100):
    sales_data = []
    for _ in range(num_records):
        product_name, category = random.choice(PRODUCTS)
        quantity_sold = random.randint(1, 20)
        unit_price = round(random.uniform(5, 1000), 2)
        sale_date = fake.date_time_between(start_date="-30d", end_date="now").strftime('%Y-%m-%d %H:%M:%S')
        sales_data.append((store_id, product_name, category, quantity_sold, unit_price, sale_date))
    return sales_data

def insert_sales_data(db_name, store_id, num_records=100):
    conn = psycopg2.connect(**DB_CONFIGS[db_name])
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO sales (store_id, product_name, category, quantity_sold, unit_price, sale_date) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    sales_data = generate_sales_data(store_id, num_records)

    cursor.executemany(insert_query, sales_data)
    conn.commit()

    print(f"Inserted {num_records} records into {db_name}.sales")
    cursor.close()
    conn.close()

num_records = int(os.getenv("RECORDS_TO_INSERT", 1000))
insert_sales_data("store_1_db", store_id=1, num_records=num_records)
insert_sales_data("store_2_db", store_id=2, num_records=num_records)

