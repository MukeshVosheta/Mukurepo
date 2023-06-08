import database as db
class shop_register:
    def __init__(self,shop_firstname,shop_lastname,shop_name,shop_add,shop_pincode,shop_contact,shop_email,shop_pass,shop_register_time):
        
        self.shop_firstname=shop_firstname
        self.shop_lastname=shop_lastname
        self.shop_name=shop_name
        self.shop_add=shop_add
        self.shop_pincode=shop_pincode
        self.shop_contact=shop_contact
        self.shop_email=shop_email
        self.shop_pass=shop_pass
        self.shop_register_time=shop_register_time

    def __repr__(self):
        return f"shop_register[{self.shop_firstname},{self.shop_lastname},{self.shop_name},{self.shop_add},{self.shop_pincode},{self.shop_contact},{self.shop_email},{self.shop_pass},{self.shop_register_time}]"



class product_register:
    def __init__(self,product_name,product_price,product_detail,product_manufacture,product_quantity,shop_email):
        self.product_name=product_name
        self.product_price=product_price
        self.product_detail=product_detail
        self.product_manufacture=product_manufacture
        self.product_quantity=product_quantity
        self.shop_email=shop_email

    def __repr__(self):
        return f"product_register[{self.product_name},{self.product_price},{self.product_detail},{self.product_manufacture},{self.product_quantity},{self.shop_email}]"
    

class customer_register:
    def __init__(self,customer_firstname,customer_lastname,customer_add,customer_contact,customer_email,customer_pass,customer_register_time):
        
        self.customer_firstname=customer_firstname
        self.customer_lastname=customer_lastname
        self.customer_add=customer_add
        self.customer_contact=customer_contact
        self.customer_email=customer_email
        self.customer_pass=customer_pass
        self.customer_register_time=customer_register_time

    def __repr__(self):
        return f"customer_register[{self.customer_firstname},{self.customer_lastname},{self.customer_add},{self.customer_contact},{self.customer_email},{self.customer_pass},{self.customer_register_time}]"
    

class admin:
    def __init__(self):
        self._admin_id = 'admin01'
        self._admin_pass = 'admin0102'
    
    def _admin_login (self,admin_id,admin_pass):
        
        if admin_id == self._admin_id:
            if admin_pass == self._admin_pass:
                return True
            else:
                return db.mssg("wrong password")         
        else:
            return db.mssg('Wrong Admin ID')





































