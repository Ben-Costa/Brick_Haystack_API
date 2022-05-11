from asyncore import read
import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory)) 

import json
from crypt import methods
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Email, EqualTo

from Application import app
from flask.wrappers import Request
from flask import render_template, redirect, url_for, flash, request, jsonify
from Backend.Operations import Ops, ReadHS
#from ..Backend.Request_Parser import Requestparser
#FilterParser

#the home page will contain the search bar which will call the read ops with filter query, the date search bar for hisread. When those
#are entered and the event is registered js will need to call the fetch api on the appropriate. Seems that the home bar calls the other
#apis to generate the final view
#parameters- q= "query parameters used to generate the current screen" (optional)
#            a= "user information"
#            d= "date rang ex: 2022-1-12,2022-3-12"
@app.route('/', methods = ["GET", "POST"])
@app.route('/home/', methods = ["GET", "POST"])
def home_page():         
    
    if request.method == 'POST':
        print(request.form.get('test'))
        url = '/home' + '?q='+ str(request.form.get('test'))
        return redirect(url)
    credentials = request.args.get('a')

    if request.args.get('q') == None:
        filter = ""
    else:
        filter = request.args.get('q')
        print(filter)

    if request.args.get('d') == None:
        daterange = ""
    else:
        daterange = request.args.get('d')
    
    #obtain converted filter from request parser
    queryResults = ReadHS(credentials, filter, 10, 1)
    #return json.load(queryResults)
    #if not queryResults == '':
    #    tempstr = str(queryResults)
    #    return jsonify(tempstr)
            #call the read api to get the ids that match the filter parameters

    #call the his_read for each item in the object returned by the read api call, append the data to the grid

    #convert grid to response and send back (the ui will handle taking the data and formatting it with provided objects)

    #return str(queryResults)



    return render_template('base.html', returned_data= queryResults.rows)

#When called, will use the provided filter parameter convert it to a request using the parser request class, call the python read ops
#sending the request in the call. This will the go off and get the matching data from the provider and then return a grid of the data
#parameters: Filter, a (user key/data),  
@app.route('/Read', methods=['GET'])
def Read():
        filter = request.args.get('filter')
        user = request.args.get('a')
        limit = request.args.get('limit')
        
        return {'filter': request.args.get('filter'), 'user': request.args.get('a')}


#When called, will call the his_read python ops and pass the id of the desired object along with the date range. The python his_read will
# use this info to go to the time series data and return the time data. This is done for each seperate id
#sending the request in the call. This will the go off and get the matching data from the provider and then return a grid of the data
#parameters: Filter, a (user key), dateFrame (d)  
@app.route('/hisRead', methods=['GET'])
def His_Read():
        id = request.args.get('id')
        user = request.args.get('a')
        dateFrame = request.args.get('d')
        
        return {'id': request.args.get('id'), 'dateFrame': request.args.get('d')}

from requests.api import delete
from flask_restful import Api, Resource,  reqparse, abort, fields, marshal_with
from Application import app

#api = Api(app)


#About API- When called returns information relating to packages, version, and server
#Requires- nothing
#Returns- haystackVersion, server timezone, sever name, current datetime on server clock,
#uri of website, name of company, vendor website, module version
#class About(Resource):
    #def get(self, name, test):
    #    return {"data": name, "test": test}

#    def get(self):
#        return "0.0.001"

#api.add_resource(About, "/BrickHayStack/about")


#Defs API- returns a list of operation definitions that can be used 
#by the user
#input- filter (optional string) and limit (int)
#returns- grid with dictionary represetnation of each ops and its definition
#class Defs(Resource):
    #def get(self, name, test):
    #    return {"data": name, "test": test}

#    def get(self):
#        return "0.0.002"


#api.add_resource(Defs, "/BrickHayStack/defs")



#example/test api
#class HelloWorld(Resource):
    #def get(self, name, test):
    #    return {"data": name, "test": test}

#    def get(self, name):
#        return name

#    def post(self):
#        return {"data": "Posted"}
#
#api.add_resource(HelloWorld, "/helloworld/<string:name>")


#class to standardize the http responses
class HTTP_Response:
    
    def __init__(self, Code, Body):
        self.Code = Code
        self.Body = Body