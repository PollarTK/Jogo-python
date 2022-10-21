import pygame
from pygame.locals import *
from sys import exit
from player import Player
from muro import Muro
from bomb import Bomb


pygame.init()

timer = 0
listaBomb = []
limitBombs = 1

#Tela
screen = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Bomber Man")

#groups
objectGroup = pygame.sprite.Group()
bombGroup = pygame.sprite.Group()

#objects
player = Player(objectGroup)
bomb = Bomb(objectGroup)
muro = Muro(objectGroup)
muro.rect.center = [120, 120]

#tela de fundo



#sons
bombPut = pygame.mixer.Sound("data/bombPut.wav")
bombPut.set_volume(0.2)
explosion = pygame.mixer.Sound("data/explosion.wav")
explosion.set_volume(0.2)

#musica
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("data/musica.mp3")
pygame.mixer.music.play(-1)

gameloop = True
clock = pygame.time.Clock()

while gameloop:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(listaBomb) < limitBombs:
                    newBomb = Bomb(objectGroup, bombGroup)
                    newBomb.rect.center = player.rect.center
                    bombPut.play()
                    listaBomb.append(newBomb)
                else:
                    pass
#logic Update
    objectGroup.update()



#draw
    screen.fill([255, 255, 255])
    objectGroup.draw(screen)

    pygame.display.update()