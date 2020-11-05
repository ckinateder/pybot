import requests, json, bs4
from colorama import init
from colorama import Fore, Back, Style
from splinter import Browser

class Bot:
    def __init__(self, base, shop, checkout, debug, info):
        self.base = base
        self.shop_ext = shop
        self.checkout_ext = checkout
        self.info = info
        self.debug = debug

    def debug_console(self, out):
        if self.debug:
            print(out)

    def init_browser(self):
        self.b = Browser('chrome', incognito=True)#, headless=True)
    
    def find_matching_href(self, names, styles): #may be moved to supreme.py but not sure yet
        for i in names:
            for j in styles:
                if i['href'] == j['href']:
                    return i['href'] #they match
        return names[0]['href'] #default condition