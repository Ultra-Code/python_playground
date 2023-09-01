import mysql.connector as connector

# Establish connection b/w Python and MySQL database via connector API
connection = connector.connect(
    user="root",  # use your own
    password="",  # use your own
)
# Create a cursor object to communicate with entire MySQL database
cursor = connection.cursor()
# Set the little_lemon database for use
cursor.execute("use little_lemon")

# Confirm the database in use
print(connection.database)
cursor.execute("DROP PROCEDURE IF EXISTS TopSpender;")

# Task 1
# Stored procedure name >> TopSpender
# Our stored procedure query is
stored_procedure_query = """
CREATE PROCEDURE TopSpender()

BEGIN

SELECT bookings.BookingID,
CONCAT(
bookings.GuestFirstname,
' ',
bookings.GuestLastname
) AS CustomerName,
Orders.BillAmount
FROM Bookings
INNER JOIN
Orders ON bookings.BookingID=Orders.BookingID
ORDER BY BillAmount DESC LIMIT 1;

END

"""

# Execute the query
cursor.execute(stored_procedure_query)

# ********************************************#

# Call the stored procedure with its name
cursor.callproc("TopSpender")

# Retrieve recrods in "dataset"
results = next(cursor.stored_results())
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop
for column_id in cursor.stored_results():
    columns = [column[0] for column in column_id.description]

# Print column names
print(columns)

# Print data
for data in dataset:
    print(data)

# Task 3
# Stored procedure name >> OrderStatus
# Our stored procedure query is
stored_procedure_query = """
CREATE PROCEDURE OrderStatus()

BEGIN

SELECT bookingID,
CASE
WHEN employeeID IN (1,2,3) THEN "Order Served"
WHEN employeeID IN (4,5) THEN "Preparing Order"
ELSE "In Queue"
END AS Status
FROM Bookings;

END

"""

# Execute the query
cursor.execute(stored_procedure_query)

# ********************************************#

# Call the stored procedure with its name
cursor.callproc("OrderStatus")

# Retrieve recrods in "dataset"
results = next(cursor.stored_results())
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop
for column_id in cursor.stored_results():
    columns = [column[0] for column in column_id.description]

# Print column names
print(columns)

# Print data
for data in dataset:
    print(data)
