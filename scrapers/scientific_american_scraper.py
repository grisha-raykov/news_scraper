from scrapers.article_scrapers import (
    TrafilaturaArticleScraper,
    NewsPleaseArticleScraper,
)


class ScientificAmericanScraper:
    def __init__(self, article_scraper=None):
        self.article_scraper = article_scraper or NewsPleaseArticleScraper()

    def scrape(self, urls):
        scraped_data = []
        for url in urls:
            article_data = self.article_scraper.scrape(url)
            scraped_data.append(article_data)

        return scraped_data


s = ScientificAmericanScraper()
a = s.scrape(
    [
        "https://www.scientificamerican.com/article/ai-surveillance-pricing-practices-under-federal-probe/"
    ]
)
print(a)
