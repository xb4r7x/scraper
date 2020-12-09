from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests
import json
import time
#from requests_html import HTMLSession, AsyncHTMLSession
#import time
#import re

#import ./config

base_url = 'https://www.vancafe.com/HS2211-p/hs2211.htm'

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

loopcount = 0
while True:
    loopcount += 1
    stock_status = check_available(base_url)

    if stock_status == 0:
        if loopcount % 720 == 0:
            notify_slack("Item is not yet in stock. {}".format(base_url))
    if stock_status == 1:
        notify_slack("HOLY CRAP IT'S AVAILABLE DROP WHAT YOU'RE DOING {}".format(base_url))     
        break
    
    time.sleep(5)
