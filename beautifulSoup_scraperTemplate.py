import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parse = "html.parser"
        sp = BeautifulSoup(html, parse)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://www.bbh.com/us/en/bbh-who-we-are/bbh-news.html"
Scraper(news).scrape()
