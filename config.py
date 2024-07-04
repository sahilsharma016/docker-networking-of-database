
# just for testing envirmoment


import pymysql

# Database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Password@123',
    database='database1',  # Replace with your actual database name
    port=3306
)

def create_table():
    with connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
        """)
    connection.commit()

def register_user(username, email, password):
    with connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO users (username, email, password)
        VALUES (%s, %s, %s)
        """, (username, email, password))
    connection.commit()

# Create table if it doesn't exist
create_table()

