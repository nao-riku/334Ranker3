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
            driver.get('https://twitter.com/i/flow/login')
            driver.maximize_window()
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "text")))
            time.sleep(1)
            
            act = ActionChains(driver)
            
            element_account = driver.find_element(By.TAG_NAME, "input")
            element_account.send_keys("")
            for i in range(len(account)):
                time.sleep(1)
                act.send_keys(account[i])
                act.perform()
            time.sleep(2)
            element_account.send_keys(Keys.ENTER)
            time.sleep(10)

            element_pass = driver.find_elements(By.TAG_NAME, "input")[1]
            for i in range(len(password)):
                time.sleep(1)
                act.send_keys(password[i])
                act.perform()
            time.sleep(2)
            #element_pass.send_keys(Keys.ENTER)
            act.send_keys(Keys.ENTER)
            act.perform()
            time.sleep(10)

            element_tel = driver.find_elements(By.TAG_NAME, "input")
            if len(element_tel) > 0:
                for i in range(len(tel)):
                    time.sleep(1)
                    act.send_keys(tel[i])
                    act.perform()
                time.sleep(2) 
                act.send_keys(Keys.ENTER)
                act.perform()
                #driver.find_element(By.CSS_SELECTOR, "[data-testid=ocfEnterTextNextButton]").click()
                time.sleep(10)
                
            time.sleep(3)
            driver.get('https://twitter.com/rank334')
            time.sleep(10)
            driver.get_screenshot_as_file("a.png")
            
            
            for request in driver.requests:
                    if request.response:
                        if "UserTweets" in request.url and "graphql" in request.url:
                            j = json.loads(decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')))
                            url = j['data']['user']['result']['timeline_v2']['timeline']['instructions'][2]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]['media_url_https']
                            dt = TweetIdTime(int(j['data']['user']['result']['timeline_v2']['timeline']['instructions'][2]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['id_str']))
                            line_bot_api = LineBotApi(os.environ['KEY'])
                            line_bot_api.push_message(os.environ['ID'], ImageSendMessage(original_content_url=url, preview_image_url=url))        
                            line_bot_api.push_message(os.environ['ID'], TextSendMessage(text=dt.strftime('%Y/%m/%d %H:%M:%S'))
                            line_bot_api.push_message(os.environ['ID'], TextSendMessage(text=str(datetime.datetime.now()-dt)[:-7] + "前"))

                            break
            time.sleep(0.5)

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

    time.sleep(1)
    login_twitter("334ranking", os.environ['PASS'], os.environ['TEL'], driver)
         
start()
