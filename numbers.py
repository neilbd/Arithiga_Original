import pygame
from pygame.locals import *
from sys import exit
import os.path as osp

class Numbers(pygame.sprite.Sprite):

	def __init__(self, screen, number_image, value, in_motion):

		pygame.sprite.Sprite.__init__(self)

		self.image = number_image
		self.rect = number_image.get_rect()
		self.value = value
		self.rect.y = 80
		self.rect.x = 0
		self.in_motion = in_motion

# Returns the value of the number
	def getValue(self):
		return self.value
		
# Sets the X Position of the number when Movement is called
	def setXPosition(self, x_position):
		self.rect.x = x_position

	# Returns the x position
	def XPosition(self):
		return self.rect.x

	# Returns the y position
	def YPosition(self):
		return self.rect.y

	def reset(self):
		self.rect.y = 80

	def getImage(self):
		return self.rect

	def toggle(self):

		self.in_motion = True if False else False
		
	def moving(self):
		return self.in_motion

	# Initializes the movement of the number
	def update(self):

		self.rect.y += 1

