# Create a cursor object
from mariadb import connect

# Establish connection between Python and MySQL database via connector API
connection = connect(
    user="megaalpha",
    password="",  # use your own
)

cursor = connection.cursor(buffered=True)

# Set the “little_lemon” database for use
cursor.execute("""USE little_lemon;""")
print("The little_lemon database is set for use.")

# Retrieve records from bookings
cursor.execute("""SELECT * FROM Bookings;""")
print("All records from Bookings table are retrieved.")

# Retrieve records from orders
cursor.execute("""SELECT * FROM Orders;""")
print("All records from Orders table are retrieved.")

dict_cursor = connection.cursor(dictionary=True)

# Execute SQL query to get the name of the tables
dict_cursor.execute("show tables;")

# Retrieve query results in a variable ‘results’
results = dict_cursor.fetchall()

# Use for loop to print the names of all the tables
for table in results:
    print(table)

cursor.close()
dict_cursor.close()

