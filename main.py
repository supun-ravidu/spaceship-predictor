import json , time
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import numpy as np
import os
import pickle

with open('spaceship_model.dat' , 'rb') as f:
    spaceship_model = pickle.load(f)

app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
@app.route('/SpaceShip', methods=['POST'])
def SpaceShip():
    
        request_data = request.get_json()
        print(request_data)

        res =spaceship_model.predict([[int(str(request_data['HomePlanet'])),int(str(request_data['CryoSleep'])),int(str(request_data['Destination'])),float(str(request_data['Age'])),int(str(request_data['VIP'])),float(str(request_data['RoomService'])),float(str(request_data['FoodCourt'])),float(str(request_data['ShoppingMall'])),float(str(request_data['Spa'])),float(str(request_data['VRDeck'])),int(str(request_data['Deck'])),float(str(request_data['Num'])),int(str(request_data['Side']))]])[0]
        print(res)

        json_dump = json.dumps({"result":str(res),"success":"true"})

        return json_dump

if __name__ == '__main__':
	app.run(host="127.0.0.1", port=1111)