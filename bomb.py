import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/bomb.png")
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.rect = pygame.Rect(50, 50, 100, 100)