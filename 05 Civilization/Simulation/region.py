class Region:
    def __init__(self, idnum, name, limit, neighbors, occupants=0):
        self.id = idnum
        self.name = name
        self.limit = limit
        self.neighbors = neighbors
        self.occupants = occupants

    def getNeighbors(self):
        return self.neighbors

    def getName(self):
        return self.name

    def getLimit(self):
        return self.limit

    def getOccupants(self):
        return self.occupants

    def incOccupants(self):
        self.occupants += 1