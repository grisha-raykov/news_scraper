from config import DATABASE_URL
from database.db_handler import DatabaseHandler
from scrapers.article_scrapers import (
    TrafilaturaArticleScraper,
    FeedparserArticleScraper,
)
from scrapers.scientific_american_scraper import ScientificAmericanScraper
from scrapers.stolica_scraper import StolicaArticleScraper


def main(save_to_db=False):
    scrapers = [
        # StolicaScraper(TrafilaturaArticleScraper()),
        ScientificAmericanScraper(FeedparserArticleScraper()),
    ]

    all_scraped_data = []

    for scraper in scrapers:
        try:
            scraped_data = scraper.scrape()
            all_scraped_data.extend(scraped_data)
            print(
                f"Scraped {len(scraped_data)} articles from {scraper.__class__.__name__}"
            )
        except Exception as e:
            print(
                f"Error occurred while scraping {scraper.__class__.__name__}: {str(e)}"
            )

    if save_to_db:
        db_handler = DatabaseHandler(DATABASE_URL)
        for article in all_scraped_data:
            db_handler.insert_article(**article)
        db_handler.close_connection()
        print(f"Saved {len(all_scraped_data)} articles to the database")
    else:
        print(
            f"Scraped a total of {len(all_scraped_data)} articles (not saved to database)"
        )


if __name__ == "__main__":
    main(save_to_db=False)  # Set to True to enable saving to the database
