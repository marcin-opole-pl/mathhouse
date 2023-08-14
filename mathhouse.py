import pygame
from random import randint


class Box(pygame.sprite.Sprite):
    ''' Operates boxes behavior'''
    def __init__(self, fl, calc):
        super().__init__()
        # Load all box images
        image_1 = pygame.image.load('images/box_0.png').convert_alpha()
        image_2 = pygame.image.load('images/box_1.png').convert_alpha()
        # Randomize value of the box
        self.value = randint(0,1)
        # Dict to store values and images
        images = {0: image_1, 1: image_2}
        # Set image
        self.image = images[self.value]
        self.rect = self.image.get_rect(midleft=(-50,400)) # Draw rectangle

        self.location = 0
        self.speed = 2
        self.distance = 60
        self.fl = fl
        self.calc = calc

    def return_loc(self, i):
        '''Return previous location to the FreeLocation list'''
        if i not in fl.free_location:
            self.fl.return_loc(i)

    def move_from_position_to_position(self, i):
        ''' If next position is available, move to next position'''
        if self.location == i:
            if (i+1) in fl.free_location:
                if self.rect.x <= ((self.distance * (i+1)) - self.speed):
                    self.rect.x += self.speed

    def action_at_position(self, i):
        ''' If at new position and position location is available,
        remove from FreeLocation list new location,
        set location to new location, 
        return current location to FreeLocation list.
        DOES NOT WORK FOR position 1''' 
        if self.rect.x == (self.distance * i) and i in fl.free_location:
            fl.remove(i)
            self.location = i
            self.return_loc(i-1)

    def update(self):
        # Move from pos 0 to 1
        self.move_from_position_to_position(0)
        # Pos 1
        if self.rect.x == 50 and 1 in fl.free_location:
            fl.remove(1)
            self.location = 1
        # Move from 1 to 2
        self.move_from_position_to_position(1)
        # Pos 2
        self.action_at_position(2)
        # Move from 2 to 3
        self.move_from_position_to_position(2)
        # Pos 3
        self.action_at_position(3)
        # Move from 3 to 4
        self.move_from_position_to_position(3)
        # Pos 4
        self.action_at_position(4)
        # Move from 4 to 5
        self.move_from_position_to_position(4)
        # Pos 5
        self.action_at_position(5)
        # Move form 5 to 6
        self.move_from_position_to_position(5)
        # Pos 6
        self.action_at_position(6)
        # Move from 6 to 7
        self.move_from_position_to_position(6)
        # Pos 7
        self.action_at_position(7)
        # Move form 7 to 8
        self.move_from_position_to_position(7)
        # Pos 8
        self.action_at_position(8)
        # Move from 8 to 9
        self.move_from_position_to_position(8)
        # Pos 9
        self.action_at_position(9)
        # Move from 9 to 10
        self.move_from_position_to_position(9)
        # Pos 10
        self.action_at_position(10)

        # Check for operation -> MAKE a NEW FUNCTION
        if self.location == 10 and calc.add: # NOT WORKING
            print('added')
            print('--------')

#        print(f'location: {self.location}, x: {self.rect.x}')
#        print(f'locations: {fl.free_location}')

class FreeLocation():
    ''' Handles location related knowledge'''
    def __init__(self):
        self.free_location = [1,2,3,4,5,6,7,8,9,10]
        self.move = 0

    def remove(self, move):
        '''Removes move from location list'''
        self.free_location.remove(move)
        return self.free_location
    
    def return_loc(self, used_loc):
        '''Returns used location to the list'''
        self.free_location.append(used_loc)
        return self.free_location.sort()


class Calculator():
    ''' Does the math'''
    def __init__(self):
        self.total = 0

        self.add = False
        self.subtract = False
        self.multiply = False
        self.divide = False
        self.destroy = False


class Operator(pygame.sprite.Sprite):
    ''' Handles operators and other buttons'''
    def __init__(self, operator):
        super().__init__()
        # Load all operators images
        image_1 = pygame.image.load('images/plus.png').convert_alpha()
        image_2 = pygame.image.load('images/box_1.png').convert_alpha()
        self.operator = operator
        # Dict to store values and images
        images = {'+': image_1, '-': image_2}
        # Set image
        self.image = images[self.operator]
        if self.operator == '+':
            self.rect = self.image.get_rect(topleft=(650,470)) # Draw rectangle


fl = FreeLocation()
calc = Calculator()


pygame.init()
screen = pygame.display.set_mode((1200,800))    # Window size
pygame.display.set_caption('MathHouse')    # Window name
icon = pygame.image.load('images/empty.png')   # Convert icon to surface
pygame.display.set_icon(icon)   # Change icon
clock = pygame.time.Clock() # Object to store time related issues
test_font = pygame.font.Font(None, 50)  # Font type, font size


# Box movement timer 
box_timer = pygame.USEREVENT + 1
pygame.time.set_timer(box_timer,1500)


# Static graphic
background_surf = pygame.image.load('images/background_1.png').convert_alpha()

# Dynamic graphic
box_group = pygame.sprite.Group()    # Create a group for sprite
box_group.add(Box(fl=fl, calc=calc))#Add instance of Box to the group
operator_group = pygame.sprite.Group() # Create a group for operators
operator_group.add(Operator('+')) # Add plus button

while True:
    for event in pygame.event.get():
        # Program exit sequence
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()
        # Add box to box_group
        if event.type == box_timer and len(fl.free_location) > 0:
            box_group.add(Box(fl=fl, calc=calc))
        # Check for operation
        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_PLUS:
            calc.add = True
        if event.type == pygame.KEYUP and event.key == pygame.K_KP_PLUS:
            calc.add = False
        # Testing sequence
#        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#            box_group.add(Box(fl=fl))

    screen.blit(background_surf,(0,0))   # Displays background
    box_group.draw(screen) # Displays box
    box_group.update() # Move box
    operator_group.draw(screen)


#    print(pygame.mouse.get_pos())  # Get mouse position

    pygame.display.update() # Updates screen
    clock.tick(60)  # Set max fps  