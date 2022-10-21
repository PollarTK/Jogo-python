import pygame
from pygame.locals import *


import muro


speed = 8

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/player.png")
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(50, 50, 100, 100)


    def update(self, *args):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= speed
        if keys[pygame.K_s]:
            self.rect.y += speed
        if keys[pygame.K_a]:
            self.rect.x -= speed
        if keys[pygame.K_d]:
            self.rect.x += speed

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 480:
            self.rect.bottom = 480
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 840:
            self.rect.right = 840

    @classmethod
    def colliderect(self, Muro):
        self.rect.center = 0




