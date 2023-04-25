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


# function for make request
def get_code(url) -> requests.Response:
    return requests.get(url)


# functions to get website scores
def linkbuttoncounter():
    counter = 0
    for link in soup.find_all('a'):
        counter += 1
    return counter


def imgcounter():
    counter = 0
    for link in soup.find_all('img'):
        counter += 1
    return counter


def divcounter():
    counter = 0
    for link in soup.find_all('div'):
        counter += 1
    return counter


def sectioncounter():
    counter = 0
    for link in soup.find_all('section'):
        counter += 1
    return counter


def metatagcounter():
    counter = 0
    for link in soup.find_all('meta'):
        counter += 1
    return counter


def linkcounter():
    counter = 0
    for link in soup.find_all('link'):
        counter += 1
    return counter


def paragraphcounter():
    counter = 0
    for link in soup.find_all('p'):
        counter += 1
    return counter


def buttoncounter():
    counter = 0
    for link in soup.find_all('button'):
        counter += 1
    return counter


def scriptcounter():
    counter = 0
    for link in soup.find_all('script'):
        counter += 1
    return counter


def h2counter():
    counter = 0
    for link in soup.find_all('h2'):
        counter += 1
    return counter


# INDEXING YOUR LARGE SITEMAPS ( input your site map url )
sitemap = adv.sitemap_to_df("https://ticapsoriginal.com/static/sitemaps2.xml")

# TYPE CASTING URL TO LIST
urls = sitemap["loc"].to_list()


# global declaration to access of total variables
global totallinkbuttons
global totalimgs
global totaldivs
global totalsections
global totalmetas
global totallinks
global totalparagraphs
global totalbuttons
global totalscripts
global totalh2

# initialization of total variables
totallinkbuttons = 0
totalimgs = 0
totaldivs = 0
totalsections = 0
totalmetas = 0
totallinks = 0
totalparagraphs = 0
totalbuttons = 0
totalscripts = 0
totalh2 = 0

# each url walking
for url in tqdm(urls):

    print(url)
    urlg = (get_code(url))
    soup = BeautifulSoup(urlg.text, 'html.parser')

    print("Number of link buttons : " + str(linkbuttoncounter()))
    print("Number of images : " + str(imgcounter()))
    print("Number of divs : " + str(divcounter()))
    print("Number of sections : " + str(sectioncounter()))
    print("Number of metatags : " + str(metatagcounter()))
    print("Number of links : " + str(linkcounter()))
    print("Number of paragraph : " + str(paragraphcounter()))
    print("Number of scripts : " + str(scriptcounter()))
    print("Number of buttons : " + str(buttoncounter()))
    print("Number of h2: " + str(h2counter()))

    totallinkbuttons += linkbuttoncounter()
    totalimgs += imgcounter()
    totaldivs += divcounter()
    totalsections += sectioncounter()
    totalmetas += metatagcounter()
    totallinks += linkcounter()
    totalparagraphs += paragraphcounter()
    totalbuttons += buttoncounter()
    totalscripts += scriptcounter()
    totalh2 += h2counter()


# print of total scores
print(" \n\n")
print("Number total of link buttons : " + totallinkbuttons)
print("Number total of images: " + totalimgs)
print("Number total of divs: " + totaldivs)
print("Number total of sections: " + totalsections)
print("Number total of metatags: " + totalmetas)
print("Number total of links: " + totallinks)
print("Number total of paragraphs buttons: " + totalparagraphs)
print("Number total of buttons: " + totalbuttons)
print("Number total of scripts: " + totalscripts)
print("Number total of h2 subtitles: " + totalh2)

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
webscores = [totallinkbuttons,
             totalimgs,
             totaldivs,
             totalsections,
             totalmetas,
             totallinks,
             totalparagraphs,
             totalbuttons,
             totalscripts,
             totalh2]

# PLOTTING WEBSITE SITEMAPS SCORE CHART
plt.figure(figsize=(10, 5))
plt.plot(totaldivs)
plt.bar(websitemetrics, webscores)
plt.suptitle('WEBSITE OVERVIEW ')
plt.show()
