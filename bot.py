import requests
import bs4
from splinter import Browser

class SupremeBot:
    def __init__(self, debug=False, **info):
        self.base = "https://www.supremenewyork.com/"
        self.shop_ext = "shop/all/"
        self.checkout_ext = "checkout/"
        self.info = info
        self.debug = debug

    def debug_console(self, out):
        if self.debug:
            print(out)

    def init_browser(self):
        self.b = Browser("chrome")
    
    def find_product(self):
        url = "{}{}{}".format(self.base, self.shop_ext, self.info["category"])
        self.debug_console(url)
        r = requests.get(url, timeout=5).text
        soup = bs4.BeautifulSoup(r, 'lxml')
        #self.debug_console(soup)
        temp_tuple = []
        temp_link = []

        for link in soup.find_all("a", href=True):
            temp_tuple.append((link["href"], link.text))
        #self.debug_console(temp_tuple) 
        for i in temp_tuple:
            if i[1] == self.info["product"] or i[1] == self.info["color"]:
                temp_link.append(i[0])
        self.debug_console(temp_link)
        #self.final_link = list(set([x for x in temp_link if temp_link.count(x) == 2]))
        print(temp_link[0])
    
    
if __name__ == "__main__":
    INFO = {
            "product": "S/S Pocket Tee",
            "color": "Black",
            "size": "Medium",
            "category": "tops_sweaters",
            "namefield": "example",
            "emailfield": "example@example.com",
            "phonefield": "XXXXXXXXXX",
            "addressfield": "example road",
            "city": "example",
            "zip": "42155",
            "country": "US",
            "card": "visa",
            "number": "1234123412341234",
            "month": "09",
            "year": "2020",
            "ccv": "123"
            }
    bot = SupremeBot(True,**INFO)
    bot.find_product()
