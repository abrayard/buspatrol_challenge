# BusPatrol Challenge

## Description:
Welcome to your coding challenge! Using python 3, flask, and sqlite create a web server route that serves database information. We would like to see you code a RESTFUL GET endpoint at /users/<name> that takes uri paramaters with the user name and returns json with their job and description. I've included the endpoint example usage below and have attached a sqlite database flat file for you to use. Please create a repository on github with your code for us to review and run. Let me know if you have any questions!

* quickstart guide for flask http://flask.pocoo.org/docs/1.0/quickstart/
* sqlite python guide http://zetcode.com/db/sqlitepythontutorial/

## Example:
{host}/users/gene

**Output:**
```
{
"job_title": "devops",
"job_description": "keeps the servers running"
}
```