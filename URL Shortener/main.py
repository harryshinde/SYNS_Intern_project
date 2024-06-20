# pip install pyshorteners
# pip install pyperclip

import pyshorteners

url = input('Enter the link : ')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print("Shortener Link : ",s.tinyurl.short(url))

shortenurl(url)