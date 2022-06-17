import pygame 
from pygame.locals import *
from paddle import Paddle
from ball import Ball

def handle_input(paddle1, paddle2,ball):
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if keys[K_w]:
        paddle1.move_up()
        
    
    if keys[K_s]:
        paddle1.move_down()

    if paddle2.rect.y < ball.y and abs(paddle2.rect.y - ball.y) > 10:
        paddle2.move_down()
    elif paddle2.rect.y > ball.y and abs(paddle2.rect.y - ball.y) > 10:
        paddle2.move_up()

