# This file initializes your application and brings together all of the various components.
# app.py or app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config.from_object('config')
app.config.from_pyfile('../instance/config.py')

db = SQLAlchemy(app)



#  Now we can access the configuration variables via app.config["VAR_NAME"]
