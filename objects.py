import pygame, time
from pygame.locals import *
from images import Images
from variables import *
from text import Text
pygame.init()
from variables import ControllerVar

class Chest:
    def handleChest():
        if ControllerVar.chestloot >= 0 and ControllerVar.chestloot < 40:
            ControllerVar.screen.blit(Images.pt1, ((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4),PlayerVar.playerposition[1]*ControllerVar.size+40-20))
        if ControllerVar.chestloot >= 40 and ControllerVar.chestloot < 80:
            ControllerVar.screen.blit(Images.pt2, ((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4),PlayerVar.playerposition[1]*ControllerVar.size+40-20))
        if ControllerVar.chestloot >= 80 and ControllerVar.chestloot < 95:
            ControllerVar.screen.blit(Images.pt5, ((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4),PlayerVar.playerposition[1]*ControllerVar.size+40-20))
        if ControllerVar.chestloot >= 95 and ControllerVar.chestloot < 100:
            ControllerVar.screen.blit(Images.pt10, ((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4),PlayerVar.playerposition[1]*ControllerVar.size+40-20))
        if ControllerVar.tickrule % 2 == 0 and ControllerVar.sametickrule == False:
            ControllerVar.chestloot = -1
        

class Refugee:
    def handleRefugee():
        if Text.txtopen:
            if Text.nbtNum < len(Text.nbt):
                if Text.globalnum < len(Text.nbt[Text.nbtNum]):
                    CurrentDialougue = Text.nbt[Text.nbtNum]
                    if CurrentDialougue[Text.globalnum] != " " and len(CurrentDialougue) > Text.globalnum:
                        if ControllerVar.tick % 23 == 0:
                            Text.globalstring += CurrentDialougue[Text.globalnum]
                            Text.globalnum += 1
                            if Text.voice != "":
                                pygame.mixer.Sound.stop(Text.voice)
                                pygame.mixer.Sound.play(Text.voice, 0, 0, 0)
                    else:
                        if ControllerVar.tick % 23 == 0:
                            Text.globalstring += CurrentDialougue[Text.globalnum]
                            Text.globalnum += 1
                            if Text.voice != "":
                                pygame.mixer.Sound.stop(Text.voice)
            else:
                Text.txtopen = False
                Text.globalnum = 0
                Text.globalstring = ""
                Text.nbtNum = 0
            
def enemyShoot(firedBy, obj):
    match firedBy:
        case "Pawn": 
            ControllerVar.bulletlist.append([obj[1],[0,0],[0,0.5],1,obj[5]])
            ControllerVar.bulletlist.append([obj[1],[0,0],[-0.5,0.5],1,obj[5]])
            ControllerVar.bulletlist.append([obj[1],[0,0],[0.5,0.5],1, obj[5]])
        case "Rook":
            ControllerVar.bulletlist.append([obj[1], [0,0],[0,0.5],10,obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0],10,obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0,-0.5],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.5,0],10, obj[5]])
        case "Bishop":
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0.5],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,-0.5],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0.5],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.5,0.5],10, obj[5]])
        case "Queen":
            ControllerVar.bulletlist.append([obj[1], [0,0],[0,0.5],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0.5],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,-0.5],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0,-0.5],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0.5],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.5,0],10, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.5,0.5],10, obj[5]])
        case "King":
            ControllerVar.bulletlist.append([obj[1], [0,0],[0,0.5],1, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0.5],1, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0],1, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,-0.5],1, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0,-0.5],1, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0.5],1, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.5,0],1, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.5,0.5],1, obj[5]])
        case "Knight":
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.25,0.5],2, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.25,-0.5],2, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.5,0.25],2, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,0.25],2, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.25,-0.5],2, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.25,-0.5],2, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[0.5,-0.25],2, obj[5]])
            ControllerVar.bulletlist.append([obj[1], [0,0],[-0.5,-0.25],2, obj[5]])