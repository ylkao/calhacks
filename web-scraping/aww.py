import sys
import pymongo
import requests  # to make GET request
from bs4 import BeautifulSoup  # to parse the HTML response
import re

uri = 'mongodb://ashleychien:apricot12@ds147454.mlab.com:47454/cal-hacks' 


def main(args):

    client = pymongo.MongoClient(uri, connect=False)

    db = client.get_default_database()
    cat = soupy()
    songs = db['aww']
    songs.insert_many(cat)
    # First we'll add a few songs. Nothing is required to create the songs 
    # collection; it is created automatically when we insert.
    print("Hi")
    client.close()


def helper(url):
    response = requests.get(url)
    page_source = response.text
    soup = BeautifulSoup(page_source, 'html.parser')

    p = re.compile('^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg|gif|png)$', re.IGNORECASE)
    holder = []

    for link in soup.find_all('a'):
        if p.match(str(link.get('href'))) != None:
            holder += [link.get('href')]

    return holder



def soupy():
    aww = helper("http://www.reddit.com/r/aww")
    cats = helper("http://www.reddit.com/r/cats")
    dogs = helper("http://www.reddit.com/r/dogs")
    catsStanding = helper("http://www.reddit.com/r/catsstandingup")

    allCute = aww + cats + dogs + catsStanding	

    no_duplicates = allCute[::2]

    hold=[]
    i = 0
    for thing in no_duplicates:
        hold += [{str(i): thing}]
        i += 1
    return hold

if __name__ == '__main__':
    main(sys.argv[1:])