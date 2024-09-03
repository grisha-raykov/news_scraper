class NewsBg:
    def __init__(self):
        self.url = 'https://news.bg'
        self.today_news = 'https://news.bg/today'
        self.today_news_xpath = '//ul[@class="secondary-articles"]/li/div/a/@href'
