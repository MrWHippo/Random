

class node():
    def __init__(self, selfvalue):
        self.value = selfvalue
        self.neighbours = []
        self.visited = False
        self.parent = None
        self.entry_time = None
        self.exit_time = None
        self.placeval = 0

    def give_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def get_neighbours(self):
        return self.neighbours
    
