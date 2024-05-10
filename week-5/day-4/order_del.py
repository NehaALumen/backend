from db_connection import connect_db , Error
from order_fetch import fetch_all_orders
from datetime import date
def order_del(id):
    try:
        con=connect_db()
        if con is not None:
            cursor=con.cursor()
            query_params=(id,)
            query="delete from orders where order_id=%s"
            cursor.execute(query,query_params)
            con.commit()
            print("order deleted successfully!")
    except Error as e:
        print(f"Error : {e}")
    finally:
        if con and con.is_connected():
            cursor.close()
            con.close()

order_del(55)
fetch_all_orders()