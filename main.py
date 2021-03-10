# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:19:51 2021

@author: Seren
"""

import sys, pygame


def quit_game():
    sys.exit(0)


def main():
    pygame.init()

    size = width, height = 1024, 800
    speed = [1, 1]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()
                # poi qua ci si mette il codice per gestire gli altri possibili keypress

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
