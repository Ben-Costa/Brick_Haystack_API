from Backend.MongoDBSoruce import MongoAtlasConnection
from shaystackdata import rows
import itertools
import random

if __name__ == '__main__':
    
    connection = MongoAtlasConnection()

    #print(len(rows))
    for items in rows:
        items['_id'] = items.pop('id')
        connection.flatDB.insert_one(items)

    #iterables = ['area', 'dis', 'geoAddr', 'geoCity', 'geoCoord', 'geoCountry', 'geoElevation', 'geoPostalCode', 'geoState', 'geoStreet', 'site', 'tz', 'weatherStationRef', 'ahu', 'chilledWaterCooling', 'chilledWaterRef', 'elec', 'equip', 'hotWaterHeating', 'hotWaterRef', 'hvac', 'singleDuct', 'vavZone', 'chilled', 'cmd', 'cool', 'cur', 'his', 'kind', 'point', 'unit', 'valve', 'water', 'custom', 'air', 'discharge', 'fan', 'speed', 'heat', 'hot', 'mixed', 'sensor', 'temp', 'damper', 'outside', 'airRef', 'meter', 'return', 'freq', 'power', 'hisMode', 'run', 'exhaust', 'pressure', 'sp', 'zone', 'occupied', 'humidity', 'dualDuct', 'coldDeck', 'hotDeck', 'fanPowered', 'thermostat', 'vav', 'flow', 'cooling', 'occ', 'heating', 'unocc']

    #data = itertools.permutations(iterables,r=2)
    #perml = []
    
    #counter = 0
    #size = 6


    #while counter < 25:
    #    temp = []
    #    sizecount = 0
    #    while sizecount < size:
    #        temp.append(random.choice(iterables))
    #        sizecount = sizecount + 1
    #    perml.append(temp)
    #    counter = counter + 1
        
    #print(perml)


