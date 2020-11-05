import supreme, bot

if __name__ == '__main__':
    INFO = {
            'product': 'Spray Hooded Sweatshirt',
            'color': 'White',
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
    bot = supreme.SupremeBot(False,**INFO)
    bot.main()
    #bot.find_product()