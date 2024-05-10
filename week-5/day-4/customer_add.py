from db_connection import connect_db , Error
from customer_fetch import fetch_customer, fetch_all_customers
def add_customer(name, email,phone):
    try:
        con=connect_db()
        if con is not None:
            cursor=con.cursor()
            new_cust=(name,email,phone)
            query="insert into Customer(customer_name, email, phone) values(%s,%s,%s)"
            cursor.execute(query,new_cust)
            con.commit()
            print(f"new customer {name} added successfully!")
    except Error as e:
        print(f"Error : {e}")
    finally:
        if con and con.is_connected():
            cursor.close()
            con.close()


add_customer("neha arora","gg@gg.com","555-555-5555")
add_customer("palp's daughter","notaskywalker@confusion.com","666-666-6666")
fetch_all_customers()