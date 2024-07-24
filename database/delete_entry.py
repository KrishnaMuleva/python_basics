import psycopg2

# Database connection parameters
db_params = {
    "dbname": "learning",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

# Establish the connection
try:
    connection = psycopg2.connect(**db_params)
    print("Connected to the database")

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a simple query
    cursor.execute("DELETE FROM student WHERE age=12")
    # Fetch the result
    connection.commit()
    print(cursor.rowcount, "deleted")

except Exception as e:
    print(f"Error connecting to the database: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()

