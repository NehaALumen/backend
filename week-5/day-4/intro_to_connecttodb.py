import mysql.connector
from mysql.connector import Error

db_name="ecomm_db"
userr="root"
pwd="041413@Val"
hostt="localhost"
try:
    con= mysql.connector.connect(
    database=db_name,
    user=userr,
    password=pwd,
    host=hostt
    )
    if con.is_connected():
        print("connection to db established")
    cursor=con.cursor() #creating a cursor to act as a middleman between python and mysql
    query="select * from Customer"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

except Error as e:
    print(f"Error : {e}")
finally:
    if con and con.is_connected():
        con.close()
        print("MySQL connection is closed")

