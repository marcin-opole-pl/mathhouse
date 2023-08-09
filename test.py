class Box():
    def __init__(self, next_loc):
        self.location = 0

    def next_move(self, next_loc):
        move = self.location + next_loc
        return move

    def visited_loc():
        visited = [0]
        return visited

class FreeLocation:
    def __init__(self):
        self.free_location = 0
    
    def update(self):
        self.free_location = 1
        return self.free_location

fl = FreeLocation()

box1 = Box(fl.update())

print(box1.next_move(fl.update()))