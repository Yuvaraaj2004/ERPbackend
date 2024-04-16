import psycopg2

# Define the connection parameters
dbname = 'Project'
user = 'postgres'
password = 'root'  # Replace 'your_password' with your actual password
host = 'localhost'
port = '5432'

# Construct the connection string
conn_string = f"dbname='{dbname}' user='{user}' password='{
    password}' host='{host}' port='{port}'"

# Establish the connection
conn = psycopg2.connect(conn_string)

# Create a cursor object
cursor = conn.cursor()
print("connection established")
# Perform database operations using the cursor

# Close the cursor
cursor.close()

# Commit the transaction (if needed)
conn.commit()

# Close the connection
conn.close()
