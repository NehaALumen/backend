from db_connection import connect_db, Error
from customer_fetch import fetch_customer,fetch_all_customers

def update_customer_email(new_email,id):
    try:
        con=connect_db()
        if con is not None:
            cursor=con.cursor()
            query_params=(new_email,id)
            query="update Customer set email=%s where id=%s"
            cursor.execute(query,query_params)
            con.commit()
            print("email successfully changed!")
    except Error as e:
        print(f"error : {e}")
    finally:
        if con and con.is_connected():
            cursor.close()
            con.close()

def update_customer_phone(new_phone,id):
    try:
        con=connect_db()
        if con is not None:
            cursor=con.cursor()
            query_params=(new_phone,id)
            query="update Customer set phone=%s where id=%s"
            cursor.execute(query,query_params)
            con.commit()
            print("phone successfully changed!")
    except Error as e:
        print(f"error : {e}")
    finally:
        if con and con.is_connected():
            cursor.close()
            con.close()

def update_customer_name(new_name,id):
    try:
        con=connect_db()
        if con is not None:
            cursor=con.cursor()
            query_params=(new_name,id)
            query="update Customer set customer_name=%s where id=%s"
            cursor.execute(query,query_params)
            con.commit()
            print("customer name successfully changed!")
    except Error as e:
        print(f"error : {e}")
    finally:
        if con and con.is_connected():
            cursor.close()
            con.close()


update_customer_email("nhj@gmail.com",6)
fetch_all_customers()
update_customer_phone("???-???-????",5)
fetch_all_customers()
update_customer_name("tina arora",6)
fetch_all_customers()