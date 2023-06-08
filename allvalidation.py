import re
import database as db


#___________________namevalidation____________________
def nameval(data):
    sp="^[a-zA-Z\ ]+$"
    if re.match(sp, data):
        return True
    else:
        return False
    
#__________________pincodevalidation__________________
def pincval(data):
    sp = "[0-9]{6}$"
    if re.match(sp, data):
        return True
    else:
        return False

#__________________contactvalidation__________________
def conval(data):
    sp = "[6-9][0-9]{9}$"
    if re.match(sp,data):
        return True
    else:
        return False

#__________________emailvalidation__________________
def emailval(data):
    sp="^[a-zA-Z0-9\_\.]+\@[a-z]+\.[com|in|org]+$"
    if re.match(sp, data):
        return True
    else:
        return False
    
#__________________addressvalidation__________________
def addressval(data):
    sp='^[a-zA-Z0-9\.\s\-\,]'
    if re.match(sp, data):
        return True
    else:
        db.mssg("Invalid Address")

#__________________passwordvalidation__________________
def passval(ps1,ps2):
    if ps1==ps2:
        if len(ps1)>=6:
            return True
        else:
            db.mssg('Password should greater then 5 digit')

#__________________productprice__________________
def priceval(pr):
    sp = "[0-9]+[0-9]"
    if re.match(sp,pr):
        if int(pr) <= 30000:
            return True
        else:
            db.mssg('Maximum Price is 30,000 ')
    else:
        db.mssg('Invalid Price')


#___________________quantityvalidation_____________
def quantityval(qn):
    sp = "[0-9]+[0-9]"
    if re.match(sp,qn):
        if int(qn) <= 300:
            return True
        else:
            db.mssg('Maximum Quantity is 300')
    else:
        db.mssg('Invalid Quantity')












