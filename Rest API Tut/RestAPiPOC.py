from flask import Flask,request,jsonify
from flask_restful import Api , Resource
from Result import Result
from flaskext.mysql import MySQL

#Initiating Flask App Using Below Function
app = Flask(__name__)
#Initiating Mysql Object
mysql = MySQL()
#Adding All Configuration for Database Here
app.config['MYSQL_DATABASE_USER'] = 'DB_USER'
app.config['MYSQL_DATABASE_PASSWORD'] = 'DB_PassWord'
app.config['MYSQL_DATABASE_DB'] = 'DB_NAME'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#Initiating mysql For flask
mysql.init_app(app)
#Creating Connection Object For mysql
conn = mysql.connect()
#Creating Cursor for db to fetch the result for specific queries
cursor =conn.cursor()

#Here we are writing queries for Fetching all the Api Key created by admin of api in Db for validation and Authorization
cursor.execute("SELECT API_KEY from users")
data = cursor.fetchone()
api_keys=[]
for val in data:
    api_keys.append(val)

#Here We got all The Api Key From DB now we have to check weather the API Key provided by Client is in the List Or not

#What We Are Doing Here is we Have Fetch 127..1/input="what is name "
#TO_DO
@app.route('/',methods=['GET','POST'])
def value():
    #What we are Doing Here is Taking the argument from the url for Api like ABCDEFGH and maching with the DB list of API Key
    #If the API_Key for DB and User Matches then We fetch another input from user as input and Pass that result to return
    api_auth=request.args['api']
    if api_auth in api_keys:
        input_user=request.args['input']
        value=Result.Hello()
        return value+" "+input_user
    else:
        return "Please Check your API Key Then Try Again"



if __name__ == '__main__':
    app.run(debug=True)