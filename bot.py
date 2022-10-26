# import csv
# from re import T
# import code
import time
import telebot
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
import json_formatter as js
import send
import random
from selenium.webdriver.chrome.options import Options
import admen as asdf
import os

nl = "\n"
# options = webdriver.ChromeOptions()
# options = Options()
# CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
# GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')

# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
# options.add_argument('user-agent={0}'.format(user_agent))

# options.add_argument("--start-maximized")
options = webdriver.ChromeOptions()
# options.binary_location = GOOGLE_CHROME_BIN
# options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--profile-directory=Default")
options.add_experimental_option("detach", True)  # keep browser not closed
options.add_argument('--blink-settings=imagesEnabled=false')  # disable images
options.headless = True  # TO TRUE
options.add_experimental_option("excludeSwitches", ['enable-logging'])
# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , chrome_options=options)
# driver1 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# zv=random.randint(0,len(order))
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
def buy_user(idds,shat,codernum,loif,numper2,numper0):




        asdf.reado_email_p()
        order=js.read_orders_0("email")
                
    # for em in order:
        cdf=random.randint(0,len(order)-1)
        lest_emaels=[]
        for mj in order:
            lest_emaels.append(mj)
        em=  lest_emaels[cdf]     
        passd=  order [lest_emaels[cdf]] [0]          
        API_KEYs = '5424683686:AAFV3fXDym0dgd-cm7KkzvROAuBzuHgtGZA'
        asdf.reado_code_p()
        order=js.read_orders_0("code")
        bot = telebot.TeleBot(API_KEYs)
            
        
        if order[codernum][0]!=[]:
            # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
            # driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=options)

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            oos = order[codernum][0][0]

            
        




            # em="tameralselwady@gmail.com"
            # passd="t99kViXgAjBS3eL"
            # idds="5602807901"
            # oos="P7W3SsrC2E226dAaRe"
            driver.get('https://www.midasbuy.com/midasbuy/ot/redeem/pubgm')
            try:
                try:
                    btn = WebDriverWait(driver, 7).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.visa-card-pat-face-pop .pop-content .close-btn')))
                    btn.click()
                    
                except  :
                    pass
                btn = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,  '.login-box .login-btn')))
                driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, '#login-iframe'))
                inputs = driver.find_elements(By.CSS_SELECTOR, '.block > .input-box > input')
                if len(inputs) > 0:
                    inputs[0].send_keys(em)
                    inputs[1].send_keys(passd)
                    inputs[1].send_keys(Keys.RETURN)
                driver.switch_to.default_content()

                player_id = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.game-wrap .tab-nav-box .box .input-box.have-select-input-box .input')))
                redeem = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.redeem-box .box .input')))
                
                # time.sleep(1)
                player_id.send_keys(idds)
                redeem.send_keys(oos)
                time.sleep(2)
                try:
                    btn = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.redeem-box.email-box .btn-box .btn')))
                    btn.click()
                except   :
                    pass

                x=0
                errrrrr=""
                
                # if x==0:
                #     try:
                        # dialog = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.pop-redeem-box .warnning-text')))
                #         errrrrr=(dialog.text)
                #         print(2)
                        
                #         x=4
                #     except   :
                #         pass
                if x==0:
                    try:

                        error_2 = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '//div[@class="redeem-box error"] //p[2]')))
                        errrrrr=(error_2.text)
                        x=3
                    except   :
                        pass
                if x==0:    
                    try:
                        WebDriverWait(driver, 8).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.pop-redeem-box .btn-box .btn.btn-submit'))).click()
                        driver.switch_to.default_content()
                        # x=2
                    except   :
                        pass
  
                try:

                    error_3 = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '//div[@class="redeem-box error"] //p[@class="error-tips"]')))
                    # print(error_3)
                    errrrrr=(error_3.text)
                    x=3

                except   :
                    pass
                if x==0: 
                    try:
                        error_2 = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '//div[@class="redeem-box error"] //p[2]')))
                        x=3
                        errrrrr=(error_2.text)
                    except   :
                        pass


                try:
                    time.sleep(2)
                    error_3 = WebDriverWait(driver, 7).until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '.buy-suc-box .title p')))
                    errrrrr=(error_3[0].text)
                    # print(errrrrr)
                    x=5
                    # print(errrrrr)

                except     :
                    pass
                if x!=5:
                    try:
                        error_1 = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'p.error-tips.show')))
                        errrrrr=(error_1.text)
                        x=1
                    except   :
                        pass
                if x==5:
                    numper0=numper0+1
                    bot.send_message(shat,errrrrr+"   "+nl+idds+nl+"Quantity    "+codernum+nl+"num "+str(numper0)+" / "+str(numper2))
                    asdf.reado_code_p()
                    order=js.read_orders_0("code")
                    lest_vo=order[codernum][0]
                    lest_vo.remove(oos)
                    asdf.code_0(lest_vo,codernum)
                    send.send_json_code(codernum,lest_vo)
                    if numper0 < numper2:
                        buy_user(idds,shat,codernum,loif,numper2,numper0)
                       

                    
                elif x==1:
                    bot.send_message(shat,errrrrr+"   "+nl+idds)
                    # order=js.read_orders_0("code")
                    # lest_vo=order[codernum][0]
                    # lest_vo.remove(oos)
                    # send.send_json_code(codernum,lest_vo)
                    # buy_user(idds,shat,codernum)
                    # try:
                    #         driver.quit() 
                    # except  :
                    #         pass 
                elif x==3:
                    bot.send_message(shat,errrrrr+"   "+nl+oos)
                    asdf.reado_code_p()
                    order=js.read_orders_0("code")
                    lest_vo=order[codernum][0]
                    lest_vo.remove(oos)
                    asdf.code_0(lest_vo,codernum)
                    send.send_json_code(codernum,lest_vo)
                    try:
                        driver.quit()
                    except  :
                            pass
                    buy_user(idds,shat,codernum,loif+1,numper2,numper0)

                elif x==0:  
                      bot.send_message(shat,"Captcha appears, try again."+nl+idds)
                      if loif<3:
                        try:
                            driver.quit() 
                        except  :
                            pass 
                        buy_user(idds,shat,codernum,loif+1,numper2,numper0)
                      else:
                          bot.send_message(shat,"Try charging the account after 10 minutes"+nl+idds)
                try:
                    driver.quit() 
                except  :
                        pass       
            except  :
                try:
                    driver.quit()
                except  :
                        pass
                pass 
        else :            
            bot.send_message(shat,"You do not have a code to charge the account  :  "+nl+idds+nl+codernum)            
      
# buy_user("5602807901",1153960679,"60")
    # try:
    #     error_3 = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '//div[@class="redeem-box error"] //p[1]')))
    
    #     print(error_3.text)
    # except   TimeoutExcept  ion:
    #     pass
    # 
    # # except  :
    #     print("err404")
    #     pass    
        
# for i in range(1,10):
#     print(i)
