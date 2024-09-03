from scrapers.article_scrapers import Goose3ArticleScraper


class NewsbgArticleScraper:
    def __init__(self):

        self.article_scraper = Goose3ArticleScraper()

    def scrape(self, urls):
        scraped_data = []

        for url in urls:
            article_data = self.article_scraper.scrape(url)
            scraped_data.append(article_data)

        return scraped_data


s = NewsbgArticleScraper().scrape(
    [
        "https://news.bg/bulgaria/prevozvachi-zaobikalyat-balgariya-zaradi-darzhavnite-tapi-po-granitsite.html"
    ]
)
print(s)
