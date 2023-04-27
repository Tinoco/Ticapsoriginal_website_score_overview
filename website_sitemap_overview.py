# IMPORT BEAUTIFULSOUP TO READ WEB CONTENT
from bs4 import BeautifulSoup

# IMPORT REQUESTS TO RECEIVE RESPONSES
import requests

# IMPORT URLIB TO PARSE URL DATA
from urllib.parse import quote

# IMPORT ADVERTOOLS TO READ LARGE SITEMAPS
import advertools as adv

# IMPORT MATPLOT TO PLOTTING CHART
import matplotlib.pyplot as plt

# IMPORT TQDM TO SEE PROGRESS BAR
from tqdm import tqdm

# TAGS LIST
global tagmanager
tagmanager = {'a': 0, 'img': 0, 'div': 0, 'section': 0, 'meta': 0,
              'link': 0, 'p': 0, 'button': 0, 'script': 0, 'h2': 0}

# INDEXING YOUR LARGE SITEMAPS ( input your site map url )
sitemap = adv.sitemap_to_df("https://ticapsoriginal.com/static/sitemaps2.xml")

# TYPE CASTING URL TO LIST
urls = sitemap["loc"].to_list()


# FUNCRION TO MAKE REQUEST
def get_code(url) -> requests.Response:
    return requests.get(url)


# UPTADE TAGMANAGER
def updatetagmanager(soup, tag):
    totalcounter = 0
    counter = 0
    for link in soup.find_all(tag):
        counter += 1
    totalcounter += counter
    tagmanager[tag] += totalcounter


# EACH URL WALKING
for url in tqdm(urls):
    print(url)
    urlg = (get_code(url))
    soup = BeautifulSoup(urlg.text, 'html.parser')
    for item in tagmanager:
        updatetagmanager(soup, item)

# CHART METRICS E VALUES
websitemetrics = ['linkbuttons ',
                  'images ',
                  'divs ',
                  'sections ',
                  'metatags ',
                  'links ',
                  'paragraphs ',
                  'buttons ',
                  'scripts ',
                  'h2 ']
webscores = list(tagmanager.values())

# PLOTTING WEBSITE SITEMAPS SCORE CHART
plt.figure(figsize=(10, 5))
plt.plot(tagmanager['div'])
plt.bar(websitemetrics, webscores)
plt.suptitle('WEBSITE OVERVIEW SCORES')
plt.show()
