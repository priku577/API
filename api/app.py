

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# Assuming salaries.db is in your app root folder
e = create_engine('sqlite:///customerData.db')  # loads db into memory

app = Flask(__name__)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)

class all_customerDetails(Resource):
	def get(self):
		conn = e.connect()  # open connection to memory data
		query = conn.execute("select * from customerData")  # query
		return  query.cursor.fetchall()  

class bank_Branches(Resource):
	def get(self):
		conn = e.connect()  # open connection to memory data
		query = conn.execute("select distinct Branches from customerData")  # query
		return {'Branches': [i[0] for i in query.cursor.fetchall()]}  # format results in dict format

class kiruna_Branch(Resource):
    def get(self):  # param is pulled from url string
        conn = e.connect()
        query = conn.execute("select * from customerData where Branches='Kiruna'")
        return query.cursor.fetchall()

class stockholm_Branch(Resource):
    def get(self):  # param is pulled from url string
        conn = e.connect()
        query = conn.execute("select * from customerData where Branches='Stockholm'")
        return query.cursor.fetchall()



api.add_resource(all_customerDetails, '/completeData')  # bind url identifier to class
api.add_resource(kiruna_Branch, '/KirunaBranch/') 
api.add_resource(stockholm_Branch, '/StockholmBranch/') 
api.add_resource(bank_Branches, '/Branches/') 


if __name__ == '__main__':
    app.run(debug=True)
