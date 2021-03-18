# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:40:33 2021

@author: Seren
"""
from math import sqrt

import pygame

black = (0, 0, 0)


# Rappresenta un paddle
class Ball(pygame.sprite.Sprite):
    INITAL_SPEED = [3, 2]

    # r è il *raggio* della palla
    def __init__(self, r):
        super().__init__()

        self.radius = r
        self.velocity = Ball.INITAL_SPEED
        # Si carica l'immagine dello sprite
        ball_img = pygame.image.load("intro_ball.gif")
        # Viene scalata in modo da rientrare nelle dimensioni richieste
        self.image = pygame.transform.scale(ball_img, (self.radius * 2, self.radius * 2))

        self.rect = self.image.get_rect()

        print(self.rect)

    def update(self, *args, **kwargs) -> None:
        scrn_size: pygame.Rect = kwargs["scrn_size"]

        self.rect = self.rect.move(self.velocity)
        if self.rect.left < 0 or self.rect.right > scrn_size.width:
            self.velocity[0] = -self.velocity[0]
        if self.rect.top < 0 or self.rect.bottom > scrn_size.height:
            self.velocity[1] = -self.velocity[1]

    # Controlla se la palla collide con un rettangolo (ossia un paddle)
    # COPIATISSIMO DA INTERNET but it works
    def collides_rect(self, rect: pygame.Rect):
        rx = rect.x  # + self.radius
        ry = rect.y  # + self.radius
        rw = rect.width
        rh = rect.height
        cx = testX = self.rect.x
        cy = testY = self.rect.y

        if cx < rx:
            testX = rx
        elif cx > rx + rw:
            testX = rx + rw
        if cy < ry:
            testY = ry
        elif cy > ry + rh:
            testY = ry + rh

        distX = cx - testX
        distY = cy - testY
        distance = sqrt((distX * distX) + (distY * distY))

        return distance <= self.radius
