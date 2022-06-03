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
    screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE)
    WINDOW_SIZE = (pygame.display.get_surface().get_size())
    size = round(WINDOW_SIZE[1]/9)
    gameover = False

def resizeDisplay(thing1, thing2, thing3):
    thing1 = pygame.display.set_mode((1080,720), pygame.RESIZABLE)
    thing2 = (pygame.display.get_surface().get_size())
    thing3 = round(thing2[1]/9)
class ChessVar:
    chesstiles = [] # Chess Board
    tilecount = 0
    worldMap = []
    objectlist = []

class PlayerVar:
    playerposition = [0,0] # board x, board y, area(area x, area y)
    prevspot = []
    playerrect = pygame.Rect(0,0,ControllerVar.size/3,ControllerVar.size/3)
    points = 0
    isHurt = False
    biome = "Default"
    wading = False

class TimerVar:
    tick_init = time.time()
    canMove = True