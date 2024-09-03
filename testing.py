from random import randint
from time import sleep

import requests
from lxml import html
from trafilatura import fetch_url, extract, extract_metadata



def wait_random():
    sleep(randint(1, 5))


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.360",
}

sciamerican = "https://www.scientificamerican.com/platform/syndication/rss/"
url = "https://stolica.bg/dnes"
path = '//div[@class="wrapper"]/h3/a/@href'

# newsbg = NewsBg()
r = requests.get(url, headers=headers)
byte_data = r.content
source_code = html.fromstring(byte_data)
tree = source_code.xpath(path)
print(tree)
for t in tree:
    raw_article = fetch_url(t)
    article_metadata = extract_metadata(raw_article)
    article = extract(
        raw_article,
        include_links=True,
        include_comments=False,
        include_formatting=True,
        include_images=True,
    )
    print(article_metadata.title, article_metadata.date, "\n", article)
    # print(article_metadata.url, article_metadata.title, article_metadata.date)
    # db.insert_article(article_metadata.title, article_metadata.url, article)
    print("---------------------------------------------")
# db.close_connection()
# feed = feedparser.parse(sciamerican)
# print(feed.entries[0].title, feed.entries[0].link)
# downloaded = fetch_url(feed.entries[0].link)
# article = extract(downloaded, include_links=True, include_comments=False, include_formatting=True, include_images=True)
# print(article)
