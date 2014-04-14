import os
import sqlite3
from flask import Flask, render_template, request, g

#initialize the Flask object
app = Flask(__name__)

#change config settings from default
app.config.update(dict(
  DATABASE=os.path.join(app.root_path, 'salsa_votes.db'),
  DEBUG=True,
  SECRET_KEY='123456',
  USERNAME='admin',
  PASSWORD='default'
))

def connect_db():
  #Connects to the specific database
  rv = sqlite3.connect(app.config['DATABASE'])
  rv.row_factory = sqlite3.Row #treats rows like dicts
  return rv

#method to create the database
def init_db():
  #must explicitly declare app context bc there's no request yet
  with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

def get_db():
  #Opens db connection if one doesn't exist
  if not hasattr(g, 'sqlite_db'):
    g.sqlite_db = connect_db()
  return g.sqlite_db

#i think this executes at the end of every request
# (indeed, that's what the teardown marker is for)
#if process executes properly, no error occurs
#if error occurs, it's passed to this method
@app.teardown_appcontext
def close_db(error):
  if hasattr(g, 'sqlite_db'): #checks to see if db conn exists
    g.sqlite_db.close()

@app.route('/')
def vote():
  return render_template('vote.html')

if __name__ == '__main__':
  app.run()
