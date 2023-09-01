import mysql.connector as connector
from mysql.connector import Error
from mysql.connector.pooling import MySQLConnectionPool

dbconfig = {"database": "little_lemon", "user": "root", "password": ""}

try:
    pool = MySQLConnectionPool(
        pool_name="ll_pool_a", pool_size=3, **dbconfig  # default is 5
    )
    print("The connection pool is created with a name: ", pool.pool_name)
    print("The pool size is:", pool.pool_size)

except Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)

# Get the connection from the connection pool "pool"
print("Getting a connection from the pool.")
connection1 = pool.get_connection()

# print("A user with connection id {} is connected to the database.".format(
#    connection1.connection_id))

# db_Info = connection1.get_server_info()
# print("MySQL server version is:", db_Info)

# Create cursor object to communicate with entire MySQL database
print("Creating a cursor object.")
cursor = connection1.cursor()

# The SQL query is:
sql_query = "SELECT BookingId, GuestFirstName, GuestLastName FROM Bookings;"

# Execute query
print("Executing the SQL query.")
cursor.execute(sql_query)

# Fetch all results that satisfy the query
print("Fetching the query results.")
results = cursor.fetchall()

# Retrieve column names
print("Retrieving the column names.")
cols = cursor.column_names

# Print column names and records in "results" using for loop
print("Printing the results.\n")
print("""Upcoming Bookings are:\n""")
print(cols)
for result in results:
    print(result)

# Put the connection back to the pool
print("\nReturning the connection back to the pool.")
connection1.close()
print("The connection is placed back into the pool for the next user to connect.")

# List of the guests who want to connect to the database
guests = ["Anna", "Marcos", "Diana", "Joakim", "Hiroki"]

# To add connection to the pool, the connection must be of MySQLConnection instance
# Also possible to create via connect module and need the import below

# Assign connection to each user
for guest in guests:
    try:
        guest_connected = pool.get_connection()
        print(f"[{guest}] is connected.\n")
    except Error:
        print("No more connections are available.")
        print("Adding new connection in the pool.")

        # Create a connection
        connection = connector.connect(user="root", password="")
        # Add the connection into the pool
        pool.add_connection(cnx=connection)
        print("A new connection is added in the pool.\n")

        user_connected = pool.get_connection()
        print(f"[{guest}] is connected.\n")
