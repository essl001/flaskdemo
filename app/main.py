import json

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class AppUser:
    def __init__(self, sn, name, age):
        self.sn = sn
        self.name = name
        self.age = age

    def serialize(self):
        return {"sn": self.sn,
                "name": self.name,
                "age": self.age
                }


@app.route('/')
def index():
    return "<h1>Welcome to Flask Demo</h1>"


@app.route("/users/all", methods=['GET'])
@cross_origin()
def allUsers():
    with open('/tmp/api.txt', 'r') as u:
        try:
            data = u.read()
            users = json.loads(data)
            return jsonify({'data': users}, 200)
        except ValueError:
            return jsonify({'error': 'File is empty'})


@app.route("/users/add", methods=['PUT'])
@cross_origin()
def newUser():
    rec = json.loads(request.data)
    with open('/tmp/api.txt', 'r') as u:
        data = u.read()
    if not data:
        users = [rec]
    else:
        users = json.loads(data)
        users.append(rec)
    with open('/tmp/api.txt', 'w') as u:
        u.write(json.dumps(users, indent=2))
    return jsonify(rec)

def userUpdate():
    return jsonify({"data": "Updated"}, 200)
