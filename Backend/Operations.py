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