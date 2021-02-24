from flask import Flask
from flask_restful import Api, Resource
import sqlite3 as lite

# Creates a Flask instance for this module
app = Flask(__name__)
# Creates an instance of a REST API with the Flask app 
api = Api(app)

# Users gets the Resource inheritance for the HTTP GET method
class Users(Resource):

	def get(self, name=""):
		# Sanitizing name input in attempt to prevent sql injections
		name = name.split(" ")[0]

		# Establishing a connection to the database
		con = lite.connect('buspatrol.db')
		
		with con:
			# Cursor object is used to traverse records and execute queries
			cur = con.cursor()
			
			# Execute query to give the title and description of a valid user from users.  
			cur.execute(f'''
				select title, description
				from jobs
				where id = (select job 
				            from users 
				            where "{name}" = name)
			''')

			# Fetches the first row from the execute query as a tuple
			# This is assuming since there are no duplicated names in the database. If the database had duplicated names we would use IDs.
			attribute = cur.fetchone()

			if attribute == None:
				return {"invalid_user" : name}

		# Return user's job title and job description
		return {"job_title": attribute[0], "job_description": attribute[1]}

# The URL /users/{name} is routed to the Users Resource which handles all names in the sqlite database. 
api.add_resource(Users, '/users/<string:name>')

if __name__ == "__main__":
	app.run()
