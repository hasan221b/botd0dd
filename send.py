
from datetime import datetime
import json_formatter as jf
import time
from datetime import datetime
import os
import json

def read_ordersa(file_name):
    with open(file_name+".json") as json_file:
        
        
        return dict(json.load(json_file))



def send_json_0(name,api_key):

    orders = read_ordersa("email")
    orders = jf.json_format(
                            orders, name, ep = (api_key))
    jf.save_orders("email", orders)

def send_json_code(name,api_key):

    orders = read_ordersa("code")
    orders = jf.json_format(
                            orders, name, ep = (api_key))
    jf.save_orders("code", orders)

def send_json_user(name,api_key):

    orders = read_ordersa("user")
    orders = jf.json_format(
                            orders, name, ep = (api_key))
    jf.save_orders("user", orders)


def send_paer_0(name,api_key):

    orders = read_ordersa("paer")
    orders = jf.json_format(
                            orders, name, ep = (api_key))
    jf.save_orders("paer", orders)


def send_paer_1(name,api_key):

    orders = read_ordersa("paer1")
    orders = jf.json_format(
                            orders, name, ep = (api_key))
    jf.save_orders("paer1", orders)

