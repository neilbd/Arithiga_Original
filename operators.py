import pygame
from pygame.locals import *
from sys import exit
import os.path as osp

class Operators(pygame.sprite.Sprite):

	def __init__(self, screen, operator_image, operation, in_motion):

		pygame.sprite.Sprite.__init__(self)

		self.screen = screen
		self.image = operator_image
		self.rect = self.image.get_rect()
		self.operator = operation
		self.rect.y = 80
		self.rect.x = 0
		self.in_motion = in_motion

	# Gets the operator of the object (is registered as a character)
	def getOperator(self):
		return self.operator

	# Sets the x position of the operator
	def setXPosition(self, x_position):
		self.rect.x = x_position

	def getImage(self):
		return self.rect

	# Returns the y position of the operator
	def YPosition(self):
		return self.rect.y

	# Returns the x position of the operator
	def XPosition(self):
		return self.rect.x

	def reset(self):
		self.rect.y = 80

	def toggle(self):
		
		self.in_motion = True if False else False

	def moving(self):
		return self.in_motion

	# Moves the object
	def update(self):

		self.rect.y += 1
		