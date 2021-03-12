# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:19:51 2021

@author: Seren
"""

import sys, pygame
from sys import exit


def main():
    pygame.init()

    #Definiamo colori e dimensioni
    size = width, height = 1024, 800
    speed = [1, 1]
    black = (0,0,0)
    white = (255,255,255)

   #Definiamo la finestra
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")
    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()
    
    #Il loop va avanti finchè l'utente non esce dal gioco 
    carryOn = True
    clock = pygame.time.Clock() #verrà usato per controllare quanto velocemente si aggiorna lo screen

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                pygame.quit()
                exit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.QUIT:
            #         pygame.display.quit()
            #         quit_game()
                # poi qua ci si mette il codice per gestire gli altri possibili keypress

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()
       
        #Limite a 90 frame per secondo
        clock.tick(90)

pygame.quit()
if __name__ == '__main__':
    main()
