from bottle import default_app, route, template
import sqlite3

connection = sqlite3.connect("shopping_list.db")

@route('/')
def hello_world():
    return 'Hello from Dr. DeLozier!'

@route('/hi')
def hi_world():
    return 'Hi from Dr. DeLozier!'

@route('/bye')
def bye_world():
    return 'Bye from Dr. DeLozier!'

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [ {'id':row[0] ,'desc':row[1]} for row in rows ]
    return template("shopping_list.tpl", name="Dr. DeLozier", shopping_list=rows)

application = default_app()

