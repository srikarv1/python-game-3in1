import pygame 
from constants import *
class Paddle:
	def __init__(self):
		self.rect = pygame.Rect(0, screenheight // 2 - paddleheight / 2, paddlewidth, paddleheight)
		self.speed = 6

	def draw(self,screen):
		pygame.draw.rect(screen, Red , self.rect)

	def move_up(self):
		self.rect.y -= self.speed
		self.keep_in_bounds()

	def move_down(self):
		self.rect.y += self.speed
		self.keep_in_bounds()

	def keep_in_bounds(self):
		self.rect.y = min(self.rect.y , screenheight - self.rect.height)
		self.rect.y = max(0 , self.rect.y)
 


	