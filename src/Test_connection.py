from mysql.connector import connect, Error

config = {
    "host": "127.0.0.1",
    "user": "home_inventory_user",
    "password": "your_password",  # Leave blank if no password
    "database": "home_inventory",
    "port": 8889,
}

try:
    connection = connect(**config)
    print("Connection successful!")
    connection.close()
except Error as e:
    print(f"Error: {e}")