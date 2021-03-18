# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:19:51 2021

@author: Seren
"""

import sys, pygame
from sys import exit

from ball import Ball
from paddle import Paddle


def main():
    pygame.init()

    # Definiamo colori e dimensioni
    # size = width, height = 1024, 800
    size = pygame.Rect(0, 0, 800, 600)
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Definiamo la finestra
    screen = pygame.display.set_mode((size.width, size.height))
    pygame.display.set_caption("Pong")

    paddleA = Paddle(white, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = (size.height - 100) / 2

    paddleB = Paddle(white, 10, 100)
    paddleB.rect.x = size.width - 10 - 20
    paddleB.rect.y = (size.height - 100) / 2

    ball = Ball(12)
    # ball = pygame.image.load("intro_ball.gif")
    # ballrect = ball.get_rect()

    # Creazione di una lista che gestisce tutti gli sprite che creeremo nel gioco (i due paddle e la pallina)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

    # Il loop va avanti finchè l'utente non esce dal gioco
    carryOn = True
    clock = pygame.time.Clock()  # verrà usato per controllare quanto velocemente si aggiorna lo screen

    while carryOn:

        for event in pygame.event.get():
            # Qui viene gestito il clic sulla "X" che chiude la finestra
            if event.type == pygame.QUIT:
                quit_game()

            # se viene premuto uno dei tasti di movimento, si dice al paddle corretto di
            # cominciare a muoversi in quella direzione
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddleA.setMovementDir(Paddle.MOVE_UP)
                if event.key == pygame.K_s:
                    paddleA.setMovementDir(Paddle.MOVE_DOWN)

                if event.key == pygame.K_i:
                    paddleB.setMovementDir(Paddle.MOVE_UP)
                if event.key == pygame.K_k:
                    paddleB.setMovementDir(Paddle.MOVE_DOWN)

                # altro modo per chiudere
                if event.key == pygame.K_ESCAPE:
                    quit_game()

            # se viene rilasciato il tasto corrispondente alla direzione in cui il paddle si sta
            # muovendo al momento, gli si dice di smettere di muoversi
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_w and paddleA.mov_dir == Paddle.MOVE_UP) or \
                        (event.key == pygame.K_s and paddleA.mov_dir == Paddle.MOVE_DOWN):
                    paddleA.setMovementDir(0)

                if (event.key == pygame.K_i and paddleB.mov_dir == Paddle.MOVE_UP) or \
                        (event.key == pygame.K_k and paddleB.mov_dir == Paddle.MOVE_DOWN):
                    paddleA.setMovementDir(0)

        # viene chiamato il metodo update() di ogni sprite nel gruppo
        # I tre parametri vengono passati all'update() di ogni sprite nel gruppo, che può usarli come vuole
        all_sprites_list.update(scrn_size=size, rectPA=paddleA.rect, rectPB=paddleB.rect)

        screen.fill(black)
        pygame.draw.line(screen, white, [size.width/2, 0], [size.width/2, size.height], 5)
        all_sprites_list.draw(screen)
        # screen.blit(ball, ballrect)
        pygame.display.flip()

        # Limite a 90 frame per secondo
        clock.tick(90)


def quit_game():
    pygame.quit()
    exit()


pygame.quit()
if __name__ == '__main__':
    main()
