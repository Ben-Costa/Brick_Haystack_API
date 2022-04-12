from .Grid import Grid
from Filter_Parser import FilterParser, FilterPhrase
from MongoDBSoruce import MongoAtlasConnection

def About(Credentials, System=None, Server=None, DataBase=None) -> Grid:
    pass

def Ops(Credentials, ObsList, DataBase=None) -> Grid:
    pass

def Read(Credentials, Filter:str, Limit, DataBase=None) -> Grid:
    parsedFilter = FilterParser(Filter)
    dataSource = MongoAtlasConnection()

    returnGrid = MongoAtlasConnection.MongoHaystackRetriever(parsedFilter)

    return returnGrid

def His_Read(Credentials, IDs, Date,DataBase=None) -> Grid:
    pass

#todo 
#1. change id classes and add in more data
#2. test the read ops
#3, test the read api call- determine whats retruned and print
#4. get read api to run on entry into query box
#5. maybe make the time series collection
if __name__ == '__main__':
    Request3 = 'siteRef == a-0000 and point and _id == a-0003' #will change it to be _id = id to get rid of the idobject issues
    Request2 = 'area < 200000'
    Request1 = ''
    Request0 = 'point'
    Request5 = 'noosdfsd'

    print(Read('Root', Request1, ))