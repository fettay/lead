from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

home = str(Path.home())


DB_URL = 'sqlite:///%s/data.db' % home

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)

# an Engine, which the Session will use for connection
# resources
engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)

