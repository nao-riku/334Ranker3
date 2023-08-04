import chromedriver_binary
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import threading
import time
import datetime
import json
import copy
import os
import sys
import traceback

post_url = ""
post_body = {}
today_result = {}
world_rank = {}
load_res_yet = True
timeline_body = {}
getuser_url = ""
getuser_body = {}
ada_url = ""
ada_body = {}
not_url = ""
not_body = {}

start_now = datetime.datetime.now()
start_time = ""
end_time = ""


def tweet(driver):
    global post_body, post_url
    for _ in range(5):
        try:
            driver.get('https://twitter.com/Rank334_2/status/1624490398730321920')
            try:
                element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[role=textbox]")))
            except:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[href='/login']")))
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, "[href='/login']").click()
                time.sleep(20)
                driver.get('https://twitter.com/Rank334_2/status/1624490398730321920')
                element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[role=textbox]")))
            time.sleep(1)

            element_box = driver.find_element(By.CSS_SELECTOR, "[role=textbox]")
            element_box.send_keys("a")
            time.sleep(2) 
            
            driver.find_element(By.CSS_SELECTOR, "[data-testid=tweetButtonInline]").click()
            time.sleep(20)


            for _ in range(5):
                for request in driver.requests:
                    if request.response:
                        if "CreateTweet" in request.url:
                            post_url = request.url
                            post_body2 = json.loads(request.body)
                            time.sleep(0.5)
                            if "variables" in post_body2:
                                post_body = post_body2
                                print("set post_body")
                                break
                if post_body != {}:
                    break
                time.sleep(0.5)
                    

            time.sleep(3)

        except Exception as e:
            traceback.print_exc()
            time.sleep(2)
        else:
            break
	
    

def login_twitter(account, password, tel, driver):
    global timeline_body, getuser_body, getuser_url, ada_url, ada_body, not_url, not_body
    for _ in range(5):
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
            time.sleep(20)

            element_pass = driver.find_elements(By.TAG_NAME, "input")[1]
            for i in range(len(password)):
                time.sleep(1)
                act.send_keys(password[i])
                act.perform()
            time.sleep(2)
            element_pass.send_keys(Keys.ENTER)
            time.sleep(20)

            element_tel = driver.find_elements(By.NAME, "text")
            if len(element_tel) > 0:
                element_tel[0].send_keys(tel)
                time.sleep(2) 
                element_tel[0].send_keys(Keys.ENTER)
                time.sleep(20)

            driver.get('https://twitter.com/home')
            time.sleep(20)
            
            for _ in range(5):
                for request in driver.requests:
                    if request.response:
                        if "Timeline" in request.url and "graphql" in request.url:
                            if request.body != b'':
                                timeline_body2 = json.loads(request.body)
                                time.sleep(0.5)
                                if "variables" in timeline_body2:
                                    timeline_body = timeline_body2
                                    print("set timeline_body")
                                    break
                            else:
                                timeline_body2 = request.params
                                time.sleep(0.5)
                                if "variables" in timeline_body2:
                                    timeline_body = timeline_body2
                                    timeline_body["variables"] = json.loads(timeline_body["variables"])
                                    timeline_body["features"] = json.loads(timeline_body["features"])
                                    print("set timeline_body")
                                    break
                if timeline_body != {}:
                    break
                time.sleep(0.5)
		
            driver.get('https://twitter.com/intent/user?user_id=1')
            time.sleep(20)
            
            for _ in range(5):
                for request in driver.requests:
                    if request.response:
                        if "UserByRestId" in request.url and "graphql" in request.url:
                            getuser_url = request.url
                            if request.body != b'':
                                getuser_body2 = json.loads(request.body)
                                time.sleep(0.5)
                                if "variables" in getuser_body2:
                                    getuser_body = getuser_body2
                                    print("set getuser_body")
                                    break
                            else:
                                getuser_body2 = request.params
                                time.sleep(0.5)
                                if "variables" in getuser_body2:
                                    getuser_body = getuser_body2
                                    getuser_body["variables"] = json.loads(getuser_body["variables"])
                                    getuser_body["features"] = json.loads(getuser_body["features"])
                                    print("set getuser_body")
                                    break
                if getuser_body != {}:
                    break
                time.sleep(0.5)
                
            driver.get('https://twitter.com/search?q=%40Rank334_2&src=recent_search_click&f=live')
            time.sleep(20)
            
            for _ in range(5):
                for request in driver.requests:
                    if request.response:
                        if "adaptive.json" in request.url:
                            ada_url = request.url
                            if request.body != b'':
                                ada_body = json.loads(request.body)
                            else:
                                ada_body = request.params
                            print("set ada_body")
                            break
                if ada_body != {}:
                    break
                time.sleep(0.5)

            driver.get('https://twitter.com/notifications/mentions')
            time.sleep(20)
            
            for _ in range(5):
                for request in driver.requests:
                    if request.response:
                        if "mentions.json" in request.url:
                            not_url = request.url
                            if request.body != b'':
                                not_body = json.loads(request.body)
                            else:
                                not_body = request.params
                            print("set not_body")
                            break
                if not_body != {}:
                    break
                time.sleep(0.5)
                
            tweet(driver)
        
        except Exception as e:
            traceback.print_exc()
            time.sleep(2)
        else:
            break



def reply(req, driver):
    print("reply start", datetime.datetime.now())
    driver.execute_script("""
var url = arguments[0];
    
var cookie = document.cookie.replaceAll(" ", "").split(";");
var token = "";
cookie.forEach(function (value) {
    let content = value.split('=');
    if (content[0] == "ct0") token = content[1];
})

var xhr = new XMLHttpRequest();
xhr.open('POST', url);
xhr.setRequestHeader('Authorization', 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA');
xhr.setRequestHeader('x-csrf-token', token);
xhr.setRequestHeader('x-twitter-active-user', 'yes');
xhr.setRequestHeader('x-twitter-auth-type', 'OAuth2Session');
xhr.setRequestHeader('x-twitter-client-language', 'ja');
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.withCredentials = true;

var data = JSON.stringify(arguments[1]);
xhr.send(data);

""", post_url, req)



def TweetIdTime(id):
    epoch = ((id >> 22) + 1288834974657) / 1000.0
    d = datetime.datetime.fromtimestamp(epoch)
    return d


def TimeToStr(d):
    stringTime = ""
    stringTime += '{0:02d}'.format(d.hour)
    stringTime += ':'
    stringTime += '{0:02d}'.format(d.minute)
    stringTime += ':'
    stringTime += '{0:02d}'.format(d.second)
    stringTime += '.'
    stringTime += '{0:03d}'.format(int(d.microsecond / 1000))
    return stringTime



def receive(dict, driver):
    ranker_id = "1558892196069134337"
    ranker_id = "1556292536477843456"

    for item in dict:
	    
        if item["status"]["data"]["user"]["id_str"] != ranker_id:
            rep_text = False
            if item["status"]["data"]["in_reply_to_status_id_str"] == None:
                pass
            else:
                if item["status"]["data"]["in_reply_to_user_id_str"] == ranker_id:
                    pass
                else:
                    user_id = item["status"]["data"]["in_reply_to_user_id_str"]
                    user_name = ""
                    text_range = item["status"]["data"]["display_text_range"]
                    mentions = item["status"]["data"]["entities"]["user_mentions"]
                    flag = False 
                    for user in mentions:
                        if user["id_str"] == ranker_id and text_range[0] <= user["indices"][0] and user["indices"][1] <= text_range[1]:
                            flag = True
                        if user["id_str"] == user_id:
                            user_name = user["name"]
                    if flag:
                        if user_name == "":
                            pass
                        if rep_text == False:
                            orig_time = TweetIdTime(int(item["status"]["data"]["in_reply_to_status_id_str"]))
                            rep_text = "ツイート時刻：" + TimeToStr(orig_time)

            if rep_text != False:
                print(item["status"]["data"]["user"]["name"])
                req = copy.deepcopy(post_body)
                req["variables"]["reply"]["in_reply_to_tweet_id"] = item["status"]["data"]["id_str"]
                req["variables"]["tweet_text"] = rep_text
                threading.Thread(target=reply, args=(req, driver,)).start()



def interval(since, end, driver):
    driver.execute_script("""
console.log(arguments)
var cookie = document.cookie.replaceAll(" ", "").split(";");
var token = "";
cookie.forEach(function (value) {
    let content = value.split('=');
    if (content[0] == "ct0") token = content[1];
});
function setheader(xhr) {
    xhr.setRequestHeader('Authorization', 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA');
    xhr.setRequestHeader('x-csrf-token', token);
    xhr.setRequestHeader('x-twitter-active-user', 'yes');
    xhr.setRequestHeader('x-twitter-auth-type', 'OAuth2Session');
    xhr.setRequestHeader('x-twitter-client-language', 'ja');
    xhr.withCredentials = true;
}
window.adaptive = [];
let from = new Date(arguments[0] * 1000);
let until = new Date(arguments[1] * 1000);
let refresh = "";
let param = "?" + Object.entries(arguments[3]).map((e) => { return `${e[0]}=${encodeURIComponent(JSON.stringify(e[1]))}` }).join("&").replaceAll("%22", "");
let refresh2 = "";
let param2 = "?" + Object.entries(arguments[5]).map((e) => { return `${e[0]}=${encodeURIComponent(JSON.stringify(e[1]))}` }).join("&").replaceAll("%22", "");

let ada = setInterval(function (arguments) {
    get_adaptive("&cursor=" + refresh, arguments);
}, 3615, arguments);

let not = setInterval(function (arguments) {
    get_notifications("&cursor=" + refresh2, arguments);
}, 5028, arguments);

function get_adaptive(cursor, arguments) {
        let xhr = new XMLHttpRequest();
        let url = arguments[2].split("?")[0] + param + cursor;
        xhr.open('GET', url);
        xhr.timeout = 3000;
        get_tweets(cursor, xhr, true);
}

function get_notifications(cursor, arguments) {
    try {
        let xhr = new XMLHttpRequest();
        let url = arguments[4].split("?")[0] + param2 + cursor;
        xhr.open('GET', url);
        xhr.timeout = 4500;
        get_tweets(cursor, xhr, false);
    } catch { }
}

function get_tweets(cursor, xhr, isadaptive) {
    setheader(xhr);
    xhr.send();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let res = JSON.parse(xhr.responseText);
            let tweets = res.globalObjects.tweets;
            let users = res.globalObjects.users;
            let timelines = res.timeline.instructions;
            let timeline = [];
            for (let j = 0; j < timelines.length; j++) {
                if ("addEntries" in timelines[j]) timeline = timeline.concat(timelines[j].addEntries.entries);
                else if ("replaceEntry" in timelines[j]) timeline.push(timelines[j].replaceEntry.entry);
            }
            for (let i = 0; i < timeline.length; i++) {
                try {
                    if (!timeline[i].entryId.includes("cursor")) {
                        let id = timeline[i].content.item.content.tweet.id;
                        let tweet = tweets[id];
                        if (!tweet.full_text.toLowerCase().includes("@rank334_2")) continue;
                        if (new Date(tweet.created_at) < from) {
                            //console.log(adaptive);
                            //break;
                            continue;
                        }
                        if (until <= new Date(tweet.created_at)) {
                            if (isadaptive) clearInterval(ada);
                            else clearInterval(not);
                            continue;
                        }
                        tweet["user"] = users[tweet.user_id_str];
                        let status = {
                            "status": {
                                "data": tweet
                            }
                        }
                        window.adaptive.push(status);
                    } else if (timeline[i].entryId.includes("top")) {
                        if (isadaptive) refresh = timeline[i].content.operation.cursor.value;
                        else refresh2 = timeline[i].content.operation.cursor.value;
                    } else if (timeline[i].entryId.includes("bottom")) {
                        //get_adaptive("&cursor=" + timeline[i].content.operation.cursor.value);
                    }
                } catch {
                    if (i === timeline.length) {
                        //console.log(adaptive);
                    }
                }
            }
        }
    }
    xhr.ontimeout = function (e) {
        //get_adaptive(cursor);
    }
}
    """, int(since.timestamp()), int(end.timestamp()), ada_url, ada_body, not_url, not_body)
    while True:
        time.sleep(0.01)
        out = driver.execute_script("""
let adaptive = JSON.parse(JSON.stringify(window.adaptive));
window.adaptive = [];
return adaptive;
""")
        if out != []:
            threading.Thread(target=receive, args=(out, driver,)).start()
        else:
            if end + datetime.timedelta(seconds=10) < datetime.datetime.now():
                break


def start():
    global start_now, start_time, end_time
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
            time.sleep(2)
        else:
            break

            
    times = [
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 7, 20, 0)], #2:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 7, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 11, 20, 0)], #6:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 11, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 15, 20, 0)], #20:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 15, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 19, 20, 0)], #14:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 19, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 23, 20, 0)], #18:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 23, 20, 0), datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 20, 0) + datetime.timedelta(days=1)], #22:50
        [datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 20, 0) + datetime.timedelta(days=1), datetime.datetime(start_now.year, start_now.month, start_now.day, 3, 20, 0) + datetime.timedelta(days=1)]
    ]
    for i in range(len(times)):
        if start_now < times[i][0]:
            start_time = times[i][0]
            end_time = times[i][1]
            
            #login_twitter(os.environ['NAME'], os.environ['PASS'], os.environ['TEL'], driver)
            if len(sys.argv) != 1:
                start_time = datetime.datetime.now().replace(microsecond = 0) + datetime.timedelta(seconds=2)
                end_time = times[i][0]
            #threading.Thread(target=interval, args=(start_time, end_time, driver,)).start()
            
            break
         
threading.Thread(target=start).start()
            
