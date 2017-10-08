import sys
from flask_pymongo import pymongo #ylk
from bson.json_util import dumps
import requests  # to make GET request
from bs4 import BeautifulSoup  # to parse the HTML response
import re
from flask import Flask, render_template

app = Flask(__name__)

uri = 'mongodb://ashleychien:apricot12@ds147454.mlab.com:47454/cal-hacks' 

 
@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route('/api/v1/loadimages/<int:lastindex>/') 
def load_images(lastindex):
	client = pymongo.MongoClient(uri, connect=False)
	db = client.get_default_database()
	img = db['test']
	print "sad"
	return dumps(img.find({}))
    #get mongodb results as a json array

	# return arr

#ashley's code
"""
def main(args):
    client = pymongo.MongoClient(uri, connect=False)
    db = client.get_default_database()
    songs = db['test']
    client.close()"""


if __name__ == '__main__':
    #main(sys.argv[1:]) #new
    app.run()
