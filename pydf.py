from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os 
from data import Papers
#import flask_whooshalchemy as wh
import flask_whooshalchemyplus as wh



app = Flask(__name__)

# configure my database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/tony/Desktop/search_engine/example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['WHOOSH_BASE'] = 'whoosh'

db = SQLAlchemy(app)

# initialize the database and the class
class myPaper(db.Model):
    __searchable__ = ['title', 'abstract', 'author', 'link']

    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(1000))
    abstract = db.Column(db.String(1000))
    author = db.Column(db.String(1000))
    link = db.Column(db.String(1000))

wh.whoosh_index(app, myPaper)

def __init__(self, id, title, abstract, author, link):
    self.id = id
    self.title = title
    self.abstract = abstract
    self.author = author
    self.link = link


Papers = Papers()

# app search componet
@app.route('/search')
def search():
    paper = myPaper.query.whoosh_search(request.args.get('query'), limit=100).all()
    paper2 = myPaper.pure_whoosh(request.args.get('query'))

    '''
    for hit in paper:
        #print(hit['title'])
        print(hit.highlights("abstract"))
    '''
    print(paper2)
    print(request.args.get('query'))
    print(paper[0].id)

    return render_template('index.html', mypaper=paper)

# works as the main page and may add more functions later
@app.route('/')
def index():
    paper = myPaper.query.all()
    return render_template('index.html', mypaper=paper)

# to see all the papers, could add the link to each one later
@app.route('/papers')
def papers():
    return render_template('papers.html', papers = Papers)

# supposed to return the id of each paper
@app.route('/to_paper/<string:id>/')
def to_paper(id):
    return render_template('to_paper.html', id=id)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8002, use_reloader=True, threaded=True)
