

      
import sys
import csv
import pymysql
import os
from dotenv import load_dotenv





#------------------------------------------------General Program functions---------------------------------------------------------------

        
        

def exit_program():   
    print("Thank you for using our app")
    sys.exit()
    

def print_main_menu():
    main_menu = int(input("""------------Main menu------------
Please choose one of the selections below
[0] To exist the program 
[1]To view the product menu
[2]To view the courier menu
[3]To view the order menu\n"""))
    while(True):
        if main_menu == 1:
            print_product_menu()
        elif main_menu ==2:
            print_courier_menu()
        elif main_menu ==3:
            print_order_menu()
        elif main_menu==0:
            exit_program()
        





#---------------------------------Functions to be used between each menu----------------------------------------------------------------

def get_new_name(name_choice):#Function to get new name for order/courier/order
    name = input("Please enter a name for the {}: ".format(name_choice))
    return name

def get_price_of_product(user_input):
    print("Please enter the new price of the product:" )
    price = float(user_input())
    return price

def get_phone_number(number_choice): #This function is to get the new number for courier/order
    new_number = input("Please enter the number of the {}: ".format(number_choice))
    return new_number

def get_id(noun,verb): #get id of product/courier/order you would like to update
    chosen_id= int(input("Please select the {} id you would like to {} or 0 to cancel: ".format(noun,verb)))
    if chosen_id ==0:
        print_main_menu()
    else:
        return chosen_id
    
def get_new_address():
    create_new_address = input("Please enter the new address you would like to add to the order: ")
    return create_new_address

def menu_optimized(menu_name):
        secondary_menu= int(input( """---------------------------         
          {0} Menu
---------------------------
[0]To return to Main menu      
[1]Show {0} options
[2]Create a new {0}  
[3]update a {0}
[4]Delete a {0}\n""".format(menu_name))) 
        return secondary_menu
    

#------------------------------------Functions for ORDER: Select ID from products and then added to a list of IDs.
    
def select_id_from_product_list(): #choose what product IDs you want to add to your order
     connect_to_product()
     selected_id = input("Please select the id you would like to or 0 to cancel: ")
     if selected_id ==0:
         print_main_menu()
     mylist = []
     while(True):
         mylist.append(selected_id)
         selected_id =input("Select another ID or Enter when you are done: ")
         if selected_id =="":
             break
     return mylist   
    
def convert_product_list_int(): #converts list returned from select_id_from_list into a string
    new_list=[]
    my_list = select_id_from_product_list()
    for item in my_list:
        new_list.append(int(item))
    print("Your product ID list is: ",new_list)
    return str(new_list)
    
    
#-------------------------------Functions for ORDER: Select ID from courier list----------------------------------------------------------

def select_id_from_courier_list():
    connect_to_courier()
    select_id = int(input("Please select a courier ID from the list above: ")) #need to verify if they have chosen the correct ID loop through list or data base
    return select_id




#-----------------------------Varaibles &Functions for caching -----------------------------------------------------------------------------


products_list = []
couriers_list = []
orders_list = []

def saving_product_list_cache():
    products_list.clear()
    connection = connection_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        products_dict = {"Product ID": str(row[0]), "Product Name": row[1], "Product Price": str(row[2])}
        products_list.append(products_dict)
    cursor.close()
    connection.close() 
                                       
                                         

def products_saving_to_csv():
    with open("product_cache.csv", "w", newline="") as products_cache_file:
        fc = csv.DictWriter(products_cache_file, fieldnames = products_list[0].keys())
        fc.writeheader()
        fc.writerows(products_list)
    products_list.clear()


def saving_order_list_cache():
    orders_list.clear()
    connection = connection_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    for row in rows:
        order_dict = {"order_id": str(row[0]), "customer_name": row[1], "customer_address": row[2], "customer_phone": row[3], "courier": str(row[4]), "order_status":row[5], "items": row[6]}
        orders_list.append(order_dict)
    cursor.close()
    connection.close() 
    
def orders_saving_to_csv():
    with open("orders_cache.csv", "w", newline="") as orders_cache_file:
        fc = csv.DictWriter(orders_cache_file, fieldnames = orders_list[0].keys())
        fc.writeheader()
        fc.writerows(orders_list)
    orders_list.clear()
   

def saving_courier_list_cache():
    couriers_list.clear()
    connection = connection_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM courier')
    rows = cursor.fetchall()
    for row in rows:
        couriers_dict = {"courier_id": str(row[0]), "courier_name": row[1], "courier_phone": row[2]}
        couriers_list.append(couriers_dict)
    cursor.close()
    connection.close() 
    
def courier_saving_to_csv():
    with open("courier_cache.csv", "w", newline="") as couriers_cache_file:
        fc = csv.DictWriter(couriers_cache_file, fieldnames = couriers_list[0].keys())
        fc.writeheader()
        fc.writerows(couriers_list)
    couriers_list.clear()

    
    
#------------------------------------------------mysql functions-----------------------------------------------------------------------------


# Load environment variables from .env file

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

def connection_to_db():
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    return connection

    
def connect_to_product():
    connection = connection_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT product_id, product_name, price FROM products')
    rows = cursor.fetchall()
    for row in rows:        
        product_dict = {"product_id":row[0], "product_name": row[1], "price":row[2]}
        print("\n")
        print("\u0332".join('PRODUCT'))
        for key,value in product_dict.items():
            print(key, ":",value)
    connection.commit()
    cursor.close()
    connection.close() 
    

def connect_to_courier():
    connection = connection_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT courier_id, courier_name, phone FROM courier')
    rows = cursor.fetchall()
    for row in rows:        
        courier_dict = {"courier_id":row[0], "courier_name": row[1], "phone":row[2]}
        print("\n")
        print("\u0332".join('COURIER'))
        for key,value in courier_dict.items():
            print(key, ":",value)
    connection.commit()
    cursor.close()
    connection.close() 
    
def connect_to_orders():
    connection = connection_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, courier, order_status, items FROM orders')
    rows = cursor.fetchall()
    for row in rows:        
        order_dict = {"order_id":row[0], "customer_name": row[1], "customer_address":row[2] , "customer_phone":row[3],"courier": row[4], "order_status":row[5],"items":row[6] }
        print("\n")
        print("\u0332".join('ORDER'))
        for key,value in order_dict.items():
            print(key, ":",value)
    connection.commit()
    cursor.close()
    connection.close() 
    




#-----------------------------------------Product Functions-------------------------------------------------------------------------------


def print_product_menu():
    product_menu= menu_optimized("Product")
    if product_menu==0:
        print_main_menu()
    elif product_menu ==1:
        connect_to_product()
    elif product_menu==2:
        create_new_product()
    elif product_menu==3:
        update_product()
    elif product_menu ==4:
        delete_product()
           
            
def create_new_product():
    connection = connection_to_db()
    cursor = connection.cursor()    
    new_product_name = get_new_name("Product")
    new_product_price = get_price_of_product(input)
    sql = 'INSERT INTO products(product_name,price)  VALUES (%s, %s)'
    val =(new_product_name,new_product_price)
    cursor.execute(sql,val)
    new_dictionary ={"product_name":new_product_name, "price":new_product_price}
    print("This is your new Product",new_dictionary) #append this to global list and then print the list
    print("This is the new list of Products from the database")
    connection.commit()
    cursor.close()
    connection.close() 
    connect_to_product()
    saving_product_list_cache()
    products_saving_to_csv()
    

def update_product():
    connection = connection_to_db()
    cursor = connection.cursor()   
    connect_to_product() 
    select_id = get_id("Product", "Update")
    if select_id == 0:
        print_main_menu()
    elif select_id > 0:
        sql ='SELECT product_id FROM products WHERE product_id = %s'
        val =(select_id)
        cursor.execute(sql,val)      
        rows = cursor.fetchall()
        for row in rows: 
            new_product_name =input("Please enter the new name or space to skip: ")
            new_product_price= input("Please enter the new price of this product or skip to pass: ")
            if new_product_name =="":
                continue 
            else:
                sql_update_name = 'UPDATE products SET product_name = %s WHERE product_id = %s'
                val_update_name = (new_product_name, select_id)
                cursor.execute(sql_update_name,val_update_name)
                
            if new_product_price =="":
                continue               
            else:
                new_product_price = float(new_product_price)
                sql_update_price = 'UPDATE products SET price = %s WHERE product_id = %s'
                val_update_price = (new_product_price, select_id)
                cursor.execute(sql_update_price,val_update_price)
            
        print("This is the new list of Products from the database")
        connection.commit()
        cursor.close()
        connection.close() 
        connect_to_product()    
        saving_product_list_cache()
        products_saving_to_csv()
    


def delete_product():
    connection = connection_to_db()
    cursor = connection.cursor()   
    connect_to_product() 
    select_id = get_id("Product","Delete")
    if select_id == 0:
        print_main_menu()
    elif select_id >0:  
    #if user id exist inside then carry out function/ else error message doesn't exist
        print("This is your selected numner", select_id)
        sql = 'DELETE FROM products WHERE product_id = %s'
        val =(select_id)
        cursor.execute(sql,val)
        print("This is the new list of Products from the database")
        connection.commit()
        cursor.close()
        connection.close() 
        connect_to_product()
        saving_product_list_cache()
        products_saving_to_csv()
    
                      
    
    
#---------------------------------------------- Courier functions--------------------------------------------------------------------------

def print_courier_menu():
    courier_menu = menu_optimized("Courier")
    if courier_menu == 0:
        print_main_menu()
    elif courier_menu==1:
        connect_to_courier()
    elif courier_menu==2:
        create_new_courier()
    elif courier_menu==3:
        update_courier()
    elif courier_menu ==4:
        delete_courier()
    
    

   
def create_new_courier():
    connection = connection_to_db()
    cursor = connection.cursor()    
    new_courier_name = get_new_name("Courier")
    new_courier_phone = get_phone_number("Courier")
    sql = 'INSERT INTO courier(courier_name,phone)  VALUES (%s, %s)'
    val =(new_courier_name,new_courier_phone)
    cursor.execute(sql,val)
    new_dictionary ={"courier_name":new_courier_name, "phone":new_courier_phone}
    print("This is your new Courier",new_dictionary) #append this to global list and then print the list
    print("This is the new list of Couriers from the database")
    connection.commit()
    cursor.close()
    connection.close() 
    connect_to_courier()
    saving_courier_list_cache()
    courier_saving_to_csv()
   
    
    
def update_courier():
    connection = connection_to_db()
    cursor = connection.cursor()   
    connect_to_courier() 
    select_id = get_id("Couriers", "Update")
    if select_id == 0:
        print_main_menu()
    elif select_id > 0:
        sql ='SELECT courier_id FROM courier WHERE courier_id = %s'
        val =(select_id)
        cursor.execute(sql,val)      
        rows = cursor.fetchall()
        for row in rows: 
            new_courier_name =input("Please enter the new name or space to skip: ")
            new_courier_phone= input("Please enter the new phone number or the courier or skip to pass: ")
            if new_courier_name =="":
                continue 
            else:
                sql_update_name = 'UPDATE courier SET courier_name = %s WHERE courier_id = %s'
                val_update_name = (new_courier_name, select_id)
                cursor.execute(sql_update_name,val_update_name)
                
            if new_courier_phone =="":
                continue               
            else:
                new_courier_phone = new_courier_phone
                sql_update_phone = 'UPDATE courier SET price = %s WHERE courier_id = %s'
                val_update_phone = (new_courier_phone, select_id)
                cursor.execute(sql_update_phone,val_update_phone)
            
        print("This is the new list of Couriers from the database")
        connection.commit()
        cursor.close()
        connection.close() 
        connect_to_product()    
        saving_courier_list_cache()
        courier_saving_to_csv()
    
    

def delete_courier():
    connection = connection_to_db()
    cursor = connection.cursor()   
    connect_to_courier() 
    select_id = get_id("Courier","Delete")
    if select_id == 0:
        print_main_menu()
    elif select_id >0:  
    #if user id exist inside then carry out function/ else error message doesn't exist
        print("This is your selected numner", select_id)
        sql = 'DELETE FROM courier WHERE courier_id = %s'
        val =(select_id)
        cursor.execute(sql,val)
        print("This is the new list of Courier from the database")
        connection.commit()
        cursor.close()
        connection.close() 
        connect_to_courier()
        saving_courier_list_cache()
        courier_saving_to_csv()   
    
    

    
    
    
#--------------------------------ORDER MENU-----------------------------------------------------------------

def print_order_menu():
    order_menu= menu_optimized("Order")
    if order_menu == 0:
        print_main_menu()
    elif order_menu ==1:
        connect_to_orders()
    elif order_menu ==2:
        create_new_order()
    elif order_menu==3:
        update_order_status()
    elif order_menu ==4:
        delete_order()
        


def create_new_order():
    connection = connection_to_db()
    cursor = connection.cursor()
    new_name = get_new_name("Customer")
    new_address = get_new_address()
    new_phone = get_phone_number("Customer")
    courier_id= select_id_from_courier_list()
    default_status = "Preparing"
    product_list=convert_product_list_int()   
    sql = 'INSERT INTO orders(customer_name,customer_address,customer_phone,courier,order_status,items)VALUES (%s,%s,%s,%s,%s,%s)'
    val =(new_name,new_address,new_phone,courier_id,default_status,product_list)  
    cursor.execute(sql,val)
    connection.commit()
    cursor.close()
    connection.close() 
    print("Your new orders are: ")
    connect_to_orders()
    saving_order_list_cache()
    orders_saving_to_csv()


def update_order_status():
    connection = connection_to_db()
    cursor = connection.cursor()  
    connect_to_orders()
    select_id = get_id("Order","update the status for") 
    chosen_status = select_order_status()
    print("This is your chosen:  ", chosen_status)
    sql = 'UPDATE orders SET order_status = %s WHERE order_id = %s'
    val = (chosen_status, select_id)
    cursor.execute(sql,val)   
    connection.commit()
    cursor.close()
    connection.close() 
    connect_to_orders()    
    saving_order_list_cache()
    orders_saving_to_csv()
    


def print_order_status_options():
    status_list=["Preparing", "Out for delivery", "Cancelled", "Delivered"]
    print("These are your status options: ")
    for status in status_list:
        print(status)
    return status_list


def select_order_status():
    selected = print_order_status_options()
    while True:
        
        selected_status = input("Please select your chosen status: ")
        x= 0
        for status in selected:
            if selected_status == status:
                chosen_status = status
                x+=1
                break
            else:
                continue
        if x==1:
            print("This is your chosen status: ", chosen_status)
            return chosen_status   
            break       
        else: 
            print("This is an error, you have not selected from your status options")
            continue
            
    
    
def delete_order():
    connection = connection_to_db()
    cursor = connection.cursor()   
    connect_to_orders() 
    select_id = get_id("Courier","Delete")
    if select_id == 0:
        print_main_menu()
    elif select_id >0:  
    #if user id exist inside then carry out function/ else error message doesn't exist
        print("This is your selected numner", select_id)
        sql = 'DELETE FROM orders WHERE order_id = %s'
        val =(select_id)
        cursor.execute(sql,val)
        print("This is the new list of Orders from the database")
        connection.commit()
        cursor.close()
        connection.close() 
        connect_to_orders()
        saving_order_list_cache()
        orders_saving_to_csv()
        
    

print_main_menu()    
connection_to_db()





        