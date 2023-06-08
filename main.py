from model import shop_register,product_register,customer_register,admin
import database as db
import allvalidation

from datetime import datetime
import time
import maskpass

# ______________________________________Message function _________________________________________________________________

def mssg(msg):
    print("- "*15," ",msg," ","- "*15,"\n")



#start here


mssg("Welcome To NearMart")


while True:
    mssg("HOME")

    print('1.Search\n2.Register\n3.Login\n4.exit\n\n')
    ch = input("Enter your option Number:")
    print()
    
    
    # ___________________Search input page done here__________________________________________________

    if ch=='1':
        mssg('Search Page')
        db.sample_products()
        search_name = input('Enter product name :')
        search_pin = input('Enter area pincode (You can skip picode hit Enter) :')
        if search_name and search_pin == '':
            db.search_all(search_name)
            print('\n\n')
            time.sleep(2)
            print(''' .----------------------------------------------------------------.
||								  ||
||	   For more details login first	                          ||
||	   after login you can order your product		  ||
||								  ||
 '----------------------------------------------------------------'  ''')
        elif search_name and search_pin:
            db.search_byarea(search_name,search_pin)
            print('\n\n')
        else:
            mssg('Enter producct name to search')


    #
    #
    #
    #
    # ___________________________Shop register and User register page done here________________________________
   
    elif ch=='2':
        mssg("registration page")
        print('1.Shop Register\n2.Custemor Register\n\n')
        cho = input('Enter option number :')

        if cho =='1':
            mssg('Shop Regitration Page')

            while True:
                shop_firstname = input('Enter Shop Owner First name :')
                if allvalidation.nameval(shop_firstname) == True:
                    break
                else:
                    mssg('Invalid Name must be in character')

            while True:      
                shop_lastname = input('Enter Shop Owner Last name :')
                if allvalidation.nameval(shop_lastname) == True:
                    break
                else:
                    mssg('Invalid Name must be in character')

            while True:
                shop_name = input('Enter Shop name :')
                if allvalidation.nameval(shop_name) == True:
                    break
                else:
                    mssg('Invalid Name must be in character')
            while True:
                shop_add = input('Enter Full address :')
                if allvalidation.addressval(shop_add) == True:
                    break

            while True:
                shop_pincode = input('Enter Area Pincode :')
                if allvalidation.pincval(shop_pincode) == True:
                    break
                else:
                    mssg('Invalid pincode')

            while True:
                shop_contact = input('Enter Contact number :')
                if allvalidation.conval(shop_contact) == True:
                    break
                else:
                    mssg('Invalid contact Number')
            
            while True:   
                shop_email = input('Enter email :')
                if allvalidation.emailval(shop_email) == True:
                    if db.check_shop_email(shop_email) == None:
                        break
                    else:
                        mssg(db.check_shop_email(shop_email))
                else:
                    mssg('Invalid Email addresss')
            
            while True:
                shop_pass = maskpass.askpass('Enter password :',mask="*")
                shop_pass2 = maskpass.askpass('Confirm password :',mask="*")
                print()
                
                if allvalidation.passval(shop_pass,shop_pass2) == True:
                    break
                else:
                    mssg('Password does not match')
 
            now = datetime.now()
            shop_register_time= str(now.strftime('%Y-%m-%d %H:%M:%S'))
                                            #2023-04-27 23:26:42

            rd = shop_register(shop_firstname,shop_lastname,shop_name,shop_add,shop_pincode,shop_contact,shop_email,shop_pass,shop_register_time)
            prom=input("To confirm press y :")
            if prom == "y":   
                db.shop_reg(rd) 
            else:
                db.mssg("Process Cancelled")         
        #
        #
        #
        #
        #
        #    ____________________________________ Custemer registration___________________________________
       
        elif cho =='2':
            mssg('Customer Regitration page')
            
            while True:
                customer_firstname = input('Enter customer First name :')
                if allvalidation.nameval(customer_firstname) == True:
                    break
                else:
                    db.mssg('Invalid Name must be in character')
            
            while True:
                customer_lastname = input('Enter customer Last name :')
                if allvalidation.nameval(customer_lastname) == True:
                    break
                else:
                    db.mssg('Invalid Name must be in character')
            
            while True:
                customer_add = input('Enter Address :')
                if allvalidation.addressval(customer_add) == True:
                    break
                else:
                    db.mssg('Invalid Address')

            while True:
                customer_contact = input('Enter contact number :')
                if allvalidation.conval(customer_contact) == True:
                    break
                else:
                    db.mssg('Invalid contact')
            
            while True:
                customer_email = input('Enter email address :')
                if allvalidation.emailval(customer_email) == True:
                    if db.check_customer_email(customer_email) == None:
                        break
                    else:
                        db.mssg('Invalid Email')
            while True:
                customer_pass = maskpass.askpass('Enter password :',mask="*")
                customer_pass1 = maskpass.askpass('Confirm password :',mask="*")

                if allvalidation.passval(customer_pass,customer_pass1) == True:
                    break
                else:
                    db.mssg('Password does not match')
 
            now = datetime.now()
            customer_register_time= str(now.strftime('%Y-%m-%d %H:%M:%S'))

            rd = customer_register(customer_firstname,customer_lastname,customer_add,customer_contact,customer_email,customer_pass,customer_register_time)
            prom=input("To confirm press y :")
            if prom == "y":   
                db.customer_reg(rd)
            else:
                db.mssg("Process Cancelled")
            print()
             
             

            
    
    # login page block 

    elif ch=='3':
        while True:
            mssg('Login page')
            print('1.Shop login\n2.Custemor login\n3.Admin Login\n4.back\n\n')
            cho =input('Enter Option Number :')
            if cho == '1':
                mssg('Shop Login Page')
                
# Shop Login and Features

                while True:
                    shop_email=input('Enter Shop Email Address :')
                    x = allvalidation.emailval(shop_email) 
                    if x == True:
                        break
                    else:
                        print()
                        db.mssg("Invalid Email")
                        print()
                shop_pass=maskpass.askpass('Enter password :',mask="*")
                loggin = db.shop_login(shop_email,shop_pass)
                print()


                if loggin == True:

                    mssg(f'{shop_email} successfully Loged In')

                    while loggin == True:
                        mssg('shop Inventory page')
                        print('1.Show Products\n2.Add Product\n3.Modify Product\n4.Delete Product\n5.Search History\n6.Orders\n7.change order status\n8.Report on Customer\n9.Log Out\n\n')
                        scho=input('Enter your option number :')
                        print()

                        if scho == '1':
                            mssg('Shop Products')
                            print('\n')
                            db.show_shop_prdoucts(shop_email)
                            print()
                            


                        elif scho =='2':
                            mssg('Add Product here')
                            product_name = input('Enter Product Name :')
                            while True:
                                product_price = input('Enter Product price :')
                                if allvalidation.priceval(product_price) == True:
                                    break

                            product_detail = input('Enter Product detail :')
                            product_manufacture = input('Enter Manufacturer name :')
                            while True:
                                product_quantity = input('Enter Product quantity :')
                                print()
                                if allvalidation.quantityval(product_quantity) == True:
                                    break

                            rad = product_register(product_name,product_price,product_detail,product_manufacture,product_quantity,shop_email)
                            prom=input("To add product press y :")
                            if prom == "y":   
                                db.product_reg(rad)
                            else:
                                db.mssg("Process Cancelled")
                            print()

                        elif scho =='3':
                            while True:
                                mssg('Modify Product')
                                print('\n')
                                db.show_shop_prdoucts(shop_email)
                                print()
                                print('1.Modify Name\n2.Modify Price\n3.Modify Detail\n4.Modify Menufacture\n5.Modify Quantity\n6.Exit\n\n')
                                choi=input('Enter your option :')

                                #___________________ product name modified here_________________________________
                                
                                if choi == '1':
                                    print('\n')
                                    product_data='product_name'
                                    new_name=input('Enter product New name :')
                                    product_id=input('Enter product ID number :')
                                    prom=input("To Modify product press y :")
                                    if prom == "y":   
                                        db.product_detail_modify(product_data,new_name,shop_email,product_id)
                                    else:
                                        db.mssg("Process Cancelled")
                                    print()

                                elif choi == '2':
                                    print('\n')
                                    product_data='product_price'
                                    new_price=input('Enter product New price :')
                                    product_id=input('Enter product ID number :')
                                    prom=input("To Modify product press y :")
                                    if prom == "y":   
                                        db.product_detail_modify(product_data,new_price,shop_email,product_id)
                                    else:
                                        db.mssg("Process Cancelled")
                                    print()
                                    

                                elif choi == '3':
                                    print('\n')
                                    product_data='product_detail'
                                    new_detail=input('Enter product New Detail :')
                                    product_id=input('Enter product ID number :')
                                    prom=input("To Modify product press y :")
                                    if prom == "y":   
                                        db.product_detail_modify(product_data,new_detail,shop_email,product_id)
                                    else:
                                        db.mssg("Process Cancelled")
                                    
                                    print()
                                
                                elif choi == '4':
                                    print('\n')
                                    product_data='product_manufacture'
                                    new_menufacture=input('Enter product New menufacture :')
                                    product_id=input('Enter product ID number :')
                                    prom=input("To Modify product press y :")
                                    if prom == "y":   
                                        db.product_detail_modify(product_data,new_menufacture,shop_email,product_id)
                                    else:
                                        db.mssg("Process Cancelled")
                                    
                                    print()
                                
                                elif choi == '5':
                                    print('\n')
                                    product_data='product_quantity'
                                    new_quantity=input('Enter product New quantity :')
                                    product_id=input('Enter product ID number :')
                                    prom=input("To Modify press y :")
                                    if prom == "y":   
                                        db.product_detail_modify(product_data,new_quantity,shop_email,product_id)
                                    else:
                                        db.mssg("Process Cancelled")
                                    
                                    print()

                                elif choi == '6':
                                    mssg('Exit Modify')
                                    break

                                else:
                                    db.mssg('Invalid option')

                        elif scho =='4':
                            mssg('Detele Product')
                            print('\n')
                            db.show_shop_prdoucts(shop_email)
                            print()
                            delete_product_id = input('Enter product ID number to delete product :')
                            prom=input("To Delete product press y :")
                            if prom == "y":   
                                db.delete_product(shop_email,delete_product_id)
                            else:
                                db.mssg("Process Cancelled")
                            print()
                              

                        elif scho =='5':
                            mssg('Search history')
                            db.most_searched()
                            db.show_search_log()
                            print()   

                        elif scho =='6':
                            mssg('Orders page')
                            db.show_shop_orders(shop_email)
                            print()     

                        elif scho =='7':
                            mssg('Place Order Status')
                            print()
                            db.show_shop_orders(shop_email)
                            print()
                            order_id = input('Enter order ID Which is placed successfully :')
                            order_status='Deliverd'
                            prom=input("To confirm press y:")
                            if prom == "y":   
                                db.order_status(order_id,order_status,shop_email)
                            else:
                                db.mssg("Process Cancelled")
                            

                        elif scho =='8':
                            mssg('Report page')
                            customer_id=input('Enter customer ID you have to report on :')
                            feed=input('Give Report description in details :')
                            now = datetime.now()
                            report_datetime= str(now.strftime('%Y-%m-%d %H:%M:%S'))
                            prom=input("To confirm press y:")
                            if prom == "y":   
                                db.shop_report(shop_email,customer_id,feed,report_datetime)
                            else:
                                db.mssg("Process Cancelled")
                            

                        elif scho =='9':
                            mssg(f'{shop_email} logout')
                            loggin = False
                        else:
                            mssg('Invalid option')
                            print()


        # ________________________customer login done here______________________________

            elif cho == '2':
                mssg('Customer Login')
                
                while True:
                    customer_email=input('Enter customer Email Address :')
                    x = allvalidation.emailval(customer_email) 
                    if x == True:
                        break
                    else:
                        print()
                        db.mssg("Invalid Email")
                        print()                    

                customer_pass=maskpass.askpass('Enter password :',mask="*")
                loggin = db.customer_login(customer_email,customer_pass)
                print()


                if loggin == True:

                    mssg(f'{customer_email} successfully Loged In')

                    while loggin == True:
                        name=db.customer_name(customer_email)
                        mssg(f'User : {name}')
                        print()
                        print('1.Search\n2.Order Product\n3.Show Orders\n4.Cancel Orders\n5.Report On shop\n6.Log Out')
                        choic = input('Enter your option number:')

                        if choic == '1':
                            mssg('Search page')
                            db.sample_products()
                            search_name = input('Enter product name :')
                            search_pin = input('Enter area pincode (You can skip picode hit Enter) :')
                            now = datetime.now()
                            search_time= str(now.strftime('%Y-%m-%d %H:%M:%S'))

                            if search_name and search_pin == '':
                                db.customer_search_all(search_name)
                                db.search_product_log(search_name,search_time,customer_email)
                            elif search_name and search_pin:
                                db.customer_search_byarea(search_name,search_pin)
                                db.pinsearch_product_log(search_name,search_time,search_pin,customer_email)

                            print('\n\n')
                        
                        elif choic == '2':
                            mssg('Product order page')
                            pro_id = input('Enter Product_id number :')
                            now = datetime.now()
                            order_register_datetime= str(now.strftime('%Y-%m-%d %H:%M:%S'))
                            try:
            
                                pro_quantity = int(input('Enter Quantity number :'))
                                
                                if pro_quantity <= 10 and pro_quantity != 0:
                                    db.product_order_show(pro_id,str(pro_quantity))
                                    print()
                                    conf=input("Confirm Order press y or press n to cancel :")
                                    print()


                                    if conf=="y":
                                        db.product_order(customer_email,pro_id,pro_quantity,order_register_datetime)
                                        print()
                                    elif conf=='n':
                                        db.mssg("Order cancelled")
                                    else:
                                        db.mssg("Invalid option")


                                elif pro_quantity > 10 or pro_quantity == 0:
                                    mssg('Maximum 10 quantity allowed')
                                    print()
                                
                                else:
                                    db.mssg("Invalid Details")
                                    print()

                            except:
                                db.mssg("Incorrect details were given")
                            




                        
                        elif choic == '3':
                            mssg('Booked orders page')
                            db.booked_orders(customer_email)
                        
                        elif choic == '4':
                            mssg('Cancel order page')
                            db.booked_orders(customer_email)
                            print()
                            order_id=int(input('Enter Order ID :'))
                            prom=input("To confirm press y:")
                            if prom == "y":   
                                db.cancel_order(order_id,customer_email)
                            else:
                                db.mssg("Process Cancelled")
                            
                            print()
                        
                        elif choic == '5':
                            mssg('Report page')
                            shop_id=input('Enter Shop ID you have to report on :')
                            feed=input('Give Report description in details :')
                            now = datetime.now()
                            report_datetime= str(now.strftime('%Y-%m-%d %H:%M:%S'))
                            prom=input("To confirm press y:")
                            if prom == "y":   
                                db.customer_report(customer_email,shop_id,feed,report_datetime)
                            else:
                                db.mssg("Process Cancelled")
                        

                        elif choic == '6':
                            mssg('Thank you')
                            mssg(f'{name} Logged out')
                            break 

                        else:
                            db.mssg('Invalid option')

            elif cho =='3':

                mssg('Admin Login')
                admin_id=input('Enter Admin ID :')
                admin_pass=maskpass.askpass('Enter Admin password :',mask="*")
                ad = admin()
                ad =ad._admin_login(admin_id,admin_pass)

                while ad ==True:
                    mssg('Admin page')
                    print('1.Registered users\n2.Reports\n3.Delete User\n4.Log out\n\n')
                    choice = input('Enter your choice number :')
                    print()

                    if choice == '1':
                        while True:
                            mssg('Registered users')
                            print('1.shops\n2.Customers\n3.Exit')
                            cch=input('Enter Your choice number :')

                            if cch =='1':
                                mssg('Shops Details')
                                db.show_shops_admin()
                                print('\n')

                            elif cch =='2':
                                mssg('Customers Details')
                                db.show_customer_admin()
                                print('\n')

                            elif cch =='3':
                                break

                            else:
                                db.mssg('Invalid option')
                        

                    elif choice == '2':
                        mssg('Reports')
                        db.show_reports()

                    elif choice == '3':
                        mssg('Delete Users')
                        print('1.Delete shop\n2.Delete customer\n3.Back')

                        while True:
                            cchh=input('Enter your choice number :')

                            if cchh =='1':
                                shop_id =input('Enter shop ID to delete Shop :')
                                prom=input("To confirm press y:")
                                if prom == "y":   
                                    db.delete_shop(shop_id)
                                else:
                                    db.mssg("Process Cancelled")
                                

                            elif cchh =='2':
                                customer_id =input('Enter customer ID to delete Customer :')
                                prom=input("To confirm press y:")
                                if prom == "y":   
                                    db.delete_customer(customer_id)
                                else:
                                    db.mssg("Process Cancelled")
                                

                            elif cchh =='3':
                                break
                    
                            else:
                                db.mssg('Invalid option')


                    elif choice == '4':
                        mssg('Admin Logged out')
                        ad=False
                    
                    else:
                        db.mssg('Invalid option')

            elif cho == '4':
                break                
            else:
                mssg('Invalid option')

            
    # ____________________Exit block done here______________________________________

    elif ch=='4':
        mssg('THANK YOU')
        break

    else:
        mssg('Invalid Option')


























