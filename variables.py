import pygame, time
from pygame.locals import *
pygame.init()
WINDOW_SIZE = (1280,720)
size = round(WINDOW_SIZE[1]/9)

class ChessVar:
    chesstiles = [] # Chess Board
    tilecount = 0

class PlayerVar:
    playerposition = [0,0] # board x, board y, area(area x, area y)
    defaultposition = [[0,0],[5,0]]
    prevspot = []
    playerrect = pygame.Rect(0,0,size/3,size/3)
    points = 15

class ControllerVar:
    click = False
    chestloot = -1
    bulletlist = []
    hitboxes = False
    currentMap = 0

class TimerVar:
    chest_passed = True
    chest_init = time.time()
    text_passed = True
    text_init = time.time()
    shoot_init = time.time()
    move_init = time.time()
    canMove = True