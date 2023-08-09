import pygame
from random import randint


class Box(pygame.sprite.Sprite):
    def __init__(self, speed, location):
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
        self.rect = self.image.get_rect(midtop=(105,0)) # Draw rectangle
        self.speed = speed
        self.location = location
        

    def update(self, location):
        if self.rect.y <= 100:
            self.rect.y += self.speed
#            print(self.rect.y)
        if self.rect.y == 102: # for speed 3 must be 102, rest - 104
            if self.rect.x <= 582: # for 3 must be 582, rest - 581
                self.rect.x += self.speed
#                print(self.rect.x)
        if self.rect.x == 585 and self.location == 9:
            if self.rect.y <= 390:
                self.rect.y += self.speed  


class Break(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load('images/test_break.png').convert_alpha()
        self.rect = self.image.get_rect(center=(width, height))

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

# Available max_boxes_number - 10
max_boxes_number = 9

location = 10



# Box movement timer 
box_timer = pygame.USEREVENT + 1
pygame.time.set_timer(box_timer,1500)


# Static graphic
background_surf = pygame.image.load('images/background.png').convert_alpha()
pos_10_block = pygame.image.load('images/horizontal_break.png')

# Dynamic graphic
box_group = pygame.sprite.Group()    # Create a group for sprite
box_group.add(Box(movement_speed(), max_boxes_number))    # Add instance of a Box to the group
break_10 = pygame.sprite.GroupSingle()
break_10.add(Break(610,390))

while True:
    for event in pygame.event.get():
        # Program exit sequence
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()
        # Add box to box_group
        if event.type == box_timer and max_boxes_number > 0:
                box_group.add(Box(movement_speed(), max_boxes_number))
                max_boxes_number -= 1
#                print(max_boxes_number)
    screen.blit(background_surf,(0,0))   # Displays background
    box_group.draw(screen) # Displays box
    box_group.update(max_boxes_number) # Move box
    break_10.draw(screen)
    print(location)

    if pygame.sprite.spritecollide(break_10.sprite, box_group, False):
        location = 9

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        location = 10
        box_group.empty()
#    print(pygame.mouse.get_pos())  # Get mouse position

    pygame.display.update() # Updates screen
    clock.tick(60)  # Set max fps  