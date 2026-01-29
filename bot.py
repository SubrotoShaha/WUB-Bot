import os
import requests
import xml.etree.ElementTree as ET

# গিটহাব সিক্রেট থেকে তথ্য নেওয়া হচ্ছে
BOT_TOKEN = os.environ.get('BOT_TOKEN')
RSS_URL = os.environ.get('RSS_URL')
CHAT_ID = "@WUBVarsityAlert"

def check_and_notify():
    try:
        response = requests.get(RSS_URL)
        tree = ET.fromstring(response.content)
        item = tree.find('.//item')
        if item is not None:
            title = item.find('title').text
            link = item.find('link').text
            
            msg = f"নতুন আপডেট এসেছে!\n\nশিরোনাম: {title}\nলিঙ্ক: {link}"
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
            requests.get(url)
            print("Message sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

if _name_ == "_main_":
    check_and_notify()
