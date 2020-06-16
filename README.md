# Search Engine
The search engine is implemented by flask-whoosh. Considering the relatively large file size, I've used sqlite as the database. The search part is implemented by using whoosh. However, since it is a web-based program, for the sake of simplicity, I've used flask to do so. I've implemented several packages in this search engine, flask, flask_sqlalchemy, and flask_whooshalchemyplus.

please make sure use pre-install these packages before running the program.

pip install flask
pip install flask_sqlalchemy
pip install flask_whooshalchemyplus

# How to run 
In the search_engine folder, you will find a python file called pydf.py. Please simply run this file in either terminal or ide to lanuch the program. Before run it, please make sure modify the file path of the database file to accommodate your system. 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/tony/Desktop/search_engine/example.db'

After a few seconds, it should be lanuched on localhost:8002. Please open it with any browsers that you like.
The main.py file is to create a sqlite database, which I've preloaded it already with the paper json file on my system and it is named as example.db
