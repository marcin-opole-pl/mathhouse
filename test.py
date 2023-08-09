class Box():
    def __init__(self, next_loc=0):
        self.location = 0
        print(f' in pos {self.location}')

    def next_move(self, next_loc):
        '''Checks if next available location is one step away and updates location.
        Calls FreeLocation to remove location from location list.'''
        if next_loc - 1 == self.location:
            self.location = next_loc
            FreeLocation.remove(self) # TO DO
            print(f' in pos {self.location}')
            return self.location
        else:
            print('No moves available')


class FreeLocation:
    def __init__(self, next_loc=0):
        self.free_location = [1,2,3,4,5,6,7,8,9]
        self.move = 0

    def pick(self):
        '''Returns the lowest value from free location list.'''
        self.move = self.free_location[0] # Need to sort
        return self.move

    def remove(self):
        '''Removes move from location list'''
        self.free_location = self.free_location[:1]



fl = FreeLocation()
print('Box 1:')
box_1 = Box()
print('Box 1:')
box_1.next_move(fl.pick())
print('Box 2:')
box_2 = Box()
print('Box 2:')
box_2.next_move(fl.pick())
print('Box 1:')
box_1.next_move(fl.pick())
print('Box 1:')
box_1.next_move(fl.pick())
print('Box 1:')
box_1.next_move(fl.pick())
