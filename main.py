from whoosh.qparser import *
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED, NUMERIC
from whoosh.analysis import StemmingAnalyzer, StandardAnalyzer
from whoosh import index
from whoosh.index import create_in
import os, os.path
import json
from pydf import myPaper
from pydf import db

db.create_all()

file_dir = '/Users/tony/Desktop/search_engine/filedir/'
file_name = os.listdir(file_dir)
print(len(file_name))

# reading files and put them into database
file_load = json.load(open('/Users/tony/Desktop/search_engine/filedir/arxivData.json', 'r'))
for i in range(len(file_load)):
    if (i%1000) == 0: 
        print("%s files loaded" % (i))

    new_input = myPaper(
                        id = file_load[i]['id'],
                        title = file_load[i]['title'],
                        abstract=file_load[i]['summary'],
                        author=file_load[i]['author'],
                        link=file_load[i]['link']
                        )
    db.session.add(new_input)
db.session.commit()
        
