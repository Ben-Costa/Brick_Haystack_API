from ast import IsNot
import json


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
        

        if data == None:
            self.addData(data) 
        else:
            self.columns = []
            self.rows = []

    #when passed a list of dicts or json of data, will parse through each row and add it to the 
    def addData(self, data):
        #check if json- will need to convert to list of dicts
        if data is type(json):
            return -2

        #iterate through the list make sure that it is form of list of dicts        
        if data is type(list):
            for items in data:
                #if not a dict within the list send an error
                if items is not type(dict):
                    return -1
                self.addRow(data)
        
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
        pass