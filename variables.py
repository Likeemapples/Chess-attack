import pygame, time
from pygame.locals import *
pygame.init()
WINDOW_SIZE = (1280,720)
size = round(WINDOW_SIZE[1]/9)

class ChessVar:
    chesstiles = [] # Chess Board
    tilecount = 0

class PlayerVar:
    playerstats = [0,0,[0,0]] # board x, board y, area(area x, area y)
    prevspot = []
    playerrect = pygame.Rect(0,0,size/3,size/3)
    points = 15

class ControllerVar:
    click = False
    chestloot = -1
    bulletlist = []

class TimerVar:
    chest_passed = True
    chest_init = time.time()
    text_passed = True
    text_init = time.time()
    shoot_init = time.time()
    move_init = time.time()