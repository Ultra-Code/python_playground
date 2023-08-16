import sys

import mariadb as db

try:
    connection = db.connect(
        user="megaalpha",
        password="",
        host="localhost",
        port=3306,
        # database="employees",
    )
except db.Error as err:
    print(f"Error: {err}")
    sys.exit(3)

cursor = connection.cursor()

# If exist, drop the database first
# cursor.execute("drop database little_lemon")

# Create database and checking all that we have!
cursor.execute("CREATE DATABASE IF NOT EXISTS little_lemon")
# Set little_lemon database for use
cursor.execute("USE little_lemon")

# Confirm the database in use
assert connection.database == "little_lemon"

cursor.execute("SHOW DATABASES")
for database in cursor:
    print(database)

# The SQL query for Bookings table is:
create_orders_table = """
CREATE TABLE Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""

# Create Orders table
# cursor.execute(create_orders_table)

# Confirm if the table is created
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
# retrieving information
# some_name = "Georgi"
# cursor.execute(
#     "SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,)
# )
#
# for first_name, last_name in cursor:
#     print(f"First name: {first_name}, Last name: {last_name}")
#
# # insert information
# try:
#     cursor.execute(
#         "INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria", "DB")
#     )
# except db.Error as e:
#     print(f"Error: {e}")
#
connection.commit()
# print(f"Last Inserted ID: {cursor.lastrowid}")
connection.close()
