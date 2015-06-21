from ship import Ship
from numbers import Numbers
from operators import Operators
from laser import LaserFactory

import pygame
from pygame.locals import *
from sys import exit
import os.path as osp

import json

from random import *

class GalagaVariant: # tentative title

    def __init__(self):

        pygame.init()

        pygame.mixer.init()

        pygame.display.set_caption("To Be Titled") # Will have an official title later

        self.screen = pygame.display.set_mode((640,480),0,32)

        self.screen.fill([0, 0, 0]) # background will be black

    # Parameter testing, not used for now
    def Parameters(self):

        # self.background_color
        # self.number_font
        # self.chosen_number_colors (array)
        # self.avatar
        # self.final_laser_choice

        selection_font = pygame.font.SysFont('arial', 20)

        intro_directions = selection_font.render("Press the n key to cycle through the options", True, (250, 50, 0), (0, 0, 0))
        intro_directions2 = selection_font.render("Press the space key to select your choice or continue", True, (250, 50, 0), (0,0,0))
        intro_directions3 = selection_font.render("To the next screen", True, (250, 50, 0), (0,0,0))

        pygame.display.flip()

        while True:

            self.screen.blit(intro_directions, (125, 100))
            self.screen.blit(intro_directions2, (75, 150))
            self.screen.blit(intro_directions3, (220, 200))
            pygame.display.flip()

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_SPACE:
                    break

            self.screen.fill([0,0,0])

        self.screen.fill([0,0,0])

        parameter_objects = []

        parameter_count = 0

        parameters = open('parameter_storage.json').read()

        parameter_objects = (json.loads(parameters))
        parameter_count += 1

        selection_font = pygame.font.SysFont('arial', 20)

        background_colors = [(0,0,0), (255, 212, 0), (255, 157, 255), (106, 185, 132), (255, 255, 255), (255, 255, 0)]

        which_back_color = selection_font.render("Which background color would you like to use?", True, (250, 50, 0), (0, 0, 0))

        pygame.display.flip()
        locations = [100, 200, 300, 400, 500, 600]
        option = 0
        back_color_count = 0

        while True:

            self.screen.blit(which_back_color, (100, 100))

            count = 0
            
            for color in background_colors:
                count += 1
                pygame.draw.rect(self.screen, color, pygame.Rect(100 * count, 300, 30, 30))

            pygame.draw.circle(self.screen, (255, 255, 255), (locations[option], 300), 3)
            pygame.display.update()

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_n:
                    self.screen.fill([0,0,0])
                    back_color_count += 1

                    if back_color_count == 6:
                        option = 0
                        back_color_count = 0

                    else:
                        option += 1

                if event.key is K_SPACE:
                    self.background_color = background_colors[option]
                    break

        self.screen.fill([0,0,0])

        font_choices = ['impact', 'arial', 'silom', 'corbel', 'optima']

        option = 0
        font_count = 0

        while True:

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_n:
                    self.screen.fill([0,0,0])

                    font_count += 1

                    if font_count == 5:
                        option = 0
                        font_count = 0

                    else:
                        option += 1

                if event.key is K_SPACE:
                    self.number_font = font_choices[option]
                    break

            which_font = selection_font.render("Which font do you want to use for the numbers?", True, (200, 50, 0), (0, 0, 0))

            current_font = pygame.font.SysFont(font_choices[option], 20)

            number = current_font.render('5', True, (200, 50, 0), (0, 0, 0))

            self.screen.blit(which_font, (50, 100))

            self.screen.blit(number, (300, 300))
            
            pygame.display.update()

        number_colors = [(255, 255, 255), (255, 212, 0), (255, 157, 255), (106, 185, 132), (0,0,0), (255, 255, 0), (201, 103, 255), (233, 54, 0), (0, 247, 194), (216, 164, 95), (73, 133, 246)]

        self.chosen_number_colors = []

        self.final_number_font = pygame.font.SysFont(self.number_font, 20)

        number_color_counter = 0

        for number in range(0,10):

            self.screen.fill([0,0,0])
            option = 0

            while True:

                event = pygame.event.wait()

                if event.type is pygame.QUIT:
                    sys.exit()

                if event.type is pygame.KEYDOWN:

                    if event.key is K_n:
                        self.screen.fill([0,0,0])

                        number_color_counter += 1
                        

                        if number_color_counter == 11:
                            option = 0
                            number_color_counter = 0

                        else:
                            option += 1

                    if event.key is K_SPACE:
                        self.chosen_number_colors.append(number_colors[option])
                        break

                which_number_color = selection_font.render("For each number, what color do you want?", True, (200, 50, 0), (0, 0, 0))

                self.screen.blit(which_number_color, (50, 100))

                the_number = self.final_number_font.render(str(number), True, number_colors[option], self.background_color)
                self.screen.blit(the_number, (300, 300))
                pygame.display.update()

        self.screen.fill([0,0,0])
        # Select the type of ship you want

        ship_option = pygame.image.load("galaga-ship.jpg").convert_alpha()
        bug_option = pygame.image.load("bug.jpg").convert_alpha()
        ghost_option = pygame.image.load("ghost.jpg").convert_alpha()

        avatar_options = [ship_option, bug_option, ghost_option]

        locations = [150, 300, 450]
        option = 0
        avatar_count = 0

        while True:

            which_avatar = selection_font.render("Which avatar would you like to use?", True, (200, 50, 0), (0, 0, 0))

            self.screen.blit(which_avatar, (100, 100))

            count = 0
            for avatar in avatar_options:
                count += 1
                self.screen.blit(avatar_options[count - 1], (150 * count, 300))

            pygame.draw.circle(self.screen, (255, 255, 255), (locations[option], 300), 3)

            pygame.display.flip()

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_n:
                    avatar_count += 1
                    if avatar_count == 3:
                        option = 0
                        avatar_count = 0

                    else:
                        option += 1

                if event.key is K_SPACE:
                    self.avatar = avatar_options[option]
                    break

            self.screen.fill([0,0,0])

        self.screen.fill([0,0,0])

        square_green_option = pygame.image.load("squaregreenlaser.png").convert_alpha()

        long_green_option = pygame.image.load("longgreenlaser.png").convert_alpha()

        square_or_long = [square_green_option, long_green_option]

        locations = [200, 400]
        option = 0
        laser_count = 0

        while True:

            which_laser = selection_font.render("Which laser would you like to use?", True, (200, 50, 0), (0, 0, 0))

            self.screen.blit(which_laser, (100, 100))

            count = 0

            for laser in square_or_long:
                count += 1
                self.screen.blit(square_or_long[count - 1], (200 * count, 300))

            pygame.draw.circle(self.screen, (255, 255, 255), (locations[option], 300), 3)

            pygame.display.flip()

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                sys.exit()

            if event.type is pygame.KEYDOWN:

                if event.key is K_n:
                    laser_count += 1
                    if laser_count == 2:
                        option = 0
                        laser_count = 0

                    else:
                        option += 1

                if event.key is K_SPACE:
                    self.laser_choice = square_or_long[option]
                    break

            self.screen.fill([0,0,0])

        if self.laser_choice is square_green_option:
            
            square_blue_option = pygame.image.load("squarebluelaser.png").convert_alpha()
            square_yellow_option = pygame.image.load("squareyellowlaser.png").convert_alpha()
            square_red_option = pygame.image.load("squareredlaser.png").convert_alpha()

            square_lasers = [square_green_option, square_blue_option, square_red_option, square_yellow_option]

            self.screen.fill([0,0,0])

            locations = [100, 200, 300, 400]
            option = 0
            laser_count = 0

            while True:

                which_color = selection_font.render("Which color would you like to use?", True, (200, 50, 0), (0, 0, 0))

                self.screen.blit(which_color, (100, 100))

                count = 1
                for color in square_lasers:
                    self.screen.blit(color, (100 * count, 300))
                    count += 1

                pygame.draw.circle(self.screen, (255, 255, 255), (locations[option], 300), 3)

                pygame.display.flip()

                event = pygame.event.wait()

                if event.type is pygame.QUIT:
                    sys.exit()

                if event.type is pygame.KEYDOWN:

                    if event.key is K_n:
                        laser_count += 1
                        if laser_count == 4:
                            option = 0
                            laser_count = 0

                        else:
                            option += 1

                    if event.key is K_SPACE:
                        self.final_laser_choice = square_lasers[option]
                        break

                self.screen.fill([0,0,0])

        elif self.laser_choice is long_green_option:
            
            long_blue_option = pygame.image.load("longbluelaser.png").convert_alpha()
            long_red_option = pygame.image.load("longredlaser.png").convert_alpha()
            long_yellow_option = pygame.image.load("longyellowlaser.png").convert_alpha()

            long_lasers = [long_green_option, long_blue_option, long_red_option, long_yellow_option]

            self.screen.fill([0,0,0])

            locations = [100, 200, 300, 400]
            option = 0
            laser_count = 0

            while True:

                which_color = selection_font.render("Which color would you like to use?", True, (200, 50, 0), (0, 0, 0))

                self.screen.blit(which_color, (100, 100))

                count = 0
                for color in long_lasers:
                    count += 1
                    self.screen.blit(long_lasers[count - 1], (100 * count, 300))

                pygame.draw.circle(self.screen, (255, 255, 255), (locations[option], 300), 3)

                pygame.display.flip()

                event = pygame.event.wait()

                if event.type is pygame.QUIT:
                    sys.exit()

                if event.type is pygame.KEYDOWN:

                    if event.key is K_n:
                        laser_count += 1
                        if laser_count == 4:
                            option = 0
                            laser_count = 0

                        else:
                            option += 1

                    if event.key is K_SPACE:
                        self.final_laser_choice = long_lasers[option]
                        break

                self.screen.fill([0,0,0])

        self.initialize()

    def initialize(self):

        # Sets up the numbers and operators that move down the screen.

        self.answer_numbers = [4, 13, 21, 34, 48, 64, 85, 110] # possible answers for game, ideally will randomize in final game

        # Creates objects for each number
        self.number_objects = []

        for number in range(0,10):

            image = self.final_number_font.render(str(number), True, self.chosen_number_colors[number])
            new_number = Numbers(self.screen, image, number, False)
            self.number_objects.append(new_number)

        plus_image = pygame.image.load("plussymbol.png").convert_alpha()
        minus_image = pygame.image.load("minussymbol.png").convert_alpha()
        multiply_image = pygame.image.load("multiplysymbol.png").convert_alpha()
        divide_image = pygame.image.load("dividesymbol.png").convert_alpha()
        power_image = pygame.image.load("caret.png").convert_alpha()

        # Creates objects for each operator (may remove minus and divide)
        self.plus = Operators(self.screen, plus_image, '+', False)
        self.minus = Operators(self.screen, minus_image, '-', False)
        self.multiply = Operators(self.screen, multiply_image, '*', False)
        self.divide = Operators(self.screen, divide_image, '/', False)
        self.power = Operators(self.screen, power_image, '^', False)

        # A lot of initializations
        self.hit_number = False

        self.hit_operator = False

        self.points = 0

        self.temporary_operator = '+' # Initalizes the operator

        self.answer_numbers_index = 0 # Defines current answer player strives for. Increments everytime the correct answer is chosen

        self.accumulating_answer = 0 # Keeps track of current value user calculates after shooting the numbers and operators.

        self.number_operators_used = 0 # Keeps track of number of operators used (for points)

        self.random_operator_count = 0  # Determines when operator will appear, spaces them out with 

        self.random_number_count = 0

        self.x = 319
        self.y = 350

        self.player_ship = Ship(self.screen, self.avatar, self.x, self.y)

        self.ships = pygame.sprite.Group()
        self.ships.add(self.player_ship)

        self.moving_numbers = pygame.sprite.Group()
        self.moving_operators = pygame.sprite.Group()
        self.moving_laser = LaserFactory(self.screen, self.final_laser_choice)

        self.introMenu()

    # Conducts operation of inputed values
    def Operation(self, temporary_operator, temporary_number_one, temporary_number_two):

        if temporary_operator == '+':
            return (temporary_number_one + temporary_number_two)
        elif temporary_operator == '-':
            return (temporary_number_one - temporary_number_two)
        elif temporary_operator == '*':
            return (temporary_number_one * temporary_number_two)
        elif temporary_operator == '/':
            return (temporary_number_one / temporary_number_two)
        else:
            return (temporary_number_one ** temporary_number_two)

    def introMenu(self):

        self.screen.fill(self.background_color)

        font = pygame.font.SysFont('impact', 40)

        text = font.render("To Be Titled", True, (200, 50, 0))

        self.screen.blit(text, (250, 50))

        font2 = pygame.font.SysFont('arial', 25)
        text2 = font2.render("Press the Space to Start", True, (200, 50, 0))

        self.screen.blit(text2, (250, 240))

        pygame.display.flip()

        while True:
    
            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.Directions()

    def endGame(self):

        self.screen.fill(self.background_color)

        end_font = pygame.font.SysFont('arial', 25)
        end_text = end_font.render("Game Over", True, (200, 50, 0))

        continue_text = end_font.render("Press f to Continue", True, (200, 50, 0))
        quit_text = end_font.render("Press q to Quit", True, (200, 50, 0))

        self.screen.blit(end_text, (310, 180))

        pygame.display.flip()

        pygame.time.wait(1100)

        self.screen.blit(continue_text, (310, 211))

        self.screen.blit(quit_text, (310, 250))

        pygame.display.flip()

        while True:

            event = pygame.event.wait()

            if event.type is pygame.KEYDOWN:

                if event.key is pygame.K_f:
                    self.initialization()

                if event.key is pygame.K_q:
                    sys.exit()

            if event.type is pygame.QUIT:
                sys.exit()

    def Directions(self):

        self.screen.fill(self.background_color)

        directions_font = pygame.font.SysFont('arial', 15)\
        
        direction_text = directions_font.render("Move the Mouse to Move the Ship, Press it To Shoot A Laser", True, (200,50,0))

        direction_text2 = directions_font.render("Shoot The Numbers and Operators to Get the Given Number!", True, (200, 50, 0))

        direction_text3 = directions_font.render("The Less Operators You Use, the More Points You'll Get", True, (200,50,0))

        direction_text4 = directions_font.render("You Have Three Lives", True, (200, 50, 0))

        self.screen.blit(direction_text, (100, 140))

        self.screen.blit(direction_text2, (100, 160))

        self.screen.blit(direction_text3, (100, 180))

        self.screen.blit(direction_text4, (100, 200))

        pygame.display.flip()

        while True:
    
            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.run()

    # Updates info on top of the screen.
    def changeInfo(self):

        info_font = pygame.font.SysFont('arial', 18)
        answer_text = info_font.render("Current Number: " + str(self.answer_numbers[self.answer_numbers_index]), True, (200, 50, 0))

        self.screen.blit(answer_text, (325, 40))

        number_of_lives_text = info_font.render("Current Lives: " + str(self.player_ship.CurrentLives()), True, (200,50,0))
        self.screen.blit(number_of_lives_text, (180, 40))

        accumulating_text = info_font.render("Current Result: " + str(self.accumulating_answer), True, (200, 50, 0))

        self.screen.blit(accumulating_text, (25, 40))

        points_text = info_font.render("Current Points: " + str(self.points), True, (200,50,0))
        self.screen.blit(points_text, (490, 40))

    # Runs the game
    def run(self):

        pygame.time.set_timer(pygame.USEREVENT, 50)

        self.screen.fill(self.background_color)

        while True:

            event = pygame.event.wait()

            if event.type is pygame.QUIT:
                print 'quit'
                sys.exit()

            # Movement of mouse determines movement of spaceship
            if event.type is pygame.MOUSEMOTION:
                self.x, self.y = pygame.mouse.get_pos()
                self.player_ship.update(self.x, self.y)

            # Determines shooting the laser
            if event.type is pygame.MOUSEBUTTONDOWN:

                self.moving_laser.NewLaser(self.player_ship.XPosition(), self.player_ship.YPosition())
            
            if event.type is not pygame.USEREVENT:
                continue

            for laser in self.moving_laser.getLasers():

                if laser.YPosition() == 80:
                    self.moving_laser.getLasers().remove(laser)

                else:
                    laser.update()

            random_value = int(random() * 9.9)  # Randomizes what number appears at the top
            
            random_operator = random() * 5  # Randomizes what operator appears at the top

            start_position_operator = 610.0 * random() # Randomizes where the number will appear at the top

            start_position_number = 610.0 * random() # Randomizes where the operator will appear at the top

            # For loop instead?

            self.random_number_count += 1
                
            # Series of if-else statements to initalize movment of a number given the random value

            if self.random_number_count == 4:

                self.random_number_count = 0

                if (not self.number_objects[random_value].moving()):
                    self.number_objects[random_value].setXPosition(start_position_number)
                    self.moving_numbers.add(self.number_objects[random_value])
                    self.number_objects[random_value].toggle()

            for number in self.moving_numbers:

                if number.YPosition() > 480:
                    number.reset()
                    self.moving_numbers.remove(number)
                    number.toggle()
                    
                else:
                    number.update()

            self.random_operator_count += 1  # Increments count

            # Initalizes movement of an operator everytime random_operator_count is 3
            if self.random_operator_count == 6:

                self.random_operator_count = 0

                if (not self.plus.moving()) and random_operator > 0 and random_operator <= 1:
                    self.plus.setXPosition(start_position_operator)
                    self.moving_operators.add(self.plus)
                    self.plus.toggle()

                elif (not self.minus.moving()) and random_operator > 1 and random_operator <= 2:
                    self.minus.setXPosition(start_position_operator)
                    self.moving_operators.add(self.minus)
                    self.minus.toggle()

                elif (not self.multiply.moving()) and random_operator > 2 and random_operator <= 3:
                    self.multiply.setXPosition(start_position_operator)
                    self.moving_operators.add(self.multiply)
                    self.multiply.toggle()

                elif (not self.divide.moving()) and random_operator > 3 and random_operator <= 4:
                    self.divide.setXPosition(start_position_operator)
                    self.moving_operators.add(self.divide)
                    self.divide.toggle()

                elif (not self.power.moving()) and random_operator > 4 and random_operator <= 5:
                    self.power.setXPosition(start_position_operator)
                    self.moving_operators.add(self.power)
                    self.power.toggle()

            for operator in self.moving_operators:

                if operator.YPosition() > 480:
                    operator.reset()
                    self.moving_operators.remove(operator)
                    operator.toggle()

                else:
                    operator.update()


            # Take into account the first number that is shot, should only occur once
            # For every answer
            if ((not self.hit_number) and (not self.hit_operator)):

                for laser in self.moving_laser.getLasers():
                    
                   laser_number_collision = pygame.sprite.spritecollide(laser, self.moving_numbers, True)

                   for number in laser_number_collision:
                       self.moving_laser.getLasers().remove(laser)
                       self.accumulating_answer = number.getValue()
                       number.reset()
                       number.toggle()
                       self.hit_number = True

            # Shoots operator after hit the number
            elif self.hit_number:

                if not self.hit_operator:

                    for laser in self.moving_laser.getLasers():

                        laser_operator_collision = pygame.sprite.spritecollide(laser, self.moving_operators, True)
                          
                        for operator in laser_operator_collision:
                            operator.toggle()
                            operator.reset()
                            self.moving_laser.getLasers().remove(laser)
                            self.temporary_operator = operator.getOperator()
                            self.hit_operator = True
                            self.number_operators_used += 1

                # Shoot another number
                elif self.hit_operator:

                    for laser in self.moving_laser.getLasers():
                            
                        laser_number_collision = pygame.sprite.spritecollide(laser, self.moving_numbers, True)

                        for number in laser_number_collision:
                           self.moving_laser.getLasers().remove(laser)
                           self.accumulating_answer = self.Operation(self.temporary_operator, self.accumulating_answer, number.getValue())
                           number.reset()
                           number.toggle()
                           self.hit_operator = False  # Only changes operator to false so user can build upon the accumulating number

            # Moves on to the next number as an answer if the accumulating_answer equals to the given number.
            # Calculates points depending on how many operators are used.
            if self.accumulating_answer == self.answer_numbers[self.answer_numbers_index]:

                self.accumulating_answer = 0

                self.answer_numbers_index += 1

                self.hit_number = False

                if (self.number_operators_used > 0) and (self.number_operators_used <= 2):
                    self.points += 100

                elif (self.number_operators_used > 2) and (self.number_operators_used <= 5):
                    self.points += 50

                else:
                    self.points += 25

                # Reduce the number of lives everytime the ship hits a number or operator
            ship_number_collisions = pygame.sprite.spritecollide(self.player_ship, self.moving_numbers, True)

            for number in ship_number_collisions:

                print self.player_ship.CurrentLives()
                self.player_ship.ReduceLives()
                number.toggle()
                number.reset()
                self.moving_numbers.remove(number)
                self.accumulating_answer = 0
                self.hit_number = False
                self.hit_operator = False

                pygame.time.delay(1000)
                self.x = 319
                self.y = 350

                # Reduce the number of lives everytime the ship hits a number or operator
            ship_operator_collisions = pygame.sprite.spritecollide(self.player_ship, self.moving_operators, True)

            for operator in ship_operator_collisions:
                print self.player_ship.CurrentLives()
                self.player_ship.ReduceLives()
                self.accumulating_answer = 0
                operator.toggle()
                operator.reset()
                self.moving_operators.remove(operator)
                self.hit_number = False
                self.hit_operator = False

                pygame.time.delay(1000)
                self.x = 319
                self.y = 350

            # Ends game when the player runs out of lives
            if self.player_ship.CurrentLives() == 0:
                break

            self.ships.draw(self.screen)
            self.moving_numbers.draw(self.screen)
            self.moving_operators.draw(self.screen)
            self.moving_laser.getLasers().draw(self.screen)

            self.changeInfo()

            pygame.display.flip()

            self.screen.fill(self.background_color)

        self.endGame()

if __name__ == '__main__':

    GalagaVariant().Parameters()

