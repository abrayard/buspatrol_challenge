from flask import Flask
from flask_restful import Api, Resource
import sqlite3 as lite

app = Flask(__name__)
api = Api(app)

class Users(Resource):
	def get(self, name):
		# sanitizing name input in attempt to prevent sql injections
		name = name.split(" ")[0]

		con = lite.connect('buspatrol.db')
	
		with con:
			cur = con.cursor()
			
			cur.execute(f'''
				select title, description
				from jobs
				where id = (select job 
				            from users 
				            where "{name}" = name)
			''')

			attribute = cur.fetchone()

		return {"job_title": attribute[0], "job_description": attribute[1]}

api.add_resource(Users, '/users/<string:name>')

if __name__ == "__main__":
	app.run()