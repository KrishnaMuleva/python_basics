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
    cursor.execute("SELECT version();")

    # Fetch the result
    db_version = cursor.fetchone()
    print(f"PostgreSQL version: {db_version[0]}")

except Exception as e:
    print(f"Error connecting to the database: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()

