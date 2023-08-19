class Box():
    def __init__(self, fl, next_loc=0):
        self.value = 1
        self.location = 0
        self.old_location = 0
        self.fl = fl

        print(f' in pos {self.location}')

    def next_move(self, next_loc):
        '''Check if next available location is one step away and update location.
        Call FreeLocation to remove location from location list.
        If so, move the box and return previous location to the list'''
        if next_loc - 1 == self.location:
            # Record current position
            if next_loc > 1:
                self.old_location = self.location
            # Update location
            self.location = next_loc
            # Remove location from list
            self.fl.remove()
            # Do the move
            self.movement()
            # Return previous location to the list
            if next_loc > 1:
                self.fl.return_loc(self.old_location)
            print(f' in pos {self.location}')
            return self.location
        else:
            print('No moves available')

    def movement(self):
        print('... ...')


class FreeLocation():
    def __init__(self):
        self.free_location = [1,2,3,4,5,6,7,8,9]
        self.move = 0

    def pick(self):
        '''Returns the lowest value from free location list.'''
        self.move = self.free_location[0]
        return self.move

    def remove(self):
        '''Removes move from location list'''
        self.free_location = self.free_location[1:]
        return self.free_location
    
    def return_loc(self, used_loc):
        '''Returns used location to the list'''
        self.free_location.append(used_loc)
        return self.free_location.sort()


class Calculator():
    def __init__(self):
        self.total = 0

    def add(self, value):
        self.total += value
        return self.total


fl = FreeLocation()
calc = Calculator()

def simulation():
    print('Box 1:')
    box_1 = Box(fl=fl)
    print('Box 1:')
    box_1.next_move(fl.pick())

    print('Box 2:')
    box_2 = Box(fl=fl)
    print('Box 2:')
    box_2.next_move(fl.pick())

    print('Box 1:')
    box_1.next_move(fl.pick())
    print('Box 2:')
    box_2.next_move(fl.pick())

    print('Box 1:')
    box_1.next_move(fl.pick())
    print('Box 2:')
    box_2.next_move(fl.pick())

    print('Box 3:')
    box_3 = Box(fl=fl)
    print('Box 3:')
    box_3.next_move(fl.pick())

    print('Box 1:')
    box_1.next_move(fl.pick())
    print('Box 2:')
    box_2.next_move(fl.pick())
    print('Box 3:')
    box_3.next_move(fl.pick())

    print('Box 4:')
    box_4 = Box(fl=fl)
    print('Box 4:')
    box_4.next_move(fl.pick())

    print('Box 1:')
    box_1.next_move(fl.pick())
    print('Box 2:')
    box_2.next_move(fl.pick())
    print('Box 3:')
    box_3.next_move(fl.pick())
    print('Box 4:')
    box_4.next_move(fl.pick())

    print('Box 5:')
    box_5 = Box(fl=fl)
    print('Box 5:')
    box_5.next_move(fl.pick())

    print('Box 1:')
    box_1.next_move(fl.pick())
    print('Box 2:')
    box_2.next_move(fl.pick())
    print('Box 3:')
    box_3.next_move(fl.pick())
    print('Box 4:')
    box_4.next_move(fl.pick())
    print('Box 5:')
    box_5.next_move(fl.pick())

    print('Box 6:')
    box_6 = Box(fl=fl)
    print('Box 6:')
    box_6.next_move(fl.pick())

    print('Box 1:')
    box_1.next_move(fl.pick())
    print('Box 2:')
    box_2.next_move(fl.pick())
    print('Box 3:')
    box_3.next_move(fl.pick())
    print('Box 4:')
    box_4.next_move(fl.pick())
    print('Box 5:')
    box_5.next_move(fl.pick())
    print('Box 6:')
    box_6.next_move(fl.pick())

    print('Box 7:')
    box_7 = Box(fl=fl)
    print('Box 7:')
    box_7.next_move(fl.pick())

    print('Box 1:')
    box_1.next_move(fl.pick())
    print('Box 2:')
    box_2.next_move(fl.pick())
    print('Box 3:')
    box_3.next_move(fl.pick())
    print('Box 4:')
    box_4.next_move(fl.pick())
    print('Box 5:')
    box_5.next_move(fl.pick())
    print('Box 6:')
    box_6.next_move(fl.pick())
    print('Box 7:')
    box_7.next_move(fl.pick())

    print('Box 8:')
    box_8 = Box(fl=fl)
    print('Box 8:')
    box_8.next_move(fl.pick())

    print('Box 1:')
    box_1.next_move(fl.pick())
    print('Box 2:')
    box_2.next_move(fl.pick())
    print('Box 3:')
    box_3.next_move(fl.pick())
    print('Box 4:')
    box_4.next_move(fl.pick())
    print('Box 5:')
    box_5.next_move(fl.pick())
    print('Box 6:')
    box_6.next_move(fl.pick())
    print('Box 7:')
    box_7.next_move(fl.pick())
    print('Box 8:')
    box_8.next_move(fl.pick())

simulation()