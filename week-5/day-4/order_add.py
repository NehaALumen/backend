from db_connection import connect_db , Error
from order_fetch import fetch_all_orders
from datetime import date
def add_order(date,cust_id):
    try:
        con=connect_db()
        if con is not None:
            cursor=con.cursor()
            query_params=(date,cust_id)
            query="insert into Orders(order_date,customer_id) values(%s,%s)"
            cursor.execute(query,query_params)
            con.commit()
            print(f"new order placed on {date} by customer {cust_id} is added successfully!")
    except Error as e:
        print(f"Error : {e}")
    finally:
        if con and con.is_connected():
            cursor.close()


add_order(date.today(),3)
fetch_all_orders()