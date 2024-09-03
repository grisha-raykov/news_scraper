from scrapers.article_scrapers import TrafilaturaArticleScraper
from lxml import html
import requests
from config import HEADERS


class StolicaArticleScraper:
    def __init__(self, article_scraper=None):
        self.article_scraper = TrafilaturaArticleScraper()

    def scrape(self, urls):
        scraped_data = []

        for url in urls:
            article_data = self.article_scraper.scrape(url)
            article_data["source"] = "Stolica.bg"
            scraped_data.append(article_data)

        return scraped_data
