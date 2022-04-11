import pstats
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
from Filter_Parser import FilterParser, FilterPhrase

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
            #self.Points = db["Points"]
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

    #filter- need the site specific stuff- site keyword, equipment specific stuff, space specific stuff, and 
    #order of searching- first get the filter from the user- break down into phrases and find keywords
    #second is to convert broken filter into a understandable thing to be read from the mongo interpreter
    #third is to go through sites seperately get the associated weather, then space, then equip, then points- need
    #to use the info from the prior to get the proper info
    def MongoHaystackRetriever(self, Filter: str):
        #go through the filter phrases and combine into a query
        #use find to do the query
        #send results to grid to be returned
        #step 1- pass the string to the filter parser and get a filter parser class 
        parsedFilter = FilterParser(Filter)

        #step 2- pass the filter parser class and make the string
        mongoQueryString = self.filterParserToString(parsedFilter)

        #step 3- convert the string to the json and change the string ints to ints
        mongoQueryJSON = self.stringToMongoJSON(mongoQueryString)
        

        #step 4- run the query and return the list of documents
        queryResults = connection.flatDB.find(json_query)
        return queryResults
    

    def filterParserToString(filterParser: FilterParser):
        
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
                    query = query + "{" + "\"" + item.getSubject() + ".val\"" + " : " "{\"$lgt\": " + "\"" +item.getValue() + "\"}" + "}"
                    screwUpList.append(item.getSubject() + ".val")
                    screwUpList.append('$lgt')
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
            reverseTheScrews.append(screwUpList)
            query = query + "," 
        
        query = query[:-1] + "]}"


    def stringToMongoJSON(queryString: str):
        #convert the query to a json to be put into the 
        json_query = json.loads(queryString)

        counter = 0
        json_list = json_query['$and']
        for keypair in reverseTheScrews:
            #if the == case and no internal operator exists in the json
            if(keypair[0] == -1):
                counter = counter + 1
                continue
            elif(keypair[1] == 0):
                if(json_list[counter][keypair[0]].isdigit()):
                    json_list[counter][keypair[0]] = int(json_list[counter][keypair[0]])
            else:
                if(json_list[counter][keypair[0]][keypair[1]].isdigit()):
                    json_list[counter][keypair[0]][keypair[1]] = int(json_list[counter][keypair[0]][keypair[1]])
            counter = counter + 1

        #testing the traversal of the json
        #for i in json_query['$and']:
        #    print(type(i['area.val']['$lt']))
        #    print(i['area.val']['$lt'].isdigit())

    

if __name__ == '__main__':
    connection = MongoAtlasConnection()

    #step 1- pass the string to the filter parser and get a filter parser class 
    #test cases
    Request3 = 'siteRef == a-0000 and point and id == a-0003'
    Request2 = 'area < 200000'
    testfilterparser = FilterParser(Request3)


    #temp = connection.flatDB.find({"$and":[{"area.val" : {"$lt": '200000'}}]})
    #for record in temp:
    #    print(record)
    #{"$and":[{'id.val' : 'a-0002'}, { 'point' : {"$exists": True }}]}
    #temp = connection.flatDB.find({"$and":[{'id.val' : 'a-0002'}, { 'point' : {"$exists": 'True' }}]}) 
    #{'_id': ObjectId("624fa8b663dd92f2100cecb4")}, {"rows": { "$elemMatch": { 'point' : {"$exists":'true'} } } } 
    #for record in temp:
    #    print(record)
    #work with the database- the documents are top level
    #will then stick as is into the grid
    #{'id.val' : "a-0002"}
    #'point': { '$exists': True }
    #{"age": {"$gt": 20}}
    #'<', '>', '=<', '=<', '==', '!='

    #print(testfilterparser.getPhraseList())
    
    #for item in testfilterparser.getPhraseList():
    #    print(item)

    #create list to hold the key pairs within the json. This is done to later go through the json document and find all strings that need to be converted into ints
    reverseTheScrews = []

    #step 2- pass the filter parser class and make the string
    #start of the query 
    query = "{\"$and\":["

    #method 2- passed the filter 
    #iterate through the filter parser list
    for item in testfilterparser.getPhraseList():
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
                query = query + "{" + "\"" + item.getSubject() + ".val\"" + " : " "{\"$lgt\": " + "\"" +item.getValue() + "\"}" + "}"
                screwUpList.append(item.getSubject() + ".val")
                screwUpList.append('$lgt')
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
        reverseTheScrews.append(screwUpList)
        query = query + "," 
    
    query = query[:-1] + "]}"
    
    #step 3- convert the string to the json and change the string ints to ints
    #convert the query to a json to be put into the 
    json_query = json.loads(query)

    counter = 0
    json_list = json_query['$and']
    for keypair in reverseTheScrews:
        #if the == case and no internal operator exists in the json
        if(keypair[0] == -1):
            counter = counter + 1
            continue
        elif(keypair[1] == 0):
            if(json_list[counter][keypair[0]].isdigit()):
                json_list[counter][keypair[0]] = int(json_list[counter][keypair[0]])
        else:
            if(json_list[counter][keypair[0]][keypair[1]].isdigit()):
                json_list[counter][keypair[0]][keypair[1]] = int(json_list[counter][keypair[0]][keypair[1]])
        counter = counter + 1

    #testing the traversal of the json
    #for i in json_query['$and']:
    #    print(type(i['area.val']['$lt']))
    #    print(i['area.val']['$lt'].isdigit())

    #step 4- run the query and return the list of documents
    temp = connection.flatDB.find(json_query)

    for record in temp:
        print(record)







    #filter- need the site specific stuff- site keyword, equipment specific stuff, space specific stuff, and 
    #order of searching- first get the filter from the user- break down into phrases and find keywords
    #second is to convert broken filter into a understandable thing to be read from the mongo interpreter
    #third is to go through sites seperately get the associated weather, then space, then equip, then points- need
    #to use the info from the prior to get the proper info
    def MongoHaystackRetriever(self, Filter):
        #1. orgnaize the phrases into what database they apply to
        #2. go to site, pull out all sites that apply
        #3. go to weather, use weather references from site to get all weather stations (use phrases to narrow if apply)
        #4. go to space with site ref and space phrases
        #5. go to equipment, bring siteRefs and the equipment phrases
        #6. go to points, bring equipment phrases
        #for the above- could just loop through the passed references for the query and add in the other operators- so avoid issue of query with list
        #or
        #use db.bios.find( { contribs: { $in: [ "ALGOL", "Lisp" ]} } )

        pass
    
    #give the Filter (list of phrases), return an orgnaized dict of each phrase in its associated reference location
    #def createPhraseRelationDict(Filter):
    #    ontologyOrganizedPhraseDict = {"SITE": [], "SPACE": [], "EQUIPMENT": [], "POINT": [], "Error: Tag Not Found": [] }

    #    for phrase in Filter:
    #        for relations in phrase.getTags():
    #            ontologyOrganizedPhraseDict[relations].append(phrase)
    #    
    #    return ontologyOrganizedPhraseDict

        #this returns the entire row list
    #temp = connection.flatDB.find({'_id': ObjectId("624fa8b663dd92f2100cecb4")}, {"rows": 1 })
    

    #this returns only the first point object
    #temp = connection.flatDB.find({'_id': ObjectId("624fa8b663dd92f2100cecb4")}, {"rows": { "$elemMatch": { 'point' : {"$exists":'true'} } } } )

    #this prints out only the point objects
    #temp2 = connection.flatDB.find({'_id': ObjectId("624fa8b663dd92f2100cecb4")}, {"rows.point": 1 } )