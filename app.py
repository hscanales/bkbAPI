import os

from flask import Flask, jsonify, request
from pymongo import MongoClient

user = str(os.environ.get('USER'))
pw = str(os.environ.get('PW'))
server = str(os.environ.get('SV'))
tb1 = str(os.environ.get("tb1"))
tb2 = str(os.environ.get("tb2"))
tb3 = str(os.environ.get("tb3"))

client = MongoClient("mongodb+srv://"+user+":"+pw+"@"+server)
db = client[tb3]
partidos = db[tb1]
usuarios = db[tb2]

app = Flask(__name__)

@app.route('/login')
def getusers():
    users = [doc for doc in usuarios.find({}, {"_id": 0})]

    return jsonify(users)


@app.route('/<string:user>/partidos')
def getpartidos(user):
    bkb = [doc for doc in partidos.find({"_id": user}, {"_id": 0})]
    return jsonify(bkb)


if __name__ == '__main__':
    app.run()
