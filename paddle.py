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

        # Setta il colore del background e lo rende trasparente
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.mov_dir = 0

        self.image.set_colorkey(black)
        # Disegna il rettangolo
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # Fa fetch con le dimensioni dell'immagine
        self.rect = self.image.get_rect()

    # metodo ereditato dalla classe Sprite, chiamato dall'omonimo update() del gruppo in cui
    # si trova lo sprite
    # non serve sapere cosa facciano gli argomenti
    def update(self, *args, **kwargs) -> None:
        self.rect.y += Paddle.SPEED * self.mov_dir
        # in questo modo la Y del paddle è sempre almeno 0
        self.rect.y = max(self.rect.y, 0)
        # in questo modo la Y del paddle è sempre al massimo 400
        self.rect.y = min(self.rect.y, 400)

    def setMovementDir(self, dir):
        if dir == Paddle.MOVE_UP:
            self.mov_dir = Paddle.MOVE_UP
        elif dir == Paddle.MOVE_DOWN:
            self.mov_dir = Paddle.MOVE_DOWN
        else:
            self.mov_dir = 0
