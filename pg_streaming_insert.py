import os
import psycopg2
from faker import Faker
import time
 
# Replace with your PostgreSQL credentials and database name
db_host = os.environ['db_host_name']
db_port = os.environ['db_port_number']
db_user = os.environ['db_user_name']
db_password = os.environ['db_password_value']
db_name = os.environ['db_name_value']
 
def insert_into_products(cursor, num_items):
    fake = Faker()
 
    for _ in range(num_items):
        product_name = fake.word()
        price = fake.random_number(digits=4) / 100.0
        description = fake.sentence()
 
        insert_query = "INSERT INTO products (product_name, price, description) VALUES (%s, %s, %s);"
        cursor.execute(insert_query, (product_name, price, description))
 
    print(f"{num_items} rows inserted into products table.")
 
def insert_into_employees(cursor, num_items):
    fake = Faker()
 
    for _ in range(num_items):
        first_name = fake.first_name()
        last_name = fake.last_name()
        department = fake.job()
        hire_date = fake.date_between(start_date='-5y', end_date='today')
 
        insert_query = "INSERT INTO employees (first_name, last_name, department, hire_date) VALUES (%s, %s, %s, %s);"
        cursor.execute(insert_query, (first_name, last_name, department, hire_date))
 
    print(f"{num_items} rows inserted into employees table.")
 
if __name__ == "__main__":
    # Establish connection
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
 
    # Create a cursor object using the connection
    cur = conn.cursor()
 
    try:
        while True:
            # Insert into products table
            insert_into_products(cur, num_items=3)
 
            # Insert into employees table
            insert_into_employees(cur, num_items=2)
 
            conn.commit()
            print("Data inserted successfully.")
 
            # Sleep for 10 seconds
            time.sleep(10)
 
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Error inserting data: {e}")
 
    finally:
        # Close cursor and connection
        cur.close()
        conn.close()