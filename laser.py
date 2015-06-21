import pygame
from pygame.locals import *
from sys import exit
import os.path as osp

class Laser(pygame.sprite.Sprite):

	def __init__(self, screen, laser_image, x, y):

		pygame.sprite.Sprite.__init__(self)

		self.screen = screen
		self.image = laser_image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	# Returns the current x position of the laser
	def XPosition(self):
		return self.rect.x

	def getImage(self):
		return self.rect
		
	# Returns the current y position of the laser
	def YPosition(self):
		return self.rect.y
		
	# Moves the laser
	def update(self):
		self.rect.y -= 1

class LaserFactory(object):

	def __init__(self, screen, image):
		self.moving_lasers = pygame.sprite.Group()
		self.screen = screen
		self.image = image

	def NewLaser(self, x, y):
		new_laser = Laser(self.screen, self.image, x, y)
		self.moving_lasers.add(new_laser)

	def getLasers(self):
		return self.moving_lasers
