import requests
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
        self.b = Browser('chrome', incognito=True)#,headless=True)
    
    def find_product(self):
        url = '{}{}{}'.format(self.base, self.shop_ext, self.info['category'])
        self.debug_console(url)
        r = requests.get(url, timeout=5).text
        soup = bs4.BeautifulSoup(r, 'lxml')
        #self.debug_console(soup)
        temp_tuple = []
        temp_link = []

        for link in soup.find_all('a', href=True):
            temp_tuple.append((link['href'], link.text))
        #self.debug_console(temp_tuple) 
        for i in temp_tuple:
            if i[1] == self.info['product'] or i[1] == self.info['color']:
                temp_link.append(i[0])
        self.debug_console(temp_link)
        #self.final_link = list(set([x for x in temp_link if temp_link.count(x) == 2]))
        self.final_link = 'shop/tops-sweaters/x6vo2ze7i/nwszmv5ot'#temp_link[0]
        print(self.final_link)

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
        self.init_browser()
        self.find_product()
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
            'zip': '42152',
            'country': 'USA',
            'card': 'Credit Card',
            'number': '1234123412341234',
            'month': '09',
            'year': '2020',
            'ccv': '123'
            }
    bot = SupremeBot(True,**INFO)
    bot.main()
