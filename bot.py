import requests
import json
from colorama import init
from colorama import Fore, Back, Style
import bs4
from splinter import Browser

class SupremeBot:
    def __init__(self, debug=False, **info):
        self.base = 'https://www.supremenewyork.com/'
        self.shop_ext = 'shop/all/'
        self.checkout_ext = 'checkout/'
        self.info = info
        self.debug = debug

    def debug_console(self, out):
        if self.debug:
            print(out)

    def init_browser(self):
        self.b = Browser('chrome', incognito=True)#, headless=True)
    
    def get_pids_prelaunch(self):
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'If-None-Match': '"MnhlSMUKPPVW1gPfswixCrrWB9Y="',
        }

        response = requests.get(self.base+'shop.json', headers=headers)
        a = json.loads(response.text)

        products = a['products_and_categories']

        fname = 'pids'
        print(Fore.CYAN + "Scraping...")
        print(Fore.WHITE)

        f = open('{}.txt'.format(fname),"w")
        f.truncate()

        for product in products['new']:
            pid = product['id']
            pname = product['name']
            pcategory = product['category_name']
            f.write(str(pid) + "\n")
            print(str(pid) + " - "+ str(pname) + " - " + str(pcategory))

    def find_product(self):
        page = requests.get(self.base+self.shop_ext+self.info['category'])
        if page.status_code == 200:
            soup = bs4.BeautifulSoup(page.content, 'html.parser')
            # look for class 'name-link'
            for i in soup.select("div.product-name a.name-link"):
                print(str(i))
        else:
            print('error: recieved response code', page.status_code)


    def visit_site(self):
        self.b.visit('{}{}'.format(self.base, str(self.final_link)))
        self.b.find_option_by_text(self.info['size']).click()
        self.b.find_by_value('add to cart').click()
        self.b.visit('{}{}'.format(self.base, self.checkout_ext))
    
    def checkout_func(self):
        self.b.visit('{}{}'.format(self.base, self.checkout_ext))
        #self.debug_console('{}{}'.format(self.base, self.checkout_ext))
        #self.debug_console(self.b.execute_script("return document.documentElement.outerHTML;"))

        self.b.fill('order[billing_name]', self.info['namefield'])
        self.b.fill('order[email]', self.info['emailfield'])
        self.b.fill('order[tel]', self.info['phonefield'])

        self.b.fill('order[billing_address]', self.info['addressfield'])
        self.b.fill('order[billing_city]', self.info['city'])
        self.b.select('order[billing_state]', self.info['state'])
        self.b.fill('order[billing_zip]', self.info['zip'])
        self.b.select('order[billing_country]', self.info['country'])

        #self.b.select('credit_card[type]', self.info['card'])
        self.b.fill('riearmxa', self.info['number'])
        self.b.select('credit_card[month]', self.info['month']) #wierd name
        self.b.select('credit_card[year]', self.info['year'])
        self.b.fill('credit_card[meknk]', self.info['ccv']) #wierd name
        self.b.find_by_css('.terms').click()
        #self.b.find_by_value('process payment').click()

    def main(self):
        #self.get_pids_prelaunch()
        self.find_product()
        self.init_browser()
        self.visit_site()
        self.checkout_func()


if __name__ == '__main__':
    INFO = {
            'product': 'Thermal Zip Up Hooded Sweatshirt',
            'color': 'Tangerine',
            'size': 'Medium',
            'category': 'sweatshirts',
            'namefield': 'example',
            'emailfield': 'example@example.com',
            'phonefield': 'XXXXXXXXXX',
            'addressfield': 'example road',
            'city': 'cincinnati',
            'state': 'OH',
            'zip': '45219',
            'country': 'USA',
            'card': 'Credit Card',
            'number': '1234123412341234',
            'month': '09',
            'year': '2020',
            'ccv': '123'
            }
    bot = SupremeBot(False,**INFO)
    #bot.main()
    bot.find_product()