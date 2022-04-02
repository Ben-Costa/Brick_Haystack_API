import pstats
import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

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
            self.Equipment = db["Equipment"]
            self.Points = db["Points"]
            self.Sites = db["Site"]
            self.Space = db["Space"]

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
    def createPhraseRelationDict(Filter):
        ontologyOrganizedPhraseDict = {"SITE": [], "SPACE": [], "EQUIPMENT": [], "POINT": [], "Error: Tag Not Found": [] }

        for phrase in Filter:
            for relations in phrase.getTags():
                ontologyOrganizedPhraseDict[relations].append(phrase)
        
        return ontologyOrganizedPhraseDict

    def getSites(self, SitePhrases):
        pass

    def getWeather(self, WeatherStationRefs, WeatherPhrases):
        pass

    def getEquipment(self, EquipmentPhrases):
        pass

    def getSpace(self, Filter):
        pass

    def getPoints(self, Filter):
        pass

    

if __name__ == '__main__':
    connection = MongoAtlasConnection()
    connection.Sites.insert_one({"_id" : "a small building"})
