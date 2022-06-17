import pygame
import sys
from pygame.locals import *
from ball import Ball
from paddle import Paddle 
from constants import *
from inputs import handle_input





pygame.init()

screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption(" PONG GAME")

clock = pygame.time.Clock()



ball = Ball()
paddle1 = Paddle()
paddle2 = Paddle()
paddle2.rect.x = screenwidth - paddle2.rect.width




game_font = pygame.font.Font("freesansbold.ttf",32)

p_score=[0,0]
ballspeed = 4
font = pygame.font.Font(None,50)

while True:



	clock.tick(tickrate)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT or p_score[0]>=3 or p_score[1]>=3:

			text = font.render(" GAME OVER ", 1 , Black)
			screen.blit(text , (screenwidth//2-100 , screenheight//2))
			pygame.display.flip()
			pygame.time.delay(500)
			pygame.quit()

	handle_input(paddle1,paddle2,ball)


	screen.fill(Yellow)


	ball.draw(screen)
	ball.update(paddle1, paddle2, p_score)
	paddle1.draw(screen)
	paddle2.draw(screen)

	
	text = font.render(str(p_score[0]), 1 , Black)
	screen.blit(text ,(screenwidth//2 - 40 , 20))
	text = font.render(str(p_score[1]), 1 , Black)
	screen.blit(text , (screenwidth // 2 + 40 , 20))

	
	pygame.display.flip()




pygame.quit()

