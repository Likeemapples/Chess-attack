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
                if Text.globalnum < len(Text.Dialougues[Text.nbt[Text.nbtNum]]):
                    CurrentDialougue = Text.Dialougues[Text.nbt[Text.nbtNum]]
                    if CurrentDialougue[Text.globalnum] != " " and len(CurrentDialougue) > Text.globalnum:
                        if ControllerVar.tick % 23 == 0:
                            Text.globalstring += CurrentDialougue[Text.globalnum]
                            Text.globalnum += 1
                            pygame.mixer.Sound.stop(Text.voice)
                            pygame.mixer.Sound.play(Text.voice, 0, 0, 0)
                    else:
                        if ControllerVar.tick % 23 == 0:
                            Text.globalstring += CurrentDialougue[Text.globalnum]
                            Text.globalnum += 1
                            pygame.mixer.Sound.stop(Text.voice)
            else:
                Text.txtopen = False
                Text.globalnum = 0
                Text.globalstring = ""
                Text.nbtNum = 0
            
            