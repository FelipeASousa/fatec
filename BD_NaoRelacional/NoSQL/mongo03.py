import bottle
import pymongo
@bottle.route('/')
def index():
  from pymongo import MongoClient
  connection = MongoClient("mongodb://localhost")
  db = connection.test

  names = db.names
  names.insert_one({'name': 'Felipe Augusto'})
                   
  item = names.find_one()

  return '<b>Hello %s!</b>' %item['name']

bottle.run(host='localhost', port = 8082)
