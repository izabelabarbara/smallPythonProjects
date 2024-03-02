import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    results = []
    
    def __init__(self, site):
        self.site = site

    def scrape(self):
        """
        scrape URLs from the site.
        save the list of scraped URLs into a txt file.
        """
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parse = "html.parser"
        sp = BeautifulSoup(html, parse)
        
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                self.results.append(url)
                
        with open("beautifulSoup_scraperTemplate.txt", "a+") as f:
            f.write(str(self.results))

# Example URL
news = "https://www.bbh.com/us/en/bbh-who-we-are/bbh-news.html"
Scraper(news).scrape()
