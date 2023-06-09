from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from flask_cors import CORS, cross_origin

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["fakeNews"]

import re
import json
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'application/json'
app.app_context().push()
# CORS(app, support_credentials=True)
api = Api(app)

cors = CORS(resources={
    r'/*': {
        'origins': [
            'http://localhost:3000'
        ]
    }
})

cors.init_app(app)

# -*- coding: utf-8 -*-
"""fake_news_gpt3_final.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1DGtAHo9Koxt2a48RMJMLPKlBrMfOYywF
"""

#imports 
#get summary  of news 
#

#installations 
# !pip install nltk 
# !pip install newspaper3k 
# !pip install openai
import nltk
from newspaper import Article 
import openai
import nltk
from helpers import fact_check

nltk.download('punkt')

# @cross_origin(supports_credentials=True)
#********************************* Authenticating a User Query ***********************************
# ************************************************************************************************
@app.route('/factcheck',methods=['POST'])
def verifier():
    print("Inside the verifier at the backend")
    data = request.data
    print("The request body is", data)
    result = fact_check(data)
    return jsonify({"result":result}) 

#********************************* Registering a user ***********************************
# ************************************************************************************************
# @app.route("/register", methods=['POST'])
# def register():
#     users = db.users
#     print("Inside the register function at the backend")
#     data = request.data
#     res = json.loads(data)
#     query_user = res["user"]
#     print(query_user["name"])
#     username = query_user["name"]
#     del query_user["name"]
#     query_user["username"] = username
#     print("Searching for the user in the database")
#     query = list(users.find({"username":query_user["username"]}))
#     if len(query) != 0:
#         print("USER FOUND!!")
#         print(list(query))
#     else:
#         print("USER DOES NOT EXIST")
#         inserted_user = dict(users.insert_one(query_user))
#         print("The inserted user is ")
#         print(inserted_user)
#     return jsonify({"MESSAGE":"SUCCESS"})

if __name__ == "__main__":
    app.run(debug=True)