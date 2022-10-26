import json
from datetime import datetime
import time


def read_orders(file_name):
    with open(file_name+".json") as json_file:
        orser =dict(json.load(json_file))
        
        return str(orser["x"][0][0]),int(orser["x"][0][1]),int(orser["x"][0][2]),int(orser["x"][0][3]),int(orser["x"][0][4]),float(orser["x"][0][5]),int(orser["x"][0][6]),int(orser["x"][0][7]),int(orser["x"][0][8]),int(orser["x"][0][9]),int(orser["x"][0][10])

def read_orders_0(file_name):
    with open(file_name+".json") as json_file:
        
        
        return dict(json.load(json_file))

def delete_order(orders, ticker):
    del orders[ticker]
    return json.dumps(orders)

def save_orders(file_name, orders):
    with open(file_name+".json", 'w') as json_file:
        json_file.write(orders)


def json_format(orders, ticker, **kwargs):
    # print(ticker)
    orders[ticker] = []
    for arg in kwargs:
        orders[ticker].append(kwargs[arg])
    return json.dumps(orders)


