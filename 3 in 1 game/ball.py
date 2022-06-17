import pygame
import random 
from constants import *
class Ball:

	def __init__(self):
		self.x = screenwidth // 2
		self.y = screenheight // 2
		self.speed =5
		self.vx = self.speed
		self.vy = self.speed
		self.radius = 10

	def get_rect(self):
		return pygame.Rect(self.x - self.radius , self.y - self.radius , self.radius*2 , self.radius * 2)	

	def draw(self,screen):
		pygame.draw.circle(screen, Black ,(self.x , self.y), self.radius)



	def update(self, paddle1 , paddle2 , p_score):

		self.x += self.vx
		self.y += self.vy
				
		if self.y > screenheight - self.radius * 2:
			self.vy *= -1

		if self.y < self.radius *2:
			self.vy *= -1

		if self.x > screenwidth - self.radius * 2:
			p_score[0] += 1
			self.vx *= -1
		
		if self.x < self.radius * 2:
			p_score[1] += 1
			self.vx *= -1
			
		if self.get_rect().colliderect(paddle1.rect):
			self.vx *= -1

		if self.get_rect().colliderect(paddle2.rect):
			self.vx *= -1



