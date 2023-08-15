import pygame
from random import randint


class Box(pygame.sprite.Sprite):
    ''' Operates boxes behavior'''
    def __init__(self, fl, calc):
        super().__init__()
        # Load all box images
        image_0 = pygame.image.load('images/box_0.png').convert_alpha()
        image_1 = pygame.image.load('images/box_1.png').convert_alpha()
        image_2 = pygame.image.load('images/box_2.png').convert_alpha()
        image_3 = pygame.image.load('images/box_3.png').convert_alpha()
        image_4 = pygame.image.load('images/box_4.png').convert_alpha()
        image_5 = pygame.image.load('images/box_5.png').convert_alpha()
        image_6 = pygame.image.load('images/box_6.png').convert_alpha()
        image_7 = pygame.image.load('images/box_7.png').convert_alpha()
        image_8 = pygame.image.load('images/box_8.png').convert_alpha()
        image_9 = pygame.image.load('images/box_9.png').convert_alpha()

        # Randomize value of the box
        self.value = randint(0,9)
        # Dict to store values and images
        images = {
            0: image_0,
            1: image_1,
            2: image_2,
            3: image_3,
            4: image_4,
            5: image_5,
            6: image_6,
            7: image_7,
            8: image_8,
            9: image_9
        }
        # Set image
        self.image = images[self.value]
        self.rect = self.image.get_rect(midleft=(-80,400)) # Draw rectangle

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
        if self.location == 0:
            if (1) in fl.free_location:
                if self.rect.x <= -50:
                    self.rect.x += self.speed
        # Pos 1
        if self.rect.x == -50 and 1 in fl.free_location:
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

        # Check for operation
        if self.location == 10 and calc.add:
            calc.adding(self.value)
            self.return_loc(10)
            self.kill()
        if self.location == 10 and calc.subtract:
            calc.subtracting(self.value)
            self.return_loc(10)
            self.kill()
        if self.location == 10 and calc.multiply:
            calc.multiplying(self.value)
            self.return_loc(10)
            self.kill()
        if self.location == 10 and calc.divide:
            calc.dividing(self.value)
            self.return_loc(10)
            self.kill()


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
        self.errors = 0

        self.add = False
        self.subtract = False
        self.multiply = False
        self.divide = False
        self.destroy = False

    def adding(self, box_value):
        self.total += box_value
        return self.total
        
    def subtracting(self, box_value):
        self.total -= box_value
        return self.total
    
    def multiplying(self, box_value):
        self.total *= box_value
        return self.total

    def dividing(self, box_value):
        try:
            result = self.total / box_value
            rest = self.total % box_value
            # If no reminder
            if rest == 0:
                return result
            # If reminder exists
            else:
                self.errors = 1
                return self.total
        except ZeroDivisionError:
            self.errors = 2
            return self.total

    def display_errors(self):
        if self.errors == 1:
            error1_surf = font_small_extra.render\
                ('Division with remainders', True, 'Red').convert_alpha()
            error1_rect = error1_surf.get_rect(topleft=(680,380))
            screen.blit(error1_surf, error1_rect)
        if self.errors == 2:
            error1_surf = font_small_extra.render('Division by 0 !!!', True, 'Red')\
                .convert_alpha()
            error1_rect = error1_surf.get_rect(topleft=(680,380))
            screen.blit(error1_surf, error1_rect)

    def display_total(self):
        ''' Display total on machine'''
        if self.total < 1000000:
            total_surf = font.render(f'{self.total}', True, 'darkolivegreen1')\
            .convert_alpha()
            total_rect = total_surf.get_rect(topleft=(680,310))
            screen.blit(total_surf, total_rect)
        if self.total >= 1000000:
            error1_surf = font_small.render('999 999', True, 'Red').convert_alpha()
            error1_rect = error1_surf.get_rect(topleft=(680,320))
            screen.blit(error1_surf, error1_rect)
            error2_surf = font_small.render('limit', True, 'Red').convert_alpha()
            error2_rect = error2_surf.get_rect(topleft=(680,360))
            screen.blit(error2_surf, error2_rect)
            error3_surf = font_small.render('exceeded', True, 'Red').convert_alpha()
            error3_rect = error3_surf.get_rect(topleft=(680,400))
            screen.blit(error3_surf, error3_rect)


class Operator():
    ''' Handles operators and other buttons'''
    def __init__(self):
        super().__init__()
        # TO DO

class Conveyor(pygame.sprite.Sprite):
    ''' Conveyor'''
    def __init__(self):
        super().__init__()
        # Load frames
        frame_1 = pygame.image.load('images/conveyor_1.png').convert_alpha()
        frame_2 = pygame.image.load('images/conveyor_2.png').convert_alpha()
        frame_3 = pygame.image.load('images/conveyor_3.png').convert_alpha()
        frame_4 = pygame.image.load('images/conveyor_2.png').convert_alpha()

        self.frames = [frame_1, frame_2, frame_3, frame_4]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomleft=(-5,460))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):# If index exceeds list len
            self.animation_index = 0 # Set index to 0
        self.image = self.frames[int(self.animation_index)] # Pick image
    
    def update(self):
        self.animation_state()


fl = FreeLocation()
calc = Calculator()



pygame.init()
screen = pygame.display.set_mode((1200,800))    # Window size
pygame.display.set_caption('MathHouse')    # Window name
icon = pygame.image.load('images/empty.png')   # Convert icon to surface
pygame.display.set_icon(icon)   # Change icon
clock = pygame.time.Clock() # Object to store time related issues
font = pygame.font.Font('The Led Display St.ttf', 50) # Font type, font size
font_small = pygame.font.Font('The Led Display St.ttf', 30) # Font type, font size
font_small_extra = pygame.font.Font('The Led Display St.ttf', 12) # Font type, font size


# Box movement timer 
box_timer = pygame.USEREVENT + 1
pygame.time.set_timer(box_timer,2000)


# Static graphic
background_surf = pygame.image.load('images/background_1.png').convert_alpha()
machine_surf = pygame.image.load('images/machine.png').convert_alpha()


# Dynamic graphic
box_group = pygame.sprite.Group()    # Create a group for sprite
box_group.add(Box(fl=fl, calc=calc))#Add instance of Box to the group
conveyor_group = pygame.sprite.GroupSingle() # Create a group for conveyor
conveyor_group.add(Conveyor()) # Add conveyor

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
        if event.type == pygame.KEYDOWN:
            calc.errors = 0 # Reset error message
            if event.key == pygame.K_KP_PLUS:
                calc.add = True
            if event.key == pygame.K_KP_MINUS:
                calc.subtract = True
            if event.key == pygame.K_KP_MULTIPLY:
                calc.multiply = True
            if event.key == pygame.K_KP_DIVIDE:
                calc.divide = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP_PLUS:
                calc.add = False
            if event.key == pygame.K_KP_MINUS:
                calc.subtract = False
            if event.key == pygame.K_KP_MULTIPLY:
                calc.multiply = False
            if event.key == pygame.K_KP_DIVIDE:
                calc.divide = False
        # Testing sequence
#        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#            box_group.add(Box(fl=fl))

    screen.blit(background_surf,(0,0)) # Displays background
    conveyor_group.draw(screen)
    if len(fl.free_location) > 0:
        conveyor_group.update()
    box_group.draw(screen) # Displays box
    box_group.update() # Move box
    screen.blit(machine_surf, (660,310)) # Display machine
    calc.display_total()
    calc.display_errors()


#    print(pygame.mouse.get_pos())  # Get mouse position

    pygame.display.update() # Updates screen
    clock.tick(60)  # Set max fps  