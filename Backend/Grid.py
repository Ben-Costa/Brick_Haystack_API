from ast import IsNot
import json
import re
#from bson.objectid import ObjectId
class Tag_Def:
    
    def __init__(self, TagsValuesList):
        pass
#standardized way to define the tags used with data= are dicts with def- name for def, doc- description, is- tree taxonomy, lib- library module that declares the definition

#each building is modeled as a site
#tags- geoaddr, timezone, area, weatherstationref
#yearbuild


#space- floors and rooms of buildings, hvac zones, lighting, ext
#tags- site ref for parent site, space ref tag if contained in another space

#equip- equipmnet that is physical asets
#tags- siteref of parent, and optional space ref, equipref if part of a bigger equipment system

#points- values that store the data- sensors, measurements
#tags- site ref, equip ref and optionally space ref. Eirther sensor (inpit/sensor), dmd- output, or setpoint, point kind tag(analog, digital, multistate), min max, curVal, curStatus, curErr

#in mongo DB- store entities with all respective data and connections- like for a building store its data, referenced meta data for weather station, equipment references- id for lookup only
#store the weather station with references to points only- basically another entity
#store the equipments seperately with meta data aand site ref and other equipment refs
#store points with tags- id, other related tags, kind, his, equipment ref, site ref, unit, tz

#point- site ref and equipment ref
#equipment- site ref + space ref
#site- basic info
#store all in mongo seperately- when want something- first go to site, get info and id, use id to go to space and equipment and get respective items associated with the id, then for all of equipments- go to points

class Grid:
    #list of dicts
    #contains meta data
    #version
    #columns 
    def __init__(self, Version, Metadata, data):
        self.version = {'version': Version}
        self.metadata = Metadata
        self.columns = []
        self.rows = []
        
        if data != None:
            self.addData(data) 
        else:
            self.columns = []
            self.rows = []

    def __str__(self):
        returnString = ""
        returnString = returnString + "Version: " + self.version['version'] + "\n"
        returnString = returnString + "Metadata: " + self.metadata + "\n"
        returnString = returnString + "Columns: " + str(self.columns) + "\n"
        returnString = returnString + "Rows: " + str(self.rows) + "\n"

        return returnString
        #return "Version: " + self.version + "\n metadata: " + self.metadata + "\ncolumns: " + self.columns + "\nrows: " + self.rows

    #when passed a list of dicts or json of data, will parse through each row and add it to the 
    def addData(self, data):
        #check if json- will need to convert to list of dicts
        if data is type(json):
            print("The JSON datatype is not supported by the Grid Class currently")
            return -2

        #iterate through the list make sure that it is form of list of dicts        
        if type(data) == list:
            for items in data:
                #if not a dict within the list send an error
                if type(items) != dict:
                    print("The data within the list for a Grid must be in type Dict")
                    return -1
                self.addRow(items)
        
    def addRow(self, data: dict):
        self.addColumns(data.keys())
        self.rows.append(data)



    def addColumns(self, Columns):
        for column in Columns:
            #check if column exists in grid already
            if column not in self.columns:
                self.addColumn(column)
                

    def addColumn(self, Column):
        self.columns.append(Column)

    def gridToJSON(self)->json:
        pass

    def JSONToGrid():
        pass

    #need to create a series of objects to send to the creator, test all individual functions as well
if __name__ == "__main__":
    data = [{'id': {'_kind': 'ref', 'val': 'a-0002', 'dis': 'a-0002'}, 'chilled': {'_kind': 'marker'}, 'cmd': {'_kind': 'marker'}, 'cool': {'_kind': 'marker'}, 'cur': {'_kind': 'marker'}, 'dis': 'Alpha Airside AHU-2 Chilled Water Valve', 'equipRef': {'_kind': 'ref', 'val': 'a-0001', 'dis': 'a-0001'}, 'his': {'_kind': 'marker'}, 'kind': 'Number', 'point': {'_kind': 'marker'}, 'siteRef': {'_kind': 'ref', 'val': 'a-0000', 'dis': 'a-0000'}, 'tz': 'Denver', 'unit': '%', 'valve': {'_kind': 'marker'}, 'water': {'_kind': 'marker'}, 'custom': {'description': 'Clg_Valve_Cmd'}}, {'id': {'_kind': 'ref', 'val': 'a-0003', 'dis': 'a-0003'}, 'air': {'_kind': 'marker'}, 'cmd': {'_kind': 'marker'}, 'cur': {'_kind': 'marker'}, 'dis': 'Alpha Airside AHU-2 Discharge Fan Speed', 'discharge': {'_kind': 'marker'}, 'equipRef': {'_kind': 'ref', 'val': 'a-0001', 'dis': 'a-0001'}, 'fan': {'_kind': 'marker'}, 'his': {'_kind': 'marker'}, 'kind': 'Number', 'point': {'_kind': 'marker'}, 'siteRef': {'_kind': 'ref', 'val': 'a-0000', 'dis': 'a-0000'}, 'speed': {'_kind': 'marker'}, 'tz': 'Denver', 'unit': '%', 'custom': {'description': 'SF VFD Signal', 'supply': {'_kind': 'marker'}}}, {'id': {'_kind': 'ref', 'val': 'a-0004', 'dis': 'a-0004'}, 'cmd': {'_kind': 'marker'}, 'cur': {'_kind': 'marker'}, 'dis': 'Alpha Airside AHU-2 Hot Water Valve', 'equipRef': {'_kind': 'ref', 'val': 'a-0001', 'dis': 'a-0001'}, 'heat': {'_kind': 'marker'}, 'his': {'_kind': 'marker'}, 'hot': {'_kind': 'marker'}, 'kind': 'Number', 'point': {'_kind': 'marker'}, 'siteRef': {'_kind': 'ref', 'val': 'a-0000', 'dis': 'a-0000'}, 'tz': 'Denver', 'unit': '%', 'valve': {'_kind': 'marker'}, 'water': {'_kind': 'marker'}, 'custom': {'description': 'Htg_Valve_Cmd'}}, {'id': {'_kind': 'ref', 'val': 'a-0005', 'dis': 'a-0005'}, 'air': {'_kind': 'marker'}, 'cur': {'_kind': 'marker'}, 'dis': 'Alpha Airside AHU-2 Mixed Air Temp', 'equipRef': {'_kind': 'ref', 'val': 'a-0001', 'dis': 'a-0001'}, 'his': {'_kind': 'marker'}, 'kind': 'Number', 'mixed': {'_kind': 'marker'}, 'point': {'_kind': 'marker'}, 'sensor': {'_kind': 'marker'}, 'siteRef': {'_kind': 'ref', 'val': 'a-0000', 'dis': 'a-0000'}, 'temp': {'_kind': 'marker'}, 'tz': 'Denver', 'unit': '°F', 'custom': {'description': 'MAT'}}, {'id': {'_kind': 'ref', 'val': 'a-0006', 'dis': 'a-0006'}, 'air': {'_kind': 'marker'}, 'cmd': {'_kind': 'marker'}, 'cur': {'_kind': 'marker'}, 'damper': {'_kind': 'marker'}, 'dis': 'Alpha Airside AHU-2 Outside Air Damper', 'equipRef': {'_kind': 'ref', 'val': 'a-0001', 'dis': 'a-0001'}, 'his': {'_kind': 'marker'}, 'kind': 'Number', 'outside': {'_kind': 'marker'}, 'point': {'_kind': 'marker'}, 'siteRef': {'_kind': 'ref', 'val': 'a-0000', 'dis': 'a-0000'}, 'tz': 'Denver', 'unit': '%', 'custom': {'description': 'Econ_Cmd'}}, {'id': {'_kind': 'ref', 'val': 'a-0007', 'dis': 'a-0007'}, 'air': {'_kind': 'marker'}, 'cur': {'_kind': 'marker'}, 'dis': 'Alpha Airside AHU-2 Outside Air Enthalpy', 'equipRef': {'_kind': 'ref', 'val': 'a-0001', 'dis': 'a-0001'}, 'his': {'_kind': 'marker'}, 'kind': 'Number', 'outside': {'_kind': 'marker'}, 'point': {'_kind': 'marker'}, 'sensor': {'_kind': 'marker'}, 'siteRef': {'_kind': 'ref', 'val': 'a-0000', 'dis': 'a-0000'}, 'tz': 'Denver', 'unit': 'BTU/lb', 'custom': {'description': 'Enthalpy', 'enthalpy': {'_kind': 'marker'}}}, {'id': {'_kind': 'ref', 'val': 'a-0008', 'dis': 'a-0008'}, 'air': {'_kind': 'marker'}, 'cur': {'_kind': 'marker'}, 'dis': 'Alpha Airside AHU-2 Outside Air Temp', 'equipRef': {'_kind': 'ref', 'val': 'a-0001', 'dis': 'a-0001'}, 'his': {'_kind': 'marker'}, 'kind': 'Number', 'outside': {'_kind': 'marker'}, 'point': {'_kind': 'marker'}, 'sensor': {'_kind': 'marker'}, 'siteRef': {'_kind': 'ref', 'val': 'a-0000', 'dis': 'a-0000'}, 'temp': {'_kind': 'marker'}, 'tz': 'Denver', 'unit': '°F', 'custom': {'dryBulb': {'_kind': 'marker'}, 'description': 'OAT'}}]

    testgird = Grid('0.0.0.000.00001', 'metadata', data)

    print(testgird)