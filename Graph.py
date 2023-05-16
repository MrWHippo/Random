

class node():
    def __init__(self, selfvalue):
        self.value = selfvalue
        self.neighbours = []
        self.weightofneighbours = []
        self.visited = False
        self.parent = None
        self.entry_time = None
        self.exit_time = None
        self.placeval = 0
        self.priority = 0
        self.final = False
        


    def give_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def get_neighbours(self):
        return self.neighbours

    def give_neighbour_weight(self, weight):
        self.weightofneighbours.append(weight)

    def getplaceofweight(self, searchnode):
        count = -1
        for node in self.neighbours:
            count +=1
            if node.value == searchnode.value:
                return count
        
    def checkfinal(self):
        return self.final
    
