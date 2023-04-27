# IMPORT BEAUTIFULSOUP TO READ WEB CONTENT
from bs4 import BeautifulSoup

# IMPORT URLIB TO PARSE URL DATA
from urllib.parse import quote

# IMPORT MATPLOT TO PLOTTING CHART
import matplotlib.pyplot as plt

# IMPORT TQDM TO SEE PROGRESS BAR
from tqdm import tqdm

# IMPORT FUNCTIONS
from functions import get_code

# TAGS LIST
global tagmanager
tagmanager = {'a': 0, 'img': 0, 'div': 0, 'section': 0, 'meta': 0,
              'link': 0, 'p': 0, 'button': 0, 'script': 0, 'h2': 0}

sitemap = "https://ticapsoriginal.com/static/sitemaps2.xml"
urll = []
urll += BeautifulSoup((get_code(sitemap)).text, 'html.parser').find_all('loc')


# UPTADE TAGMANAGER
def updatetagmanager(soup, tag):
    tagmanager[tag] += (len(soup.find_all(tag)))


# EACH URL WALKING
for url in tqdm(urll):
    print(url)
    urlg = (get_code(str(url).replace("<loc>", " ").replace("</loc>", " ")))
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
