import pygame
from pygame.locals import *
pygame.init()
WINDOW_SIZE = (1280,720)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
size = round(WINDOW_SIZE[1]/9)

class Images:
    # Objects
    loadchest = pygame.image.load('Assets\Misc\Chest.png').convert()
    loadchest.set_colorkey((0,0,0))
    chest = pygame.transform.scale(loadchest, (size,size))

    loadrefugee = pygame.image.load('Assets\Chess Pieces\BeatenPawn.png').convert()
    loadrefugee.set_colorkey((0,0,0))
    refugee = pygame.transform.scale(loadrefugee, (size,size))

    loadwall = pygame.image.load('Assets\Tiles\Dark Stone.png').convert()
    loadwall.set_colorkey((0,0,0))
    wall = pygame.transform.scale(loadwall, (size,size))

    # Points 
    loadpt1 = pygame.image.load('Assets\Misc\plus_one.png').convert()
    loadpt1.set_colorkey((0,0,0))
    pt1 = pygame.transform.scale(loadpt1, (size,size))

    loadpt2 = pygame.image.load('Assets\Misc\plus_two.png').convert()
    loadpt2.set_colorkey((0,0,0))
    pt2 = pygame.transform.scale(loadpt2, (size,size))

    loadpt5 = pygame.image.load('Assets\Misc\plus_five.png').convert()
    loadpt5.set_colorkey((0,0,0))
    pt5 = pygame.transform.scale(loadpt5, (size,size))

    loadpt10 = pygame.image.load('Assets\Misc\plus_ten.png').convert()
    loadpt10.set_colorkey((0,0,0))
    pt10 = pygame.transform.scale(loadpt10, (size,size))

    # UI
    loadtxt = pygame.image.load('Assets\Misc\TXT_BOX.png').convert()
    txt = pygame.transform.scale(loadtxt, (480*2,120*2))

    loadtable = pygame.image.load('Assets\Misc\Table.png').convert()
    table = pygame.transform.scale(loadtable, WINDOW_SIZE)

    # Player
    loadplayer = pygame.image.load('Assets\Chess Pieces\Pawn.png').convert()
    loadplayer.set_colorkey((0,0,0))
    player = pygame.transform.scale(loadplayer, (size, size))

    # Enemies
    loadbullet = pygame.image.load('Assets\Chess Pieces\Bullet.png').convert()
    loadbullet.set_colorkey((0,0,0))
    bullet = pygame.transform.scale(loadbullet, (size/3,size/3))

    loadpawn = pygame.image.load('Assets\Chess Pieces\Enemy Pawn.png').convert()
    loadpawn.set_colorkey((0,0,0))
    pawn = pygame.transform.scale(loadpawn, (size,size))

    loadbishop = pygame.image.load('Assets\Chess Pieces\Enemy Bishop.png').convert()
    loadbishop.set_colorkey((0,0,0))
    bishop = pygame.transform.scale(loadbishop, (size,size))

    loadguard = pygame.image.load('Assets\Chess Pieces\Enemy Guard.png').convert()
    loadguard.set_colorkey((0,0,0))
    guard = pygame.transform.scale(loadguard, (size,size))

    loadking = pygame.image.load('Assets\Chess Pieces\Enemy King.png').convert()
    loadking.set_colorkey((0,0,0))
    king = pygame.transform.scale(loadking, (size,size))

    loadknight = pygame.image.load('Assets\Chess Pieces\Enemy Knight.png').convert()
    loadknight.set_colorkey((0,0,0))
    knight = pygame.transform.scale(loadknight, (size,size))

    loadqueen = pygame.image.load('Assets\Chess Pieces\Enemy Queen.png').convert()
    loadqueen.set_colorkey((0,0,0))
    queen = pygame.transform.scale(loadqueen, (size,size))

    loadrook = pygame.image.load('Assets\Chess Pieces\Enemy Rook.png').convert()
    loadrook.set_colorkey((0,0,0))
    rook = pygame.transform.scale(loadrook, (size,size))

