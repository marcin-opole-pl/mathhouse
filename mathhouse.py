import pygame
from random import randint


class Box(pygame.sprite.Sprite):
    def __init__(self, speed):
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
        self.rect = self.image.get_rect(midtop=(0,400)) # Draw rectangle
        self.speed = speed
        self.locations = {1: (105,0)}
        

    def update(self):
        if self.rect.x <= 100:
            self.rect.x += self.speed


class FreeLocation:
    def __init__(self):
        self.free_location = 1

free_location = FreeLocation()

def movement_speed(): # 1, 2 or 3
    speed = 3
    return speed

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
box_group.add(Box(movement_speed()))#Add instance of Box to the group

while True:
    for event in pygame.event.get():
        # Program exit sequence
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()
        # Add box to box_group
        if event.type == box_timer:
                box_group.add(Box(movement_speed()))

    screen.blit(background_surf,(0,0))   # Displays background
    box_group.draw(screen) # Displays box
    box_group.update() # Move box


#    print(pygame.mouse.get_pos())  # Get mouse position

    pygame.display.update() # Updates screen
    clock.tick(60)  # Set max fps  