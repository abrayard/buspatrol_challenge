# BusPatrol Challenge

## Description:
Welcome to your coding challenge! Using python 3, flask, and sqlite create a web server route that serves database information. We would like to see you code a RESTFUL GET endpoint at /users/<name> that takes uri paramaters with the user name and returns json with their job and description. I've included the endpoint example usage below and have attached a sqlite database flat file for you to use. Please create a repository on github with your code for us to review and run. Let me know if you have any questions!

* quickstart guide for flask http://flask.pocoo.org/docs/1.0/quickstart/
* sqlite python guide http://zetcode.com/db/sqlitepythontutorial/

## Example:

**Action:**
```
GET Request from http://127.0.0.1:5000/users/gene
```

**Output:**
```
{
"job_title": "devops",
"job_description": "keeps the servers running"
}
```

## Setup:
*Before setting up, it is assumed you have Python 3.6.x or higher installed and that you have basic command line knowledge. This setup has been tested on Ubuntu 20.04; Steps could vary for a Windows machine.*

1. Open your terminal, and install dependencies for the Python program by running: `pip3 install flask flask_restful requests`.
2. After installing dependencies and cloning this repository, navigate to `buspatrol_challenge/` and run the command `python3 main.py`.
3. You will be prompted with the default host set to be http://127.0.0.1:5000/. No index page is set, however you should still be able to open a browser and navigate to the following url: http://127.0.0.1:5000/users/gene. The output should be in JSON format with the user's job title and job description.
4. (Optional) Open another terminal, navigate to the `buspatrol_challenge/` and run the command `python3 test.py` to test the GET request and confirm the json output with the small tester.

