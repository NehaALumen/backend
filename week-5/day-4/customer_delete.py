from db_connection import connect_db, Error
from customer_fetch import fetch_customer, fetch_all_customers

def customer_del(id):
    try:
        con=connect_db()
        if con is not None:
            cursor=con.cursor()
            query_params=(id,)
            query="delete from Customer where id=%s"
            cursor.execute(query,query_params)
            con.commit()
            print("customer deleted successfully!")
    except Error as e:
        print(f"Error : {e}")
    finally:
        if con and con.is_connected():
            cursor.close()
            con.close()

def delete_customer_wno(id): #only deletes customers with no associated orders
    con=connect_db()
    try:
        cursor=con.cursor()
        query="select * from orders where order_id=%s"
        query_params=(id,)
        cursor.execute(query,query_params)
        orders=cursor.fetchall()
        if orders:
            customer_del(id)
        else:
            print("cannot delete a user who has associated orders")
    except Error as e:
        print(f"Error : {e}")
    finally:
        if con and con.is_connected():
            cursor.close()
            con.close()



customer_del(6)
fetch_all_customers()
delete_customer_wno(5)
fe