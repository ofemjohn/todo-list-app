from flask import Flask, jsonify, request, make_response
from database.db import Db
from flask_cors import CORS


app = Flask(__name__)
DB = Db(app)
CORS(app, supports_credentials=True)


