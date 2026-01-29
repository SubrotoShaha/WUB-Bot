import requests
import xml.etree.ElementTree as ET
import time

BOT_TOKEN = "8474117716:AAHWG_9q78s3NJXTx-fkpo2kx30jJXRcFFE"
CHAT_ID = "@WUBVarsityAlert"
RSS_URL = "https://rss.app/feeds/U3qHFNFcf1bURQsM.xml"

def check_and_notify():
    response = requests.get(RSS_URL)
    tree = ET.fromstring(response.content)
    item = tree.find('.//item')
    title = item.find('title').text
    link = item.find('link').text
    
    msg = f"নতুন আপডেট এসেছে!\n\nশিরোনাম: {title}\nলিঙ্ক: {link}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    requests.get(url)
    print("নোটিফিকেশন পাঠানো হয়েছে!")

while True:
    check_and_notify()
    time.sleep(3600)