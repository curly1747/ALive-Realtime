from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DatabaseConfig

app = Flask(__name__, static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = DatabaseConfig.URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
engine = db.get_engine(app)
Session = db.create_scoped_session(options=dict(bind=engine))
