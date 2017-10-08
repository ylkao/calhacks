import sys
import pymongo
import requests  # to make GET request
from bs4 import BeautifulSoup  # to parse the HTML response
import re

uri = 'mongodb://ashleychien:apricot12@ds147454.mlab.com:47454/cal-hacks'
i = 0

def main(args):

    client = pymongo.MongoClient(uri, connect=False)

    db = client.get_default_database()
    cat = soupy('https://www.brainyquote.com/quotes/topics/topic_positive.html')
    dog = soupy('https://www.brainyquote.com/quotes/topics/topic_motivational.html')
    bird = soupy('https://www.brainyquote.com/quotes/topics/topic_courage.html')
    pigeon = soupy('https://www.brainyquote.com/quotes/topics/topic_happiness.html')
    meow = soupy('https://www.brainyquote.com/quotes/topics/topic_jokes.html')
    ruff = soupy('https://www.brainyquote.com/quotes/topics/topic_humor.html')
    insp = soupy('https://www.brainyquote.com/quotes/topics/topic_inspirational.html')


    songs = db['quotes']
    songs.insert_many(cat)
    songs.insert_many(dog)
    songs.insert_many(bird)
    songs.insert_many(pigeon)
    songs.insert_many(meow)
    songs.insert_many(ruff)
    songs.insert_many(insp)
    # First we'll add a few songs. Nothing is required to create the songs 
    # collection; it is created automatically when we insert.
    print("Hi")
    client.close()

def soupy(link):
	global i
	# make a GET request
	response = requests.get(link)
	# read the content of the server’s response as a string
	page_source = response.text
	soup = BeautifulSoup(page_source, 'html.parser')
	arr = []
	for thing in soup("a", class_ = "oncl_q"):
		thing = str(thing)
		try:
			num = thing.index("img alt")
			end_index = thing.index('class=" zoomc bqpht"')
			arr += [thing[(num+9):end_index-2]]
		except:
			pass

	hold = []
	for t in arr:
		hold += [{str(i): t}]
		i += 1
	return hold

if __name__ == '__main__':
    main(sys.argv[1:])