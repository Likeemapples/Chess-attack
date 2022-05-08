import pygame, time
from pygame.locals import *
pygame.init()

class ControllerVar:
    click = False
    chestloot = -1
    bulletlist = []
    hitboxes = False
    currentMap = 0
    tick = 0
    tickrule = 0
    sametickrule = False
    screen = pygame.display.set_mode((1920,1080), pygame.RESIZABLE)
    WINDOW_SIZE = (pygame.display.get_surface().get_size())
    size = round(WINDOW_SIZE[1]/9)
    gameover = False

class ChessVar:
    chesstiles = [] # Chess Board
    tilecount = 0
    worldMap = []
    objectlist = []

class PlayerVar:
    playerposition = [0,0] # board x, board y, area(area x, area y)
    defaultposition = [[0,0],[5,0],[4,3]]
    prevspot = []
    playerrect = pygame.Rect(0,0,ControllerVar.size/3,ControllerVar.size/3)
    points = 15
    isHurt = False
    biome = "Default"

class TimerVar:
    tick_init = time.time()
    canMove = True