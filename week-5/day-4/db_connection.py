import mysql.connector
from mysql.connector import Error
def connect_db():
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
            return con
    except Error as e:
        print(f"Error : {e}")
        return None