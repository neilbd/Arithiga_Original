import pygame
from pygame.locals import *
from sys import exit
import os.path as osp

class Ship(pygame.sprite.Sprite):

	def __init__(self, screen, ship_image, x, y):

		pygame.sprite.Sprite.__init__(self)

		self.screen = screen
		self.screen_width, self.screen_height = self.screen.get_size()

		self.image = ship_image
		self.rect = self.image.get_rect()
		self.lives = 3
		self.rect.x = x
		self.rect.y = y

	# Updates location of ship depending on x and 
	def update(self, x, y):

		if y <= 320:
			self.rect.y = 320

		elif y + self.rect.height >= self.screen_height:
			self.rect.y == self.screen_height - self.rect.height

		else:
			self.rect.y = y

		if x + self.rect.width >= self.screen_width:
			self.rect.x = self.screen_width - self.rect.width
		elif x < 0:
			self.rect.x = 0
		else:
			self.rect.x = x

	# Returns current x position of the ship
	def XPosition(self):
		return self.rect.x

	# Returns current y position of the ship
	def YPosition(self):
		return self.rect.y

	def getImage(self):
		return self.rect

	# Returns current number of lives of the ship
	def CurrentLives(self):
		return self.lives

	# Reduces number of lives of the ship when it hits a number or operator
	def ReduceLives(self):
		self.lives -= 1