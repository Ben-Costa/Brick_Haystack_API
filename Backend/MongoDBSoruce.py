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
    def getSites(self, Filter):
        pass

    def getWeather(self, WeatherStation, Filter):
        pass

    def getEquipment(self, Filter):
        pass

    def getSpace(self, Filter):
        pass

    def getPoints(self, Filter):
        pass

    

if __name__ == '__main__':
    connection = MongoAtlasConnection()
    connection.Sites.insert_one({"_id" : "a small building"})
