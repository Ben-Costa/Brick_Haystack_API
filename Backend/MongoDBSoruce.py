import sys  
from pathlib import Path
from tokenize import Double  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory)) 

from cgi import test
import pstats
from re import A
import sys  
from pathlib import Path
from urllib.request import Request  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

import json
import pymongo 
from pymongo import MongoClient
from pymongo.errors import ConfigurationError, ConnectionFailure, OperationFailure
from to_ignore import var
from Backend.Filter_Parser import FilterParser, FilterPhrase
from Backend.Grid import Grid

BRICK_HAYSTACK_VERSION = '0.0.00000001'
METADATA = 'This will be for later metadata'

class MongoAtlasConnection:

    def __init__(self):
        
        try:
            cluster = MongoClient(var)
            db = cluster["BrickStack"]
            temp = cluster.admin.command('ping')
            

            self.mgclient = cluster
            self.db = db
            self.flatDB = db["HaystackFlatDB"]
            #self.Equipment = db["Equipment"]
            self.Points = db["Points"]
            #self.Sites = db["Site"]
            #self.Space = db["Space"]

            self.connection_status = True

        except ConfigurationError:
            print("Configuration Error: Database Connection Failed")
            self.connection_status = False
        except ConnectionFailure:
            print("Execption Error: Database Connection Failed")
            self.connection_status = False
            return
        except OperationFailure:
            print("Authentication Failure: Invalid Credentials")
            self.connection_status = False
            return

    def MongoHaystackRetriever(self, Filter: str):

        if(Filter == ''):
            queryResults = self.Points.find()
            returnedList = MongoIteratorToList(queryResults)
            returnGrid = Grid(BRICK_HAYSTACK_VERSION, METADATA, returnedList)
            return returnGrid

        #step 1- pass the string to the filter parser and get a filter parser class 
        parsedFilter = FilterParser(Filter)

        #step 2- pass the filter parser class and make the string + step 3 convert string to json
        json_query = self.filterParserToJSON(parsedFilter)        
        

        #step 4- run the query and return the list of documents
        queryResults = self.Points.find(json_query)
        
        returnedList = MongoIteratorToList(queryResults)
        returnGrid = Grid(BRICK_HAYSTACK_VERSION, METADATA, returnedList)
        return returnGrid
    

    def filterParserToJSON(self, filterParser: FilterParser) -> list:
        
        keyList = []
        #step 2- pass the filter parser class and make the string
        #start of the query 
        query = "{\"$and\":["

        #method 2- passed the filter 
        #iterate through the filter parser list
        for item in filterParser.getPhraseList():
            #list to hold the keys for later int changing traversal
            screwUpList = []
            #if no comparison then just add in a exists tag as searching if a tag exists
            if item.getComparison() == 'no comparison found':
                query = query + "{" + "\"" + item.getSubject() + "\"" + " : { \"$exists\": \"True\" }}"
                #append -1 as this is a later case that will be skilled
                screwUpList.append(-1)
            else:
                #else search what type of comparison it is, add to the string, need .val as thats how the data is stored (type,val,description)
                if item.getComparison() == "==":
                    query = query + "{" + "\"" + item.getSubject() + ".val\"" + " : " "\"" + item.getValue() + "\"" + "}"
                    #append the key of the subject to the list and append 0 to the second space in the list as no operators exisists in this case
                    screwUpList.append(item.getSubject() + ".val")
                    screwUpList.append(0)
                elif item.getComparison() == "<":
                    query = query + "{" + "\"" + item.getSubject() + ".val\"" + " : " "{\"$lt\": " + "\"" +item.getValue() + "\"}" + "}"
                    #append both the operator and the subject as these are both needed for the traversal
                    screwUpList.append(item.getSubject() + ".val")
                    screwUpList.append('$lt')
                elif item.getComparison() == ">":
                    query = query + "{" + "\"" + item.getSubject() + ".val\"" + " : " "{\"$gt\": " + "\"" +item.getValue() + "\"}" + "}"
                    screwUpList.append(item.getSubject() + ".val")
                    screwUpList.append('$gt')
                elif item.getComparison() == "=<":
                    query = query + "{" + "\"" + item.getSubject() + ".val\"" + " : " "{\"$lte\": " + "\"" +item.getValue() + "\"}" + "}"
                    screwUpList.append(item.getSubject() + ".val")
                    screwUpList.append('$lte')                
                elif item.getComparison() == "=>":
                    query = query + "{" + "\"" + item.getSubject() + ".val\"" + " : " "{\"$gte\": " + "\"" +item.getValue() + "\"}" + "}"
                    screwUpList.append(item.getSubject() + ".val")
                    screwUpList.append('$gte')     
                elif item.getComparison() == "!=":
                    query = query + "{" + "\"" + item.getSubject() + ".val\"" + " : " "{\"$ne\": " + "\"" +item.getValue() + "\"}" + "}"
                    screwUpList.append(item.getSubject() + ".val")
                    screwUpList.append('$ne')    
                else:
                    print('comparison not found')
            #add the key pair to the key list
            keyList.append(screwUpList)
            query = query + "," 
        
        query = query[:-1] + "]}"
        
        #convert the query to a json to be put into the 
        json_query = json.loads(query)

        counter = 0
        json_list = json_query['$and']
        #Iterate through the keylist and find all value comparisons. These are currently stored as strings and need to be converted to floats.
        ###ISSUE: this converts to floats and will not work if the mongo is storing ints. Need to find a way to determine the proper comparison of the value
        for keypair in keyList:
            #if the == case and no internal operator exists in the json
            if(keypair[0] == -1):
                counter = counter + 1
                continue
            elif(keypair[1] == 0):
                if(json_list[counter][keypair[0]].isdigit()):
                    json_list[counter][keypair[0]] = float(json_list[counter][keypair[0]])
                    print(json_list[counter][keypair[0]])
            else:
                if(json_list[counter][keypair[0]][keypair[1]].isdigit()):
                    json_list[counter][keypair[0]][keypair[1]] = float(json_list[counter][keypair[0]][keypair[1]])
                    print(json_list[counter][keypair[0]])
            counter = counter + 1

        return json_query


#This function takes in a mongo iterator and converts it into a python list for easier use
def MongoIteratorToList(Iterator):
    itemList = []
    for doc in Iterator:
        itemList.append(doc)

    return itemList
    

if __name__ == '__main__':
    connection = MongoAtlasConnection()


    #step 1- pass the string to the filter parser and get a filter parser class 
    #test cases
    Request3 = 'siteRef == a-0000 and point and _id == a-0003' #will change it to be _id = id to get rid of the idobject issues
    Request2 = 'area < 200000'
    Request1 = 'curVal =< 10'
    Request0 = 'point'
    Request5 = 'noosdfsd'
    
    
    testfilterparser = connection.MongoHaystackRetriever(Request1)

    print(testfilterparser)
    print(testfilterparser.rowsLength())

    
