from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()
# Connect to the DB
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'group23'
# Initiate a connection
mysql.init_app(app)
connection = mysql.connect()
cursor = connection.cursor()
# Session start
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
