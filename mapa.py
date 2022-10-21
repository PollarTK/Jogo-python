import pygame

pygame.init()

preto = (0, 0, 0)
vermelho = (200, 0, 0)
largura = 800
altura = 600

bloco_width = largura//40
bloco_height = altura//20
screen = pygame.display.set_mode((largura, altura))

def load_image(img_set, x, y):
        img_orig = tiles.subsurface((x, y), (16, 16))
        img_scaled = pygame.transform.scale(img_orig, (bloco_width, bloco_height))
        return img_scaled

tiles = pygame.image.load("./data2/basictiles.png")
character = pygame.image.load("./data2/player.png").convert_alpha()
img_bush = load_image(tiles, 64, 16)
img_floor = load_image(tiles, 16, 128)
img_wall = load_image(tiles, 32, 16)
car_img1 = load_image(character, 28, 0)
car_img2 = load_image(character, 64, 32)
car_img3 = load_image(character, 96, 64)

class Player(pygame.sprite.Sprite):
        def __int__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = car_img1
                self.rect = pygame.Rect((32, 32), (bloco_width, bloco_height))

        def update(self):
                pass

hero = Player()
groupHero = pygame.sprite.Group(hero)
groupHero.draw(screen)

mapa = [

        "pppppppppppppppppppppppppppppppppppppppp",
        "pp                                    pp",
        "pp                                    pp",
        "pp     p     p     p     p     p      pp",
        "pp                                    pp",
        "pp                                    pp",
        "pp     p     p     p     p     p      pp",
        "pp                                    pp",
        "pp                                    pp",
        "pp     p     p     p     p     p      pp",
        "pp                                    pp",
        "pp                                    pp",
        "pp     p     p     p     p     p      pp",
        "pp                                    pp",
        "pp                                    pp",
        "pp     p     p     p     p     p      pp",
        "pp                                    pp",
        "pp                                    pp",
        "pp                                    pp",
        "pppppppppppppppppppppppppppppppppppppppp",
]

objetos = [

        "                                        ",
        "                                       ",
        "                                        ",
        "      b     b     b     b     b     b   ",
        "                                        ",
        "                                        ",
        "      b     b     b     b     b     b   ",
        "                                        ",
        "                                        ",
        "      b     b     b     b     b     b   ",
        "                                        ",
        "                                        ",
        "      b     b     b     b     b     b   ",
        "                                        ",
        "                                        ",
        "      b     b     b     b     b     b   ",
        "                                        ",
        "                                        ",
        "                                        ",
        "                                        ",
]


for id_linha, linha in enumerate(mapa):
    for id_coluna, caracter in enumerate(linha):
        #cor = preto
        #if caracter == "p":
        #    cor = vermelho
        x = id_coluna * bloco_width
        y = id_linha * bloco_height
        if caracter == "p":
                screen.blit(img_wall, (x, y))
        else:
                screen.blit(img_floor, (x, y))
        #r = pygame.Rect((x, y), (bloco_width, bloco_height))
        #pygame.draw.rect(screen, cor, r, 1)

for id_linha, linha in enumerate(objetos):
    for id_coluna, caracter in enumerate(linha):
        x = id_coluna * bloco_width
        y = id_linha * bloco_height
        if caracter == "b":
                screen.blit(img_bush, (x, y))


pygame.display.update()

while True:

        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                        exit()
