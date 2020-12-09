from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests
import json
import time

import config

base_url = 'https://www.vancafe.com/HS2211-p/hs2211.htm'
checkout_url = 'https://www.vancafe.com/one-page-checkout.asp'

def check_available(base_url):
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find(itemprop="offers").get_text()
    if "Out" in div:
        return 0
    else:
        return 1
   
def notify_slack(message):
    webhook_url = 'https://hooks.slack.com/services/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'
    payload = {'text': message}
    
    response = requests.post(
        webhook_url, data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )

def purchase_heater(base_url, checkout_url):
    driver = webdriver.Chrome()
    driver.get(base_url)
    btn = driver.find_element_by_class_name('addcartbtns').find_elements_by_name('btnaddtocart')
    btn[0].click()
   
    time.sleep(1)    

    driver.get(checkout_url)

    time.sleep(5)
    
    driver.find_element_by_name('BillingFirstName').send_keys(config.FIRSTNAME)
    driver.find_element_by_name('BillingLastName').send_keys(config.LASTNAME)
    driver.find_element_by_name('BillingAddress1').send_keys(config.ADDRESS)
    driver.find_element_by_name('BillingCity').send_keys(config.CITY)
    
    select = Select(driver.find_element_by_name('BillingState_dropdown'))
    select.select_by_visible_text(config.STATE)

    driver.find_element_by_name('BillingPostalCode').send_keys(config.ZIP)
    driver.find_element_by_name('BillingPhoneNumber').send_keys(config.PHONE)
    driver.find_element_by_name('Email').send_keys(config.EMAIL)
    driver.find_element_by_name('emailsubscriber').click()    
    driver.find_element_by_name('password').send_keys(config.PASSWORD)    
    driver.find_element_by_name('passwordagain').send_keys(config.PASSWORD)
    
    driver.find_element_by_name('ShipResidential').click()
    time.sleep(5)
    select = Select(driver.find_element_by_name('ShippingSpeedChoice'))
    select.select_by_value('1098')

    time.sleep(5)

    driver.find_element_by_id('CreditCard').click()
    time.sleep(5)

    iframe = driver.find_element_by_id('paymentFrame')
    driver.switch_to.frame(iframe)

    time.sleep(5)

    select = Select(driver.find_element_by_id('CreditCardType'))
    select.select_by_value('6')   

    driver.find_element_by_name('CardHoldersName').send_keys(config.CCNAME)
    driver.find_element_by_name('CreditCardNumber').send_keys(config.CCNUMBER)
    
    select = Select(driver.find_element_by_id('CC_ExpDate_Month'))
    select.select_by_value(config.CCEXPMONTH)

    select = Select(driver.find_element_by_id('CC_ExpDate_Year'))
    select.select_by_value(config.CCEXPYEAR)
 
    driver.find_element_by_id('CVV2').send_keys(config.CCCVV)

    driver.switch_to.default_content()

    driver.find_element_by_name('Orders.Custom_Field_Terms').click()
    driver.find_element_by_id('imgSubmitOrder').click()

    time.sleep(28800)

loopcount = 0
while True:
    loopcount += 1
    stock_status = check_available(base_url)

    if stock_status == 0:
        if loopcount % 720 == 0:
            print(loopcount) 
            notify_slack("Item is not yet in stock. {}".format(base_url))
    if stock_status == 1:
        notify_slack("HOLY CRAP IT'S AVAILABLE! PURCHASING AUTOMATICALLY - GO VERIFY PURCHASE {}".format(base_url))    
        purchase_heater(base_url, checkout_url)
        break
    
    time.sleep(5)
