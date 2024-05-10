from db_connection import connect_db, Error
def fetch_all_orders():
    con=connect_db()
    if con is not None:
        try:
            cursor=con.cursor()
            query="select * from orders"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        finally:
            cursor.close()
            con.close()
def fetch_order(cid,oid):
    try:
        con=connect_db()
        if con is not None:
            cursor=con.cursor()
            query="select * from orders where order_id=%s and customer_id=%s"
            cursor.execute(query,(oid,cid))
            print(cursor.fetchall())
    finally:
        cursor.close()
        con.close()

fetch_all_orders()
fetch_order(2,56)