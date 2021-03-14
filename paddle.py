# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:40:33 2021

@author: Seren
"""

import pygame
black = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    #Rappresenta un paddle
    
    def __init__(self, color, width, height):
        super().__init__()
        
        #Setta il colore del background e lo rende trasparente
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
       
        #Disegna il rettangolo
        pygame.draw.rect(self.image, color, [0,0, width, height])
        #Fa fetch con le dimensioni dell'immagine
        self.rect = self.image.get_rect()
        
    #Per muovere su e giù i rettangoli
    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Check che non stia andando fuori dallo screen
        if self.rect.y < 0:
            self.rect.y = 0
            
    def moveDown(self, pixels):
        self.rect.y += pixels
        #Stesso check di prima
        if self.rect.y > 400:
            self.rect.y = 400
       