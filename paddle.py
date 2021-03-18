# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:40:33 2021

@author: Seren
"""

import pygame

black = (0, 0, 0)


# Rappresenta un paddle
class Paddle(pygame.sprite.Sprite):
    # attributo statico per indicare la velocità con cui un paddle può muoversi
    SPEED = 6
    MOVE_UP = -1
    MOVE_DOWN = 1

    def __init__(self, color, width, height):
        super().__init__()

        # Crea l'immagine dello sprite con dimensioni width x height
        self.image = pygame.Surface([width, height])
        # Colora l'immagine disegnandovi dentro un rettangolo del colore "color"
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

        self.mov_dir = 0

    # metodo ereditato dalla classe Sprite, chiamato dall'omonimo update() del gruppo in cui
    # si trova lo sprite
    # non serve sapere cosa facciano gli argomenti
    def update(self, *args, **kwargs) -> None:
        scrn_h = kwargs["scrn_size"].height

        self.rect.y += Paddle.SPEED * self.mov_dir
        # in questo modo la Y del paddle è sempre almeno 0
        self.rect.y = max(self.rect.y, 0)
        # in questo modo la Y del paddle è sempre al massimo (altezza_schermo)-(altezza_paddle)
        self.rect.y = min(self.rect.y, scrn_h - self.rect.height)

    def setMovementDir(self, dir):
        if dir == Paddle.MOVE_UP:
            self.mov_dir = Paddle.MOVE_UP
        elif dir == Paddle.MOVE_DOWN:
            self.mov_dir = Paddle.MOVE_DOWN
        else:
            self.mov_dir = 0
