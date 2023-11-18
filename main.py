import chromedriver_binary
from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import json
import os
import traceback
from linebot import LineBotApi
from linebot.models import ImageSendMessage
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

def TweetIdTime(id):
    epoch = ((id >> 22) + 1288834974657) / 1000.0
    d = datetime.datetime.fromtimestamp(epoch)
    return d

def login_twitter(account, password, tel, driver):
    global timeline_body, search_body
    for _ in range(2):
        try:
            driver.get('https://nao-riku.github.io/334Ranker3/')
            time.sleep(1)
            driver.get_screenshot_as_file("a.png")
            

        except Exception as e:
            traceback.print_exc()
        else:
            break


def start():
    for _ in range(3):
        try:
            options=Options()
            #options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options = options)
            
        except Exception as e:
            traceback.print_exc()
        else:
            break

    login_twitter("334ranking", os.environ['PASS'], os.environ['TEL'], driver)
         
start()
