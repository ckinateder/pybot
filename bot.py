import requests
import bs4
from splinter import Browser

class SupremeBot:
    def __init__(self, **info):
        self.base = "http://supremenewyork.com/"
        self.shop_ext = "shop/all/"
        self.checkout_ext = "checkout/"
        self.info = info

    def init_browser(self):
        self.b = Browser()
    
    def find_product(self):
        r = requests.get("{}{}{}".format(self.base, self.shop, self.info["category"])).text
        soup = bs4.BeautifulSoup(r, 'lxml')

if __name__ == "__main__":
    INFO = {
            "driver": "geckodriver",
            "product": "Thermal Zip Up Hooded Sweatshirt",
            "color": "Tangerine",
            "size": "Medium",
            "category": "sweatshirts",
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
