# install connector api using the command below.
# Import the MySQL Connector/Python
from mariadb import connect

# Establish connection between Python and MySQL database via connector API
connection = connect(
    user="megaalpha",
    password="",  # use your own
)

# Create cursor object to communicate with entire MySQL database
cursor = connection.cursor()

# If exist, drop the database first, and create again
try:
    cursor.execute("CREATE DATABASE little_lemon")
except:
    cursor.execute("drop database little_lemon")
    cursor.execute("CREATE DATABASE little_lemon")
print("The database little_lemon is created.\n")

# Set little_lemon database for use
cursor.execute("USE little_lemon")
print("The database little_lemon is set for use.\n")

# The SQL query for MenuItems table is:
create_menuitem_table = """
CREATE TABLE MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
);"""

# Create MenuItems table
cursor.execute(create_menuitem_table)
print("MenuItmes table is created.\n")

# The SQL query for Menu table is:
create_menu_table = """
CREATE TABLE Menus (
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY (MenuID,ItemID)
);"""

# Create Menu table
cursor.execute(create_menu_table)
print("Menu table is created.\n")

# The SQL query for Bookings table is:
create_booking_table = """
CREATE TABLE Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
);"""

# Create Bookings table
cursor.execute(create_booking_table)
print("Bookings table is created.\n")

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
cursor.execute(create_orders_table)
print("Orders table is created.\n")

# Confirm if the tables are created
print("Following tables are created in the little_lemon database.\n")
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
