# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:19:51 2021

@author: Seren
"""

import sys, pygame
from sys import exit
from paddle import Paddle


def main():
    pygame.init()

    #Definiamo colori e dimensioni
    #size = width, height = 1024, 800
    size = width, height = (700,500)
    speed = [1, 1]
    black = (0,0,0)
    white = (255,255,255)

    #Definiamo la finestra
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")
    
    
    paddleA = Paddle(white, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200
    
    paddleB = Paddle(white, 10, 100)
    paddleB.rect.x = 670
    paddleB.rect.y = 200
    #ball = pygame.image.load("intro_ball.gif")
    #ballrect = ball.get_rect()
    
    #Creazione di una lista che memorizza tutti gli sprite che creeremo nel gioco (ossia 2)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    
    
    #Il loop va avanti finchè l'utente non esce dal gioco 
    carryOn = True
    clock = pygame.time.Clock() #verrà usato per controllare quanto velocemente si aggiorna lo screen

    while carryOn:
        
        #Qui viene gestito il clic sulla "X" che chiude la finestra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                pygame.quit()
                exit()
                
            #In questo modo si riesce a spostare il paddle A con le frecce (su e giù)    
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         paddleA.rect.y -= 3
            #     if event.key == pygame.K_DOWN:
            #         paddleA.rect.y += 3
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddleB.moveUp(6)
            if keys[pygame.K_s]:
                paddleB.moveDown(6)
            if keys[pygame.K_UP]:
                paddleA.moveUp(6)
            if keys[pygame.K_DOWN]:
                paddleA.moveDown(6)
           
            

        all_sprites_list.update()

        # ballrect = ballrect.move(speed)
        # if ballrect.left < 0 or ballrect.right > width:
        #     speed[0] = -speed[0]
        # if ballrect.top < 0 or ballrect.bottom > height:
        #     speed[1] = -speed[1]

        screen.fill(black)
        pygame.draw.line(screen, white, [349, 0], [349, 500], 5)
        all_sprites_list.draw(screen)
        #screen.blit(ball, ballrect)
        pygame.display.flip()
       
        #Limite a 90 frame per secondo
        clock.tick(90)

pygame.quit()
if __name__ == '__main__':
    main()
