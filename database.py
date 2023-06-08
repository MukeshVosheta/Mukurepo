import mysql.connector
from mysql.connector import Error
import os
import pandas as pd
import time

def mssg(msg):
    print("* "*15," ",msg," ","* "*15)

# ______________________________________screen clear funstion____________________________________________________________

def clears():
        os.system('clear')



try:
    #con = mysql.connector.connect(host='localhost',user='dbuser',password='Squ@d123',database='BasicDB')
    con = mysql.connector.connect(host='localhost',user='muku',password='25456',database='findshop')
    cursor = con.cursor()
    if con.is_connected:
        print('Connection successfully established')

        try:
#_______________________Creating shop registration_______________________________________

            create_q='''create table shop_register
            (shop_id int(11) not null auto_increment primary key,
            shop_firstname varchar(25) not null,
            shop_lastname varchar(25) not null,
            shop_name varchar(50) not null,
            shop_add varchar(255) not null,
            shop_pincode int(6) not null,
            shop_contact bigint not null,
            shop_email varchar(45) not null,
            shop_pass varchar(25) not null,
            shop_register_time datetime not null)'''
            cursor.execute(create_q)
            con.commit()
        except Error as prm:
            mssg(f"Connecting to The server...{prm}")

#_______________________Creating shop products registration_______________________________________
        
        try:
            create_q='''create table product_register
            (product_id int auto_increment not null primary key,
            product_name varchar(25) not null,
            product_price float(10,2) not null,
            product_detail tinytext not null,
            product_manufacture varchar(30),
            product_quantity int not null default '0',
            shop_id int(11),
            foreign key(shop_id) references shop_register(shop_id))'''

            cursor.execute(create_q)
            con.commit()

        except Error as prm:
            mssg(f'Connecting to the server {prm}')


#_______________________Creating Customer registration_______________________________________
        
        try:
            create_q='''create table customer_register
            (customer_id int auto_increment not null primary key,
            customer_firstname varchar(25) not null,
            customer_lastname varchar(25) not null,
            customer_add varchar(255) not null,
            customer_contact bigint not null,
            customer_email varchar(45) not null,
            customer_pass varchar(25) not null,
            customer_register_time datetime not null)'''

            cursor.execute(create_q)
            con.commit()
        except Error as prm:
            mssg(f'Connecting to the server {prm}')

#_______________________Creating Customer_order_registration_______________________________________
        
        try:
            create_q='''create table order_register
            (order_id int auto_increment not null primary key,
            customer_id int not null,
            product_id int not null,
            shop_id int not null,
            order_quantity int not null default '0',
            order_register_datetime datetime not null,
            order_bill float(10,2) not null,
            order_status varchar(10) default 'pending' not null,
            foreign key(customer_id) references customer_register(customer_id),
            foreign key(product_id) references product_register(product_id),
            foreign key(shop_id) references shop_register(shop_id)
            )'''

            cursor.execute(create_q)
            con.commit()
        except Error as prm:
            mssg(f'Connecting to the server {prm}')

#_______________________Creating search log_______________________________________
        
        try:
            create_q='''create table search_log
            (search_id int auto_increment not null primary key,
            product_name varchar(30) not null,
            search_pincode int(6),
            customer_id int not null,
            search_time datetime not null,
            foreign key(customer_id) references customer_register(customer_id))'''

            cursor.execute(create_q)
            con.commit()
        except Error as prm:
            mssg(f'Connecting to the server {prm}')

#_____________________Creating customer report______________________________________
        
        try:
            create_q='''create table customer_reports(cust_report_id int auto_increment not null primary key,
            cust_feed varchar(150) not null default "No Feed",
            shop_id int not null,
            customer_id int not null,
            cust_report_date_time datetime not null,
            foreign key(customer_id) references customer_register(customer_id),
            foreign key(shop_id) references shop_register(shop_id));'''

            cursor.execute(create_q)
            con.commit()
        except Error as prm:
            mssg(f'Connecting to the server {prm}')


#_____________________Creating Shop report______________________________________
        
        try:
            create_q='''create table shop_reports(shop_report_id int auto_increment not null primary key,
            shop_feed varchar(150) not null default "No Feed",
            shop_id int not null,
            customer_id int not null,
            shop_report_date_time datetime not null,
            foreign key(customer_id) references customer_register(customer_id),
            foreign key(shop_id) references shop_register(shop_id));'''

            cursor.execute(create_q)
            con.commit()    
        except Error as prm:
            mssg(f'Connecting to the server {prm}')




    
except Error as prm:
    mssg(f'Unable establish SQL server connection{prm}')

finally:
    time.sleep(1)
    clears()
    mssg('Connected')
    time.sleep(1)
    clears()

#
# 
# 
# 
# 
#___________________________________Search product function__________________________________

def search_all(search_name):

    print('\n\n')
    sl=f"select product_name,product_detail,product_quantity,shop_name,shop_add,shop_pincode from product_register inner join shop_register on product_register.shop_id = shop_register.shop_id where product_name ='{search_name}';"
    
    cursor.execute(sl)
    user=cursor.fetchall()
    
    rec=pd.DataFrame(user,columns=['product name',' product detail',' product quantity',' shop name',' shop add',' shop pincode'])
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.width',None)
    
    if rec.empty == True:
        print(f' there is no product as {search_name}')

    else:
        print(rec.to_string(index=False))
    # for i in user:
    #     for j in i :
    #            print(j,end="-----")
    #     print()

#
#
#
#
#_____________________________________Search by area________________________________________

def search_byarea(search_name,search_pin):

    print('\n\n')
    sl=f"select product_name,product_detail,product_quantity,shop_name,shop_add,shop_pincode from product_register inner join shop_register on product_register.shop_id = shop_register.shop_id where product_name ='{search_name}' and shop_pincode ='{search_pin}';"
    
    cursor.execute(sl)
    user=cursor.fetchall()
    
    rec=pd.DataFrame(user,columns=['product name',' product detail',' product quantity',' shop name',' shop add',' shop pincode'])
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.width',None)
    
    if rec.empty == True:
        print(f' there is no product as {search_name}')
    else:
        print(rec.to_string(index=False))


#
# 
# 
# 
# 
#_____________________________________Shop insert function___________________________________ 

def shop_reg(rd):
    
    try:
        insert_r="insert into shop_register(shop_firstname,shop_lastname,shop_name,shop_add,shop_pincode,shop_contact,shop_email,shop_pass,shop_register_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(rd.shop_firstname,rd.shop_lastname,rd.shop_name,rd.shop_add,rd.shop_pincode,rd.shop_contact,rd.shop_email,rd.shop_pass,rd.shop_register_time)
        cursor.execute(insert_r,data)
        con.commit()
        mssg(f'Successfully {rd.shop_name} Registered')

    except Error as er:
        mssg(er)

#
# 
# 
# 
# 
#_____________________________________customer insert function___________________________________ 

def customer_reg(rd):
    
    try:
        insert_r="insert into customer_register(customer_firstname,customer_lastname,customer_add,customer_contact,customer_email,customer_pass,customer_register_time) values(%s,%s,%s,%s,%s,%s,%s)"
        data=(rd.customer_firstname,rd.customer_lastname,rd.customer_add,rd.customer_contact,rd.customer_email,rd.customer_pass,rd.customer_register_time)
        cursor.execute(insert_r,data)
        con.commit()
        mssg(f'Successfully {rd.customer_firstname} Registered')

    except Error as er:
        mssg(er)



#
#
#
#
#
#____________________________________Product insert Function___________________________________

def product_reg(rad):
    try:
        insert_p='''insert into product_register 
                (product_name,product_price,product_detail,product_manufacture,product_quantity,shop_id)select %s,%s,%s,%s,%s,shop_id from shop_register where shop_email = %s'''
        data = rad.product_name,rad.product_price,rad.product_detail,rad.product_manufacture,rad.product_quantity,rad.shop_email
        cursor.execute(insert_p,data)
        con.commit()
        mssg(f'{rad.product_name} Added')

    except Error as er:
        mssg(er)


#
#
#
#
#
#________________________________________Order product Function____________________________

def product_order(customer_email,pro_id,pro_quantity,order_register_datetime):
    q = f'select product_quantity from product_register where product_id = "{pro_id}"'
    cursor.execute(q)
    pq = cursor.fetchone()
    try:
        for i in pq:
            pq = i
    except:
        return mssg(f'There is no product ID as {pro_id}')
    
    if pq > 0 and pro_quantity <= pq:

        try:
            nq =f'insert into order_register (customer_id,product_id,shop_id,order_quantity,order_register_datetime,order_bill) select (select customer_id from customer_register where customer_email = "{customer_email}") as customer_id,{pro_id},(select shop_id from product_register where product_id ={pro_id}),{pro_quantity},"{order_register_datetime}",({pro_quantity}* product_price) from product_register where product_id = "{pro_id}"'
             #insert into order_register (customer_id,product_id,order_quantity,order_register_datetime,order_bill) select (select customer_id from customer_register where customer_email = "abc@gmail.com") as customer_id,4,5,"2023-05-10 21:33:31",5*product_price from product_register where product_id = "4";
            cursor.execute(nq)
            con.commit()
        except Error as er:
            mssg(er)

        try:
            ns =f'update product_register set product_quantity = product_quantity - {pro_quantity} where product_id = {pro_id};'
            cursor.execute(ns)
            con.commit()
            mssg(f'Order confirmed')
        except Error as er:
            mssg(er)
            
    elif pq == 0 and pro_quantity >= pq:
        mssg(f'Invalid quantity {pro_quantity}')
    else:
        mssg(f'Invalid Product ID {pro_id}')


#
#
#
#
#
#_______________________________________Shop email check_______________________________________________

def check_shop_email(shop_email):
    check_q=f'select shop_email from shop_register where shop_email = "{shop_email}"'
    cursor.execute(check_q)
    email=cursor.fetchone()
    try:
        for i in email:
            email=i
    except:
        return None
    if email == shop_email:
        return f'{shop_email} alerady exists'
    elif email != shop_email:
        return None



#
#
#
#
#
#_______________________________________customer email check_______________________________________________

def check_customer_email(customer_email):
    check_q=f'select customer_email from customer_register where customer_email = "{customer_email}"'
    cursor.execute(check_q)
    email=cursor.fetchone()
    try:
        for i in email:
            email=i
    except:
        return None
    
    if email == customer_email:
        return f'{customer_email} alerady exists'
    
    elif email != customer_email:
        return None



#
#
#
#
#
#_____________________________________shop_login______________________________________

def shop_login(shop_email,shop_pass):
    check_q_email=f'select shop_email from shop_register where shop_email = "{shop_email}"'
    cursor.execute(check_q_email)
    email = cursor.fetchone()
    try :
        for i in email:
            email = i
        if shop_email == email:
            check_q_pass=f'select shop_pass from shop_register where shop_email = "{shop_email}"'
            cursor.execute(check_q_pass)
            email_pass=cursor.fetchone()
            for i in email_pass:
                email_pass = i
            if shop_pass == email_pass:
                return True
            else:
                return  mssg('Wrong password')
        
    except:
        return mssg('Email not registered')
    
    
    
#
#
#
#
#
#_____________________________________customer_login______________________________________

def customer_login(customer_email,customer_pass):
    check_q_email=f'select customer_email from customer_register where customer_email = "{customer_email}"'
    cursor.execute(check_q_email)
    email = cursor.fetchone()
    try :
        for i in email:
            email = i
        if customer_email == email:
            check_q_pass=f'select customer_pass from customer_register where customer_email = "{customer_email}"'
            cursor.execute(check_q_pass)
            email_pass=cursor.fetchone()
            for i in email_pass:
                email_pass = i
            if customer_pass == email_pass:
                return True
            else:
                return  mssg('Wrong password')
        
    except:
        return mssg('Email not registered')


#
#
#
#
#_______________________________customer get name_________________________________________

def customer_name(customer_email):
    check_name=f'select customer_firstname from customer_register where customer_email = "{customer_email}"'
    cursor.execute(check_name)
    name = cursor.fetchone()
    try :
        for i in name:
            name = i
            return name
    except:
        return None


#
#
#
#
#____________________________________________shop_products_________________________________________________

def show_shop_prdoucts(shop_email):
    try:
        sl=f"select product_id,product_name,product_price,product_detail,product_manufacture,product_quantity from product_register where shop_id = (select shop_id from shop_register where shop_email ='{shop_email}' );"
        cursor.execute(sl)
        user=cursor.fetchall()
        '''
        for i in user:
            for j in i :
                print(j,end="-----")
            print()
         '''   
        rec =pd.DataFrame(user,columns=[' product id',' product name',' product price',' product detail',' product manufacture',' product quantity'])
        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.width',None)

        if rec.empty == True:
            print(f'There is no Product')
        else:
            print(rec.to_string(index=False))
    
    
    except Error as e:
        print("Error : ",e)



#
#
#
#
#_______________________________________show customer booked orders_________________________________________________

def booked_orders(customer_email):
    try:
        sl=f"select order_id,customer_firstname,customer_add,customer_contact,product_name,order_quantity,product_price,shop_name,shop_add,order_bill,order_status from order_register inner join customer_register on order_register.customer_id = customer_register.customer_id inner join product_register on order_register.product_id = product_register.product_id inner join shop_register on order_register.shop_id=shop_register.shop_id where order_register.customer_id = (select customer_id from customer_register where customer_email='{customer_email}')"
        cursor.execute(sl)
        user=cursor.fetchall()

        rec =pd.DataFrame(user,columns=['Order ID','Customer Name','Customer Address','Customer Contact','Product Name','Order Quantity','Product Price','Shop Name','Shop Address','Order Bill','order_status'])
        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.width',None)

        if rec.empty == True:
            print(f'There is No Orders\n')
        else:
            print(rec.to_string(index=False))
    
    
    except Error as e:
        print("Error : ",e)

#
#
#
#
#_________________________________________________cancel order_____________________________________________

def cancel_order(order_id,customer_email):
    s=f"select order_id from order_register where customer_id=(select customer_id from customer_register where customer_email='{customer_email}') and order_id ='{order_id}';"
    cursor.execute(s)
    r = cursor.fetchone()
    try:
        for i in r:
            r=i
        if r:
            try:
                sl=f"update product_register set product_quantity = product_quantity+(select order_quantity from order_register where order_id = {order_id}) where product_id = (select product_id from order_register where order_id={order_id});"
                cursor.execute(sl)
                con.commit()
                mssg ('Quantity send back')
            except Error as er:
                mssg(er)

            try:
                sl=f"delete from order_register where customer_id=(select customer_id from customer_register where customer_email='{customer_email}') and order_id ='{order_id}';"
                cursor.execute(sl)
                con.commit()
                mssg ('Order successfully Canceled')
            except Error as er:
                mssg(er)
    except:
        return mssg('Wrong Product ID')




#
#
#
#
#___________________________________________shop order list_________________________________________

def show_shop_orders(shop_email):
    try:
        sl=f"select order_id,customer_firstname,customer_add,customer_contact,product_name,order_quantity,product_price,order_bill,order_status from order_register as o inner join customer_register as c on o.customer_id = c.customer_id inner join product_register as p on o.product_id = p.product_id inner join shop_register as s on o.shop_id = s.shop_id where o.shop_id = (select shop_id from shop_register where shop_email = '{shop_email}')"
        cursor.execute(sl)
        user=cursor.fetchall()

        rec =pd.DataFrame(user,columns=['Order ID',' Customer Name',' Customer Address',' Customer Contact',' Product Name',' Order Quantity',' Product Price',' Order Bill','Order Status'])
        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.width',None)

        if rec.empty == True:
            print(f'There is No Orders yet\n')
        else:
            print(rec.to_string(index=False))
    
    
    except Error as e:
        print("Error : ",e)



#
#
#
#
#____________________________order status change___________________________________
def order_status(order_id,order_status,email):

    sl=f"select order_id from order_register where shop_id = (select shop_id from shop_register where shop_email='{email}') and order_id={order_id}"
    cursor.execute(sl)
    dt =cursor.fetchone()
    try:
        dt =dt[0]
        try:
            sl=f"update order_register set order_status = '{order_status}' where order_id={order_id} and shop_id=(select shop_id from shop_register where shop_email='{email}')"
            cursor.execute(sl)
            con.commit()
            mssg(f'Order placed successfully')
            
        except Error as er:
            mssg(er)
    except:
        return mssg('Wrong Order ID')




#
#
#
#
#______________________product modify_________________________________

def product_detail_modify(product_data,new_detail,shop_email,product_id):
    try:
        sl=f"update product_register set {product_data} = '{new_detail}' where shop_id=(select shop_id from shop_register where shop_email='{shop_email}') and product_id ='{product_id}'"
        cursor.execute(sl)
        con.commit()
        mssg(f'successfully modified to {new_detail}')
        
    except Error as er:
        mssg(er)
#
#
#
#
#______________________product delete_________________________________

def delete_product(shop_email,delete_product_id):
    try:
        sl=f"delete from product_register where shop_id=(select shop_id from shop_register where shop_email='{shop_email}') and product_id ='{delete_product_id}'"
        cursor.execute(sl)
        con.commit()
        mssg(f'{delete_product_id} successfully deleted')
        
    except Error as er:
        mssg(er)

#
#
#
#
#_________________________customer search by area__________________________________

def customer_search_byarea(search_name,search_pin):

    print('\n\n')
    sl=f"select product_name,product_detail,product_price,product_manufacture,product_quantity,shop_name,shop_add,shop_pincode,shop_contact from product_register inner join shop_register on product_register.shop_id = shop_register.shop_id where product_name ='{search_name}' and shop_pincode ='{search_pin}';"
    
    cursor.execute(sl)
    user=cursor.fetchall()
    
    rec=pd.DataFrame(user,columns=[' product name',' product detail',' product quantity',' product price',' product manufacture',' shop name',' shop address',' shop pincode',' shop contact'])
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.width',None)
    
    if rec.empty == True:
        print(f' there is no product as {search_name}')
    else:
        print(rec.to_string(index=False))


#
#
#
#
#___________________________________customer Search product function__________________________________

def customer_search_all(search_name):

    print('\n\n')
    sl=f"select product_id,product_name,product_detail,product_price,product_manufacture,product_quantity,shop_name,shop_add,shop_pincode,shop_contact from product_register inner join shop_register on product_register.shop_id = shop_register.shop_id where product_name ='{search_name}';"
    
    cursor.execute(sl)
    user=cursor.fetchall()
    
    rec=pd.DataFrame(user,columns=[' product ID',' product name',' product detail',' product price',' product manufacture',' product Quantity',' shop name',' shop add',' shop pincode',' shop contact'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)
    
    if rec.empty == True:
        print(f' there is no product as {search_name}')
    else:
        print(rec.to_string(index=False))


#
#
#
#
#___________________________________Search log function__________________________________

def search_product_log(product_name,search_time,customer_email):
    try:
        insert_p=f'''insert into search_log(product_name,customer_id,search_time) select '{product_name}',(select customer_id from customer_register where customer_email = '{customer_email}') as customer_id,'{search_time}';'''
        cursor.execute(insert_p)
        con.commit()

    except Error as er:
        mssg(er)


#
#
#
#
#___________________________________Search log with pincode function__________________________________

def pinsearch_product_log(product_name,search_time,search_pincode,customer_email):
    try:
        insert_p=f'''insert into search_log(product_name,search_pincode,customer_id,search_time) select '{product_name}','{search_pincode}',(select customer_id from customer_register where customer_email = '{customer_email}') as customer_id,'{search_time}';'''
        cursor.execute(insert_p)
        con.commit()

    except Error as er:
        mssg(er)



#
#
#
#
#_____________________________________shop search log show_______________________________________

def show_search_log():
    print('\n\n')
    sl="select product_name,customer_firstname,customer_contact,search_pincode,search_time from search_log inner join customer_register on customer_register.customer_id = search_log.customer_id;"
    
    cursor.execute(sl)
    user=cursor.fetchall()
    
    rec=pd.DataFrame(user,columns=[' product name','customer name','customer contact','search pincode','search time'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)
    
    if rec.empty == True:
        print('         there is no searched log right now')
    else:
        print(rec.to_string(index=False))
    

#
#
#
#
#_____________________________________most_search_function________________________________
def most_searched():
    print('\n\n')
    sl='select product_name,(count(product_name)) as search_count from search_log group by product_name having count(product_name)>1'
    cursor.execute(sl)
    data=cursor.fetchall()

    rec=pd.DataFrame(data,columns=[' Product Name',' Search Count'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)
    
    if rec.empty == True:
        print(' ')
    else:
        print(rec.to_string(index=False))
    
    


#
#
#
#
#_____________________________________customer Reports function______________________________

def customer_report(customer_email,shop_id,feed,report_datetime):
    sl=f"select shop_id from shop_register where shop_id = {shop_id}"
    cursor.execute(sl)
    dt =cursor.fetchone()
    try:
        dt =dt[0]
        try:
            iq=f'insert into customer_reports(cust_feed,shop_id,customer_id,cust_report_date_time) select "{feed}","{shop_id}",(select customer_id from customer_register where customer_email="{customer_email}")as customer_id,"{report_datetime}"'
            cursor.execute(iq)
            con.commit()
            mssg('Report submitted')

        except Error as er:
            mssg(er)
    except:
        mssg("Wrong Shop ID")




#
#
#
#
#_____________________________________shop Reports function______________________________

def shop_report(shop_email,customer_id,feed,report_datetime):
    sl=f"select customer_id from customer_register where customer_id = {customer_id}"
    cursor.execute(sl)
    dt =cursor.fetchone()
    try:
        dt =dt[0]
        try:
            iq=f'insert into shop_reports(shop_feed,shop_id,customer_id,shop_report_date_time) select "{feed}",(select shop_id from shop_register where shop_email="{shop_email}")as shop_id,"{customer_id}","{report_datetime}"'
            cursor.execute(iq)
            con.commit()
            mssg('Report submitted')

        except Error as er:
            mssg(er)
    except:
        mssg("Wrong Customer ID")




#
#                                    A D M I N   F U N C T I O N
#
#                                       
#_____________________________________Admin Show Reports________________________________________

def show_reports():
    
    #--------------Most Reported cutomers--------------
    print('\n\n')
    print('--------------Most Reported cutomers--------------\n')
    sl='select shop_reports.customer_id,customer_firstname,customer_contact,count(shop_reports.customer_id) from shop_reports inner join customer_register on shop_reports.customer_id=customer_register.customer_id group by shop_reports.customer_id having count(shop_reports.customer_id)>1;'
    cursor.execute(sl)
    data=cursor.fetchall()

    rec=pd.DataFrame(data,columns=['customer id','customer name','customer_contact','Reports Count'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)

    if rec.empty == True:
        print('There is no reports at the moment')
    else:
        print(rec.to_string(index=False))
    
    #
    #
    #
    #--------------Most Reported shops--------------
    print('\n\n')
    print('--------------Most Reported shops--------------\n')
    sl='select customer_reports.shop_id,shop_name,shop_contact,count(customer_reports.shop_id) from customer_reports inner join shop_register on customer_reports.shop_id=shop_register.shop_id group by customer_reports.shop_id having count(customer_reports.shop_id)>1;'
    cursor.execute(sl)
    data=cursor.fetchall()

    rec=pd.DataFrame(data,columns=['shop id','shop name','shop contact','Reports Count'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)

    if rec.empty == True:
        print('There is no reports at the moment')
    else:
        print(rec.to_string(index=False))
    #
    #
    #
    #: : :Reports on cutomers from Shops: : :
    print('\n\n')
    print(': : :Reports on cutomers from Shops: : :\n')
    sl='select shop_report_id,shop_reports.shop_id,shop_feed,shop_name,shop_contact,shop_reports.customer_id,customer_firstname,customer_contact,customer_add,shop_report_date_time from shop_reports join shop_register on shop_reports.shop_id = shop_register.shop_id inner join customer_register on shop_reports.customer_id = customer_register.customer_id;'
    cursor.execute(sl)
    data=cursor.fetchall()

    rec=pd.DataFrame(data,columns=['shop report id','shop id','shop feed','shop name','shop contact','customer id','customer firstname','customer contact','customer add','report date time'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)

    if rec.empty == True:
        print(' ')
    else:
        print(rec.to_string(index=False))
    #
    #
    #
    #: : :Reports on Shops from Customers: : :
    print('\n\n')
    print(': : :Reports on Shops from Customers: : :\n')
    sln='select cust_report_id,customer_reports.customer_id,cust_feed,customer_firstname,customer_contact,customer_reports.shop_id,shop_name,shop_contact,shop_add,cust_report_date_time from customer_reports join shop_register on customer_reports.shop_id = shop_register.shop_id inner join customer_register on customer_reports.customer_id = customer_register.customer_id;'
    cursor.execute(sln)
    data=cursor.fetchall()

    reco=pd.DataFrame(data,columns=['cust report id','customer ID','customer feed','customer name','customer contact','shop id','shop name','shop contact','shop address','report date time'])
    pd.set_option('display.colheader_justify','center')
    pd.set_option('display.width',None)
    
    if reco.empty == True:
        print('There is no reports at the moment')
    else:
        print(reco.to_string(index=False))


#
#
#
#____________________________________admin shop registers________________________________________

def show_shops_admin():
    try:
        sl="select*from shop_register;"
        cursor.execute(sl)
        user=cursor.fetchall()

        rec =pd.DataFrame(user,columns=['shop id','shop firstname','shop lastname','shop name','shop add','shop pincode','shop contact','shop email','shop pass','register time'])
        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.width',None)

        if rec.empty == True:
            print('Currently there is no shops are registered at the moment.\n')
        else:
            print(rec.to_string(index=False))
    
    
    except Error as e:
        print("Error : ",e)


#
#
#
#____________________________________admin customer registers________________________________________

def show_customer_admin():
    try:
        sl="select*from customer_register;"
        cursor.execute(sl)
        user=cursor.fetchall()

        rec =pd.DataFrame(user,columns=['customer id','customer firstname','customer lastname','customer add','customer contact','customer email','customer pass','customer register time'])
        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.width',None)

        if rec.empty == True:
            print('Currently there is no shops are registered at the moment.\n')
        else:
            print(rec.to_string(index=False))
    
    
    except Error as e:
        print("Error : ",e)


#
#
#
#
#______________________________________admin shop delete____________________________________________
def delete_shop(shop_id):
    try:
        sln=f"select shop_id from shop_register where shop_id='{shop_id}'"
        cursor.execute(sln)
        rec=cursor.fetchone()
        try:
            rec=rec[0]
        except:
            rec=None
        if rec:
            sl=f"SET FOREIGN_KEY_CHECKS=0;"
            cursor.execute(sl)
            sl=f"delete from shop_register where shop_id='{shop_id}';"
            cursor.execute(sl)
            sl=f"delete from product_register where shop_id='{shop_id}';"
            cursor.execute(sl)
            sl=f"SET FOREIGN_KEY_CHECKS=1;"
            cursor.execute(sl)
            
            con.commit()
            mssg(f'ID number {shop_id} successfully deleted')
        else:
            mssg(f'There is no Shop with shop ID : {shop_id}')
        
    except Error as er:
        mssg(er)
    

#
#
#
#
#______________________________________admin shop delete____________________________________________
def delete_customer(customer_id):
    try:
        sln=f"select customer_id from customer_register where customer_id='{customer_id}'"
        cursor.execute(sln)
        rec=cursor.fetchone()
        try:
            rec=rec[0]
        except:
            rec=None
        if rec:
            sl=f"SET FOREIGN_KEY_CHECKS=0;"
            cursor.execute(sl)
            sl=f"delete from customer_register where customer_id='{customer_id}';"
            cursor.execute(sl)
            sl=f"delete from order_register where customer_id='{customer_id}';"
            cursor.execute(sl)
            sl=f"SET FOREIGN_KEY_CHECKS=1;"
            cursor.execute(sl)

            con.commit()
            mssg(f'ID number {customer_id} successfully deleted')
        else:
            mssg(f'There is no customer with customer ID : {customer_id}')
        
    except Error as er:
        mssg(er)
    

#
#
#
#
#________________________________________sample products__________________________________________
def sample_products():
    sq='select product_name,product_quantity,shop_name,shop_pincode from product_register join shop_register on product_register.shop_id=shop_register.shop_id limit 5'
    cursor.execute(sq)
    user=cursor.fetchall()
    
    rec=pd.DataFrame(user,columns=['Product Name','product Quantity','Shop Name','Pincode'])
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.width',None)
    
    if rec.empty == True:
        print(f'No products')

    else:
        print("~~~~~Recommend Products~~~~~\n")
        print(rec.to_string(index=False),"\n")




#
#
#
#
#________________________________________book order product show_______________________________________

def product_order_show(product_id,quantity):
    try:
        sq=f'select product_name,({quantity}) as product_quantity,product_price,(product_price*{quantity}) as total_bill from product_register where product_id = {product_id}'
        cursor.execute(sq)
        user=cursor.fetchall()
        
        rec=pd.DataFrame(user,columns=['Product Name','product Quantity','Product price','Total Bill'])
        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.width',None)
        
        if rec.empty == True:
            print(f'Wrong Product ID')

        else:
            print()
            print(rec.to_string(index=False),"\n")
    except:
        return mssg('Invalid Details were given')













