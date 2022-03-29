import json


class Tag_Def:
    
    def __init__(self, TagsValuesList):
        pass
#standardized way to define the tags used with data= are dicts with def- name for def, doc- description, is- tree taxonomy, lib- library module that declares the definition

#each building is modeled as a site
#tags- geoaddr, timezone, area, weatherstationref
#yearbuild


#space- floors and rooms of buuldings, hvac zones, lighting, ext
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
    def __init__(self, Version, Metadata, Columns):
        self.version = {'version': Version}
        self.metadata = Metadata
        self.columns = Columns 

    def checkIfColumnExists(self, ColumnName):
        pass

    def addColumn(self, Column):
        self.columns.append(Column)

    def gridToJSON(self)->json:
        pass

    def JSONToGrid():
        pass