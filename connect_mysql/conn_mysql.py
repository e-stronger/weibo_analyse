import pandas as pd
import pymysql

def create_connection(host_name, user_name, user_password, db_name):
    connection = pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=db_name
    )
    print("Connection to MySQL DB successful")
    return connection

def create_table(connection, table_name, df):
    cursor = connection.cursor()
    columns = ", ".join([f"{col} VARCHAR(255)" for col in df.columns])
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cursor.execute(create_table_query)
    connection.commit()
    print(f"Table {table_name} created successfully")

def insert_data(connection, table_name, df):
    cursor = connection.cursor()
    for _, row in df.iterrows():
        values = ", ".join([f"'{value}'" for value in row])
        insert_query = f"INSERT INTO {table_name} VALUES ({values})"
        cursor.execute(insert_query)
    connection.commit()
    print("Data inserted successfully")

# MySQL database configuration
host = 'localhost'
user = 'your_username'
password = 'your_password'
database = 'weibo'

# Excel file path
excel_file = 'your_excel_file.xlsx'

# Read Excel file
df = pd.read_excel(excel_file)

# Connect to MySQL database
connection = create_connection(host, user, password, database)

# Create a table for the Excel data
table_name = 'excel_data'
create_table(connection, table_name, df)

# Insert data into the table
insert_data(connection, table_name, df)

# Close the connection
connection.close()