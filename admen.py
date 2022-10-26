import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json_formatter as jf
import json

import json


# {"60": [["dsfsfsdf","sdfsdfsd"]], "325": [[]], "660": [[]], "1800": [[]], "3850": [[]], "8100": [[]], "16200": [[]]}

# crad = credentials.Certificate("sparkd1-dk.json")
# firebase_admin.initialize_app(crad,{
#     'databaseURL' : 'https://spark-a2c9d-default-rtdb.firebaseio.com/'
# })
crad = credentials.Certificate("sabubg-bc85a-firebase-adminsdk-gh1a5-c66fbdb3ec.json")
firebase_admin.initialize_app(crad,{
            'databaseURL' : 'https://sabubg-bc85a-default-rtdb.firebaseio.com/'
        })



def code_0(x,a):
    ref =db.reference("code/"+a)
    ref.set([x])


def code_1(x):
    ref =db.reference("code")
    ref.set(x)


def code_1s(x):
    ref =db.reference("codes")
    ref.set(x)



# code_1(order)
def all_user(x):
    ref =db.reference("user")
    ref.set(x)



# order=jf.read_orders_0("email")
def all_email2(x):
    x = str(x).replace("l.c", 'lc')
    x = x.replace("'", '"')
    x=json.loads(x)
    ref =db.reference("email")
    ref.set(x)




# all_email2(order)

def reado_code_p():
    ref = db.reference("code")
    ref=ref.get() 
    ref= str(ref)
    ref = ref.replace("'", '"')
    ref1 = db.reference("codes")
    ref1=ref1.get() 
    
    if ref=="None":
        ref="{}"
    ref=json.loads(ref)
    for k in  ref1:
        if k not in ref:
            ref[k]=[[]]
    ref= str(ref)
    ref = ref.replace("'", '"')  
    jf.save_orders("code", ref)  



def reado_rename_code_p(c,v):
    reado_code_p()
    order=jf.read_orders_0("code")
    lest_anme=[]
    lest_ddd=[]
    for i in order:
        lest_anme.append(i)
    for ik in lest_anme:
        if ik == c:
            order[v] = order.pop(ik)
            lest_ddd .append(v)
        else:
            order[ik] = order.pop(ik)  
            lest_ddd .append(ik)
    code_1(order)
    code_1s(lest_ddd)        
    order=json.dumps(order)
    
    jf.save_orders("code", order)  
    # print(order)
# jf.save_orders("code", str(order))
# reado_rename_code_p("60","70")


def reado_user_p():
    ref = db.reference("user")
    ref=ref.get() 
    ref= str(ref)
    ref = ref.replace("'", '"')
    if ref=="None":
        ref="{}" 
    jf.save_orders("user", ref) 
    # return json.loads(ref)

def reado_email_p():
    ref = db.reference("email")
    ref=ref.get() 
    ref= str(ref)
    ref = ref.replace("lc", 'l.c')
    ref = ref.replace("'", '"')
    if ref=="None":
        ref="{}"
    jf.save_orders("email", ref)      
    # return json.loads(ref)


# reado_email_p()


