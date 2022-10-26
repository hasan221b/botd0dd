# from tokenize import Name
import telebot
from telebot import types
from telebot.types import LabeledPrice, ShippingOption
import json_formatter as js
from telegram import *
import requests
from requests import *
import pandas as pd
from datetime import datetime
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import datetime as ati
import random
import threading

nl ="\n"
import admen as asdf
import bot as dggg
Subscribe_1=30
import send
nl = "\n"
av = "%20%60"
pracant = "%20%25"
API_KEY = '5424683686:AAFV3fXDym0dgd-cm7KkzvROAuBzuHgtGZA'

provider_token = '5424683686:AAFV3fXDym0dgd-cm7KkzvROAuBzuHgtGZA'  # @BotFather -> Bot Settings -> Payments

def send_msg(my_chat_id,text):
    url ="https://api.telegram.org/bot"+API_KEY+"/sendMessage?chat_id="+ my_chat_id+"&parse_mode=Markdown&text="
    request = url+text
    response = requests.get(request)
    return response.json()
# Data of items 
# 
bot = telebot.TeleBot(API_KEY)


@bot.callback_query_handler(func=lambda call:True)

def callback_idnline(call):
        # print(call)
        # print(call.from_user.id)
        idcol=call.from_user.id
   

        if call.data == "𝐄𝐌𝐀𝐈𝐋":
                asdf.reado_email_p()
                order=js.read_orders_0("email")
                maseges=""
                for i in order:
                                maseges=maseges+i+nl
                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                first_button1 = types.InlineKeyboardButton(text="add email", callback_data="add email")
                first_button2 = types.InlineKeyboardButton(text="dell email", callback_data="dell email")

                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                
                
                keyboardmain.add(first_button1,first_button2,z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="📬📬📬 𝐄𝐌𝐀𝐈𝐋 📬📬📬"+nl+nl+maseges,reply_markup=keyboardmain)
        elif call.data == "𝐄𝐃𝐈𝐓 𝐂𝐎𝐃𝐄":
                asdf.reado_code_p()
                order=js.read_orders_0("code")
                maseges=""
                
                bo=0                    
                for i in order:
                        
                        if bo==0 :
                                t1 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                        if bo==1 :
                                t2 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                        if bo==2 :
                                t3 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                        if bo==3 :
                                t4 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                        if bo==4 :
                                t5 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                        if bo==5 :
                                t6 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                        if bo==6 :
                                t7 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                        bo=bo +1


                keyboardmain = types.InlineKeyboardMarkup(row_width=4)
               
                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                keyboardmain.add(t1,t2,t3,t4,t5,t6,t7,z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="🖋🖋🖋🖋 𝐄𝐃𝐈𝐓 𝐂𝐎𝐃𝐄 🖋🖋🖋🖋"+nl+nl+maseges,reply_markup=keyboardmain)
        elif call.data == "𝐂𝐎𝐃𝐄":
                asdf.reado_code_p()
                order=js.read_orders_0("code")
                maseges=""
                for i in order:
                                maseges=maseges+"💰💎 "+i+" 💎💰"+nl+nl
                                
                                for c in order[i][0]:
                                       
                                                maseges=maseges+c+nl    
                bo=0                    
                for i in order:
                        
                        if bo==0 :
                                t1 = types.InlineKeyboardButton(text=i, callback_data=i+"codef")
                        if bo==1 :
                                t2 = types.InlineKeyboardButton(text=i, callback_data=i+"codef")
                        if bo==2 :
                                t3 = types.InlineKeyboardButton(text=i, callback_data=i+"codef")
                        if bo==3 :
                                t4 = types.InlineKeyboardButton(text=i, callback_data=i+"codef")
                        if bo==4 :
                                t5 = types.InlineKeyboardButton(text=i, callback_data=i+"codef")
                        if bo==5 :
                                t6 = types.InlineKeyboardButton(text=i, callback_data=i+"codef")
                        if bo==6 :
                                t7 = types.InlineKeyboardButton(text=i, callback_data=i+"codef")
                        bo=bo +1


                keyboardmain = types.InlineKeyboardMarkup(row_width=4)
               
                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                
                
                keyboardmain.add(t1,t2,t3,t4,t5,t6,t7,z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="📝📝📝📝 𝐂𝐎𝐃𝐄 📝📝📝📝"+nl+nl+maseges,reply_markup=keyboardmain)
        
        
        
        elif call.data == "𝐔𝐒𝐄𝐑":
                asdf.reado_user_p()
                order=js.read_orders_0("user")
                maseges=""
                for i in order:
                                maseges=maseges+i+nl
                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                first_button1 = types.InlineKeyboardButton(text="add user", callback_data="add user")
                first_button2 = types.InlineKeyboardButton(text="dell user", callback_data="dell user")

                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                
                
                keyboardmain.add(first_button1,first_button2,z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="👨🏻‍⚖️👨🏻‍⚖️👨🏻‍⚖️ 𝐔𝐒𝐄𝐑 👨🏻‍⚖️👨🏻‍⚖️👨🏻‍⚖️"+nl+nl+maseges,reply_markup=keyboardmain)
        elif call.data == "Back" :
                
                
                frame1="🟢🟢 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐃𝐄𝐀𝐑 🟢🟢"+nl
                rsiup1="what do you want me to do "+nl
        
                masge=frame1+rsiup1

                # z1 =types.InlineKeyboardButton(text=str("𝐑𝐄𝐃𝐄𝐄𝐌"), callback_data=str("𝐑𝐄𝐃𝐄𝐄𝐌"))

                z2 =types.InlineKeyboardButton(text=str("𝐂𝐎𝐃𝐄"), callback_data=str("𝐂𝐎𝐃𝐄"))
                z3 =types.InlineKeyboardButton(text=str("𝐄𝐌𝐀𝐈𝐋"), callback_data=str("𝐄𝐌𝐀𝐈𝐋"))

                z4 =types.InlineKeyboardButton(text=str("𝐔𝐒𝐄𝐑"), callback_data=str("𝐔𝐒𝐄𝐑"))
                z6 =types.InlineKeyboardButton(text=str("𝐄𝐃𝐈𝐓 𝐂𝐎𝐃𝐄"), callback_data=str("𝐄𝐃𝐈𝐓 𝐂𝐎𝐃𝐄"))




                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                keyboardmain.add(z2,z6,z3,z4)
                # bot.send_message(call.message.chat.id,masge, reply_markup=keyboardmain)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=masge,reply_markup=keyboardmain)
        elif call.data =="add email" :
                
                
                

                frame1="Send email and pas as "+nl+"Example  :  addemail=ali@gmail.com,23151513"
                
                masge=frame1
                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))

                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                keyboardmain.add(z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=masge,reply_markup=keyboardmain)
        elif call.data =="dell email":
                frame1="Send email and pas as "+nl+"Example  :  dellemail=ali@gmail.com,23151513"
                
                masge=frame1
                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))

                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                keyboardmain.add(z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=masge,reply_markup=keyboardmain)
        
        elif call.data =="add user" :
                
                
                

                frame1="Send user  as "+nl+"Example  :  adduser=1561651"
                
                masge=frame1
                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))

                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                keyboardmain.add(z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=masge,reply_markup=keyboardmain)
        elif call.data =="dell user":
                frame1="Send user  as "+nl+"Example  :  delluser=1215165"
                
                masge=frame1
                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))

                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                keyboardmain.add(z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=masge,reply_markup=keyboardmain)
        
        elif "coder" in call.data :
                xa=call.data.replace("coder","")
                if " " in xa:
                        xa=xa.replace(" ","")
                xa=str(xa)
                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                
                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                maseges="Send new name  as "+nl+"Example  :  nameco="+xa+",300"
                
                keyboardmain.add(z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=maseges,reply_markup=keyboardmain) 

        elif "codef" in call.data :
                xa=call.data.replace("codef","")
                if " " in xa:
                        xa=xa.replace(" ","")

                xa=str(xa)
                asdf.reado_code_p()
                order=js.read_orders_0("code")
                if xa in  order:
                        maseges="Send code  as "+nl+"Example  :  code"+xa+"=dsfef156e1f65s"
                        

                        keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                
                        z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                        
                        
                        keyboardmain.add(z11y)
                        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=maseges,reply_markup=keyboardmain) 
        elif "asd" in call.data : 
                xa=call.data.replace("asd","")
                if " " in xa:
                        xa=xa.replace(" ","")

                xa=str(xa)
                bny=xa.split(",")


                for v in range(1,11):
                        i=str(v)
                        if v==1 :
                                t1 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                        if v==2 :
                                t2 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                        if v==3 :
                                t3 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                        if v==4 :
                                t4 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                        if v==5 :
                                t5 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                        if v==6 :
                                t6 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                        if v==7 :
                                t7 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                        if v==8 :
                                t8 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                        if v==9 :
                                t9 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")  
                        if v==10 :
                                t10 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")                      
                        # bo=bo +1


                keyboardmain = types.InlineKeyboardMarkup(row_width=3)
               
                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                z131y =types.InlineKeyboardButton(text=str("⬅️"), callback_data=str("⬅️1"+bny[1]))
                
                
                keyboardmain.add(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,z131y,z11y)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="📝"+xa+"📝"+nl+nl,reply_markup=keyboardmain)
        



















                # order=js.read_orders_0("code")
                # if xa[0] in  order:
                #         if []!= order[xa[0]][0]:
                #                 maseges=" بدات عملية شحن الحساب"
                                

                #                 keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                        
                #                 z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                
                #                 threading.Thread(target =  dggg.buy_user,args=[xa[1] ,call.message.chat.id,xa[0],0]).start()
                                
                #                 keyboardmain.add(z11y)
                #                 bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=maseges,reply_markup=keyboardmain)                       
                #         else:
                #                 keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                        
                #                 z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                #                 keyboardmain.add(z11y)
                #                 bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="لا يوجد كودات",reply_markup=keyboardmain)    
        elif "tamer" in call.data : 
                xa=call.data.replace("tamer","")
                if " " in xa:
                        xa=xa.replace(" ","")
                xac=str(xa)
                xa=xa.split(",")
                asdf.reado_code_p()
                order=js.read_orders_0("code")
                if xa[0] in  order:
                        if int(xa[2])<= len(order[xa[0]][0]): 


                                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                                zy =types.InlineKeyboardButton(text=str("confirm"), callback_data=xac+str("confirm"))
                                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                z110y =types.InlineKeyboardButton(text=str("⬅️"), callback_data=str(xa[0]+","+xa[1]+"asd"))
                                keyboardmain.add(zy,z11y,z110y)
                                # xa=str(xa)
                                # xa=xa.split(",")
                                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Quantity  :  "+xa[0] +nl+"x"+xa[2]  +nl+"id  : "+xa[1]  ,reply_markup=keyboardmain)    
                        else:


                                xa=str(xac)
                                bny=xa.split(",")
                                xa=bny[0]+","+bny[1]
                                bny=xa.split(",")
                                for v in range(1,11):
                                        i=str(v)
                                        if v==1 :
                                                t1 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                                        if v==2 :
                                                t2 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                                        if v==3 :
                                                t3 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                                        if v==4 :
                                                t4 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                                        if v==5 :
                                                t5 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                                        if v==6 :
                                                t6 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                                        if v==7 :
                                                t7 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                                        if v==8 :
                                                t8 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")
                                        if v==9 :
                                                t9 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")  
                                        if v==10 :
                                                t10 = types.InlineKeyboardButton(text=i, callback_data=xa+","+i+"tamer")                      
                                        # bo=bo +1


                                keyboardmain = types.InlineKeyboardMarkup(row_width=3)
                        
                                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                z131y =types.InlineKeyboardButton(text=str("⬅️"), callback_data=str("⬅️1"+bny[1]))
                                
                                
                                keyboardmain.add(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,z131y,z11y)
                                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="There is only "+str(len(order[bny[0]][0]))+ " code"+nl+"📝"+xa+"📝"+nl+nl,reply_markup=keyboardmain)
        elif "confirm" in call.data : 
                xa=call.data.replace("confirm","")
                if " " in xa:
                        xa=xa.replace(" ","")
                xac=str(xa)
                xa=str(xa)
                xa=xa.split(",")
                asdf.reado_code_p()
                order=js.read_orders_0("code")
                if xa[0] in  order:
                        if int(xa[2])<= len(order[xa[0]][0]):
                                maseges="charging process has begun..."
                                

                                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                        
                                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                
                                threading.Thread(target =  dggg.buy_user,args=[xa[1] ,call.message.chat.id,xa[0],0,int(xa[2]),0]).start()
                                
                                keyboardmain.add(z11y)
                                bot.send_message(chat_id=call.message.chat.id, text=maseges,reply_markup=keyboardmain) 
                                try:
                                        bo=0  
                                        order=js.read_orders_0("code")   
                                        xa=xa[1]                
                                        for i in order:
                                                
                                                if bo==0 :
                                                        t1 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                                if bo==1 :
                                                        t2 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                                if bo==2 :
                                                        t3 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                                if bo==3 :
                                                        t4 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                                if bo==4 :
                                                        t5 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                                if bo==5 :
                                                        t6 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                                if bo==6 :
                                                        t7 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                                bo=bo +1


                                        keyboardmain = types.InlineKeyboardMarkup(row_width=3)
                                
                                        z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                        keyboardmain.add(t1,t2,t3,t4,t5,t6,t7,z11y)
                                        
                                        # bot.edit_message_text(call.message.chat.id,"💵Choose Quantity💵 ",reply_markup=keyboardmain)
                                        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="💵Choose Quantity💵 ",reply_markup=keyboardmain)



                                except:
                
                                        pass    




                        else:
                                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                        
                                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                bot.send_message(chat_id=call.message.chat.id, text="There is only "+str(len(order[xa[0]][0]))+ " code"  ,reply_markup=keyboardmain)    
        elif "⬅️1" in call.data : 
                xa=call.data.replace("⬅️1","")        
                try:
                                bo=0  
                                asdf.reado_code_p()
                                order=js.read_orders_0("code")                   
                                for i in order:
                                        
                                        if bo==0 :
                                                t1 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                        if bo==1 :
                                                t2 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                        if bo==2 :
                                                t3 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                        if bo==3 :
                                                t4 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                        if bo==4 :
                                                t5 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                        if bo==5 :
                                                t6 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                        if bo==6 :
                                                t7 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
                                        bo=bo +1


                                keyboardmain = types.InlineKeyboardMarkup(row_width=3)
                        
                                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                keyboardmain.add(t1,t2,t3,t4,t5,t6,t7,z11y)
                                
                                bot.send_message(call.message.chat.id,"💵Choose Quantity💵 ",reply_markup=keyboardmain)



                except:
       
                        pass    

        # elif "⬅️2" in call.data : 
        #         xa=call.data.replace("⬅️2","")        
        #         try:
        #                         bo=0  
        #                         order=js.read_orders_0("code")                   
        #                         for i in order:
                                        
        #                                 if bo==0 :
        #                                         t1 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
        #                                 if bo==1 :
        #                                         t2 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
        #                                 if bo==2 :
        #                                         t3 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
        #                                 if bo==3 :
        #                                         t4 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
        #                                 if bo==4 :
        #                                         t5 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
        #                                 if bo==5 :
        #                                         t6 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
        #                                 if bo==6 :
        #                                         t7 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+xa)
        #                                 bo=bo +1


        #                         keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                        
        #                         z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
        #                         keyboardmain.add(t1,t2,t3,t4,t5,t6,t7,z11y)
                                
        #                         bot.send_message(call.message.chat.id,".     اخترالكمبة  ",reply_markup=keyboardmain)



        #         except:
       
        #                 pass 

@bot.message_handler()
def exemple_keyboard(message):
    mas = message.text
    cid =message.chat.id
    cidtt =message.chat.username

    
#     fd =(message.json)["from"]['id']
    fd =message.forward_date
    print(mas)
    asdf.reado_user_p()
    ordersx=js.read_orders_0("user") 


    if str(cid) in ordersx:

        if "/start" in mas :
                # frame,rsiup,rsidu,bandslen,bands_Sd,SARnim,SARmax,SARup,SARdu,hik_up,hik_du=js.read_orders("settv")
                frame1="🟢🟢 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐃𝐄𝐀𝐑 🟢🟢"+nl
                rsiup1="what do you want me to do "+nl
        
                masge=frame1+rsiup1

                # z1 =types.InlineKeyboardButton(text=str("𝐑𝐄𝐃𝐄𝐄𝐌"), callback_data=str("𝐑𝐄𝐃𝐄𝐄𝐌"))

                z2 =types.InlineKeyboardButton(text=str("𝐂𝐎𝐃𝐄"), callback_data=str("𝐂𝐎𝐃𝐄"))
                z6 =types.InlineKeyboardButton(text=str("𝐄𝐃𝐈𝐓 𝐂𝐎𝐃𝐄"), callback_data=str("𝐄𝐃𝐈𝐓 𝐂𝐎𝐃𝐄"))
                z3 =types.InlineKeyboardButton(text=str("𝐄𝐌𝐀𝐈𝐋"), callback_data=str("𝐄𝐌𝐀𝐈𝐋"))

                z4 =types.InlineKeyboardButton(text=str("𝐔𝐒𝐄𝐑"), callback_data=str("𝐔𝐒𝐄𝐑"))




                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                keyboardmain.add(z2,z6,z3,z4)




                bot.send_message(message.chat.id,masge, reply_markup=keyboardmain)



        elif "addemail=" in mas  :
                xa=mas.replace("addemail=","")
                if " " in xa:
                        xa=xa.replace(" ","")

                xa=str(xa)
                xa=xa.split(",")
                asdf.reado_email_p()
                send.send_json_0(xa[0],xa[1])
                order=js.read_orders_0("email") 
                asdf.all_email2(order)
                maseges=""
                for i in order:
                                maseges=maseges+i+nl
                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                first_button1 = types.InlineKeyboardButton(text="add email", callback_data="add email")
                first_button2 = types.InlineKeyboardButton(text="dell email", callback_data="dell email")

                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                
                
                keyboardmain.add(first_button1,first_button2,z11y)
                bot.send_message(message.chat.id,"📬📬📬 𝐄𝐌𝐀𝐈𝐋 📬📬📬"+nl+nl+maseges,reply_markup=keyboardmain)

        elif "code"in mas :
                masf=mas
                x=0
                for o in mas:
                        if o =="=":
                            mas =mas[x+1:] 
                        #     print(mas) 
                            xa=masf.replace("code","")
                            xa=xa.replace("=","") 
                            xa=xa.replace(mas,"") 
                            xa=xa.replace(" ","") 
                            asdf.reado_code_p()
                            order=js.read_orders_0("code") 

                            lestcode=order[xa][0]
                            
                            if "," not in mas:
                                if mas not in lestcode:

                                        lestcode.append(mas)
                                        send.send_json_code(xa,lestcode)
                                        order=js.read_orders_0("code") 
                                        asdf.code_0(lestcode,xa)
                                        bot.send_message(message.chat.id,"✅Code has been added✅")
                                else:
                                        bot.send_message(message.chat.id,"❌ The code already exists ❌")
                            else:
                                mas=mas.split(",") 
                                for mas55 in  mas:
                                        if mas55 not in lestcode:

                                                lestcode.append(mas55)
                                                send.send_json_code(xa,lestcode)
                                                bot.send_message(message.chat.id,"✅Code has been added✅"+nl+mas55+nl+xa)
                                        else:
                                                bot.send_message(message.chat.id,"❌ The code already exists ❌"+nl+mas55+nl+xa)
                            

                                asdf.code_0(lestcode,xa)


                        x=x+1
        elif "nameco="in mas :
                try:
                        xa=mas.replace("nameco=","")
                        if " " in xa:
                                xa=xa.replace(" ","")

                        xa=str(xa)
                        xa=xa.split(",")
                        asdf.reado_code_p()
                        order=js.read_orders_0("code") 
                        print(xa)
                        if xa[0]  in order:

                                # lestyy=order[xa[0]][0]
                                # order=js.delete_order(order, xa[0])
                                # js.save_orders("code", order)
                                # send.send_json_code(xa[1],lestyy)
                                asdf.reado_rename_code_p(xa[0],xa[1])
                                asdf.reado_code_p()
                                order=js.read_orders_0("code") 
                                


                                
                                bo=0                    
                                for i in order:
                                        
                                        if bo==0 :
                                                t1 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                                        if bo==1 :
                                                t2 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                                        if bo==2 :
                                                t3 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                                        if bo==3 :
                                                t4 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                                        if bo==4 :
                                                t5 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                                        if bo==5 :
                                                t6 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                                        if bo==6 :
                                                t7 = types.InlineKeyboardButton(text=i, callback_data=i+"coder")
                                        bo=bo +1


                                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                        
                                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                keyboardmain.add(t1,t2,t3,t4,t5,t6,t7,z11y)
                                
                                bot.send_message(message.chat.id,"📝📝📝📝 𝐂𝐎𝐃𝐄 📝📝📝📝",reply_markup=keyboardmain)
                        else:
                                bot.send_message(message.chat.id,xa[0]+" not in name   ")   
                except:
                        pass

        elif "dellemail=" in mas :
                
                try:
                        xa=mas.replace("dellemail=","")
                        if " " in xa:
                                xa=xa.replace(" ","")

                        xa=str(xa)
                        xa=xa.split(",")
                        asdf.reado_email_p()
                        order=js.read_orders_0("email") 
                        if xa[0]  in order:
                                order=js.delete_order(order, xa[0])
                                js.save_orders("email", order)
                        

                                order=js.read_orders_0("email") 
                                asdf.all_email2(order)
                                maseges=""
                                for i in order:
                                                maseges=maseges+i+nl
                                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                                first_button1 = types.InlineKeyboardButton(text="add email", callback_data="add email")
                                first_button2 = types.InlineKeyboardButton(text="dell email", callback_data="dell email")

                                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                
                                
                                keyboardmain.add(first_button1,first_button2,z11y)
                                bot.send_message(message.chat.id,"📬📬📬 𝐄𝐌𝐀𝐈𝐋 📬📬📬"+nl+nl+maseges,reply_markup=keyboardmain)
                        else:
                                bot.send_message(message.chat.id,xa[0]+" not in lest   ")   
                except:
                        pass

        

        elif "adduser=" in mas  :
                xa=mas.replace("adduser=","")
                if " " in xa:
                        xa=xa.replace(" ","")

                xa=str(xa)
                xa=xa.split(",")
                asdf.reado_user_p()
                send.send_json_user(xa[0],"")
                order=js.read_orders_0("user")
                asdf.all_user(order) 
                maseges=""
                for i in order:
                                maseges=maseges+i+nl
                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                first_button1 = types.InlineKeyboardButton(text="add user", callback_data="add user")
                first_button2 = types.InlineKeyboardButton(text="dell user", callback_data="dell user")

                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                
                
                keyboardmain.add(first_button1,first_button2,z11y)
                bot.send_message(message.chat.id,"👨🏻‍⚖️👨🏻‍⚖️👨🏻‍⚖️ 𝐔𝐒𝐄𝐑 👨🏻‍⚖️👨🏻‍⚖️👨🏻‍⚖️"+nl+nl+maseges,reply_markup=keyboardmain)

        

        elif "delluser=" in mas :
                try:
                        xa=mas.replace("delluser=","")
                        if " " in xa:
                                xa=xa.replace(" ","")

                        xa=str(xa)
                        xa=xa.split(",")
                        asdf.reado_user_p()
                        order=js.read_orders_0("user") 
                        if xa[0]  in order:
                                order=js.delete_order(order, xa[0])
                                js.save_orders("user", order)
                        

                                order=js.read_orders_0("user") 
                                asdf.all_user(order)
                                maseges=""
                                for i in order:
                                                maseges=maseges+i+nl
                                keyboardmain = types.InlineKeyboardMarkup(row_width=1)
                                first_button1 = types.InlineKeyboardButton(text="add user", callback_data="add user")
                                first_button2 = types.InlineKeyboardButton(text="dell user", callback_data="dell user")

                                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                
                                
                                keyboardmain.add(first_button1,first_button2,z11y)
                                bot.send_message(message.chat.id,"👨🏻‍⚖️👨🏻‍⚖️👨🏻‍⚖️ 𝐔𝐒𝐄𝐑 👨🏻‍⚖️👨🏻‍⚖️👨🏻‍⚖️"+nl+nl+maseges,reply_markup=keyboardmain)
                        else:
                   
                   
                   
                   
                                bot.send_message(message.chat.id,xa[0]+" not in lest   ")   
                except:
       
                        pass  
        elif    mas.isdigit  :
                try:
                                bo=0  
                                asdf.reado_code_p()
                                order=js.read_orders_0("code")                   
                                for i in order:
                                        
                                        if bo==0 :
                                                t1 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+mas)
                                        if bo==1 :
                                                t2 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+mas)
                                        if bo==2 :
                                                t3 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+mas)
                                        if bo==3 :
                                                t4 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+mas)
                                        if bo==4 :
                                                t5 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+mas)
                                        if bo==5 :
                                                t6 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+mas)
                                        if bo==6 :
                                                t7 = types.InlineKeyboardButton(text=i, callback_data=i+"asd,"+mas)
                                        bo=bo +1


                                keyboardmain = types.InlineKeyboardMarkup(row_width=3)
                        
                                z11y =types.InlineKeyboardButton(text=str("Back"), callback_data=str("Back"))
                                keyboardmain.add(t1,t2,t3,t4,t5,t6,t7,z11y)
                                
                                bot.send_message(message.chat.id,"💵Choose Quantity💵  ",reply_markup=keyboardmain)



                except:
       
                        pass                
    else:
         bot.send_message(message.chat.id,"You don't have access ")          
         bot.send_message(message.chat.id,str(message.chat.id))      

        
        
bot.skip_pending = True            
bot.polling(none_stop=True)