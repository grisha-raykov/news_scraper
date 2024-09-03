from abc import ABC, abstractmethod
from trafilatura import fetch_url, extract, extract_metadata
from trafilatura.settings import use_config
from models.article import Article
from utils.helpers import wait_random
from config import USER_AGENT
from goose3 import Goose
from newsplease import NewsPlease
import json
import subprocess


class TrafilaturaArticleScraper:
    def __init__(self, user_agent=None):
        self.user_agent = user_agent or USER_AGENT
        # Set the user agent in Trafilatura's configuration
        config = use_config()
        config.set("DEFAULT", "USER_AGENT", self.user_agent)

    def scrape(self, url) -> Article:
        wait_random()
        raw_content = fetch_url(url)
        metadata = extract_metadata(raw_content)
        content = extract(
            raw_content,
            include_links=True,
            include_comments=False,
            include_formatting=True,
            include_images=True,
        )

        return Article(
            title=metadata.title,
            url=url,
            content=content,
            date=metadata.date,
            author=metadata.author,
            description=metadata.description,
            language=metadata.language,
        )


class Goose3ArticleScraper:
    def __init__(self, user_agent=None):
        self.user_agent = user_agent or USER_AGENT
        self.goose = Goose({"browser_user_agent": self.user_agent})

    def scrape(self, url) -> Article:
        wait_random()
        article = self.goose.extract(url)
        return Article(
            title=article.title,
            url=url,
            content=article.cleaned_text,
            date_published=article.publish_date,
            author=article.authors,
            language=article.meta_lang,
            description=article.meta_description,
        )


class NewsPleaseArticleScraper:
    def __init__(self, user_agent=None):
        self.user_agent = user_agent or USER_AGENT
        self.newsplease = NewsPlease()

    def scrape(self, url) -> Article:
        wait_random()
        article = self.newsplease.from_url(url)
        return Article(
            title=article.title,
            url=url,
            content=article.maintext,
            language=article.language,
        )


class ReadabilityArticleScraper:
    def __init__(self, user_agent=None):
        self.user_agent = user_agent or USER_AGENT

    def scrape(self, url):
        wait_random()
        result = subprocess.run(
            ["node", "readability_wrapper.js", url], capture_output=True, text=True
        )

        try:
            data = json.loads(result.stdout)
            if "error" in data:
                raise Exception(data["error"])

            return {
                "title": data["title"],
                "url": url,
                "content": data["content"],
                "text_content": data["textContent"],
                "length": data["length"],
                "description": data["excerpt"],
            }
        except json.JSONDecodeError:
            raise Exception("Failed to parse JSON output from Node.js script")
