import mysql.connector
def display(table_name):
        # Display
    print("-----Table-----")
    query = f"SELECT * FROM company.{table_name}"
    cursor.execute(query)
    for item in cursor.fetchall():
        print(item)
    else:
        print("Empty")
try:
    connect = mysql.connector.connect(
    host= "localhost", 
    user= "root", 
    password= "root", 
    database="company")

    print(connect.is_connected())
    cursor = connect.cursor()
    # # Create
    print("-----Create-----")
    table_name = str(input("Enter table name: "))
    query = f"CREATE TABLE {table_name}(uid int PRIMARY KEY NOT NULL, uname varchar(20), age int, email_id varchar(50))"
    cursor.execute(query)
    display(table_name)
    # # Insert
    print("-----Insert-----")
    query = "INSERT INTO users(uid, uname, age, email_id) VALUES (%s, %s, %s, %s)"
    entries = int(input("Enter the number of entries: "))
    for i in range (0, entries):    
        values = [int, str, int, str]
        print(f"Entry {i+1}:")
        values[0] = input("Enter your User ID: ")
        values[1] = input("Enter your Username: ")
        values[2] = input("Enter your Age: ")
        values[3] = input("Enter your Email ID: ")

        cursor.execute(query, values)
    
    # # Update
    print("-----Update Age-----")
    query = "UPDATE users SET age = %s WHERE uid = %s"
    values = [int, int]
    values[1] = input("Enter the UID for updation: ")
    values[0] = input("Enter new Age: ")
    cursor.execute(query, values)

    # # Delete
    print("-----Delete-----")
    query = "DELETE FROM users WHERE uid = %s"
    value = [int]
    value[0] = int(input("Enter the UID to be deleted: "))
    cursor.execute(query, value)

    display(table_name)
    
    # # Drop
    query = "DROP TABLE users;"
    cursor.execute(query)
    cursor.close()

    connect.commit()

except mysql.connector.Error as err:
    print("ERROR:",err)
