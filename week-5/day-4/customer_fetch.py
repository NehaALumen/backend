from db_connection import connect_db, Error
def fetch_all_customers():
    con=connect_db()
    if con is not None:
        try:
            cursor=con.cursor()
            query="select * from Customer"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f"{row[0]}.){row[1]}'s contact info email: {row[2]} Phone: {row[3]} ")
        finally:
            cursor.close()
            con.close()

def fetch_customer(id):
    try:
        con=connect_db()
        if con is not None:
            cursor=con.cursor()
            query="select * from Customer where id=%s"
            cursor.execute(query,(id,))
            print(cursor.fetchall())
    finally:
        cursor.close()
        con.close()

