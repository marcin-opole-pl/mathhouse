import pygame
from random import randint


class Box(pygame.sprite.Sprite):
    def __init__(self, fl):
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
        self.old_location = 0
        self.fl = fl

        
    def return_loc(self, i):
        # Return previous location to the list
        if i not in fl.free_location:
            self.fl.return_loc(i)


    def update(self):
        # Move from pos 0 to 1
        if self.location == 0:
            if 1 in fl.free_location:
                if self.rect.x <= 48:
                    self.rect.x += 2
        # Pos 1
        if self.rect.x == 50 and 1 in fl.free_location:
            fl.remove(1)
            self.location = 1
        # Move from 1 to 2
        if self.location == 1:
            if 2 in fl.free_location:
                if self.rect.x <= 98:
                    self.rect.x += 2
        # Pos 2
        if self.rect.x == 100 and 2 in fl.free_location:
            fl.remove(2)
            self.location = 2
            self.return_loc(1)
        # Move from 2 to 3
        if self.location == 2:
            if 3 in fl.free_location:
                if self.rect.x <= 148:
                    self.rect.x += 2
        # Pos 3
        if self.rect.x == 150 and 3 in fl.free_location:
            fl.remove(3)
            self.location = 3
            self.return_loc(2)
        # Move from 3 to 4
        if self.location == 3:
            if 4 in fl.free_location:
                if self.rect.x <= 198:
                    self.rect.x += 2
        # Pos 4
        if self.rect.x == 200 and 4 in fl.free_location:
            fl.remove(4)
            self.location = 4
            self.return_loc(3)
        # Move from 4 to 5
        if self.location == 4:
            if 5 in fl.free_location:
                if self.rect.x <= 248:
                    self.rect.x += 2
        # Pos 5
        if self.rect.x == 250 and 5 in fl.free_location:
            fl.remove(5)
            self.location = 5
            self.return_loc(4)


        print(f'location: {self.location}, x: {self.rect.x}')
        print(f'locations: {fl.free_location}')

class FreeLocation():
    def __init__(self):
        self.free_location = [1,2,3,4,5,6,7,8,9]
        self.move = 0

    def remove(self, move):
        '''Removes move from location list'''
        self.free_location.remove(move)
        return self.free_location
    
    def return_loc(self, used_loc):
        '''Returns used location to the list'''
        self.free_location.append(used_loc)
        return self.free_location.sort()

fl = FreeLocation()


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
box_group.add(Box(fl=fl))#Add instance of Box to the group

while True:
    for event in pygame.event.get():
        # Program exit sequence
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()
        # Add box to box_group
        if event.type == box_timer and len(fl.free_location) > 0:
            box_group.add(Box(fl=fl))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            box_group.add(Box(fl=fl))


    screen.blit(background_surf,(0,0))   # Displays background
    box_group.draw(screen) # Displays box
    box_group.update() # Move box


#    print(pygame.mouse.get_pos())  # Get mouse position

    pygame.display.update() # Updates screen
    clock.tick(60)  # Set max fps  