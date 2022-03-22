class Grid:
    #list of dicts
    #contains meta data
    #version
    #columns 
    def __init__(self, Version, Metadata, Columns):
        self.version = {'version': Version}
        self.metadata = Metadata
        self.columns = Columns 


    def addColumn(self, Column):
        self.columns.append(Column)

