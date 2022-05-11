import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory)) 

from Backend.Grid import Grid
from Backend.Filter_Parser import FilterParser, FilterPhrase
from Backend.MongoDBSoruce import MongoAtlasConnection

def About(Credentials, System=None, Server=None, DataBase=None) -> Grid:
    pass

def Ops(Credentials, ObsList, DataBase=None) -> Grid:
    pass

def ReadHS(Credentials, Filter:str, Limit, DataBase=None) -> Grid:
    #parsedFilter = FilterParser(Filter)
    dataSource = MongoAtlasConnection()

    returnGrid = dataSource.MongoHaystackRetriever(Filter)

    return returnGrid

def His_Read(Credentials, IDs, Date,DataBase=None) -> Grid:
    pass



if __name__ == '__main__':
    Request3 = 'siteRef == a-0000 and point and _id == a-0003' #will change it to be _id = id to get rid of the idobject issues
    Request2 = 'area < 200000'
    Request1 = 'area == 3149'
    Request0 = 'point'
    Request5 = 'noosdfsd'
    Request111 = 'hvac and thermostat'

    print(ReadHS('Root', Request1, 10, 1))
    #file = open('log.txt', 'w')
    #print(ReadHS('Root', Request111, 10, 1), file = file)

    #file.close()

    #print(ReadHS('Root', Request1, 10, 1))