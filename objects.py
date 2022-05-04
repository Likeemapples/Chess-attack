import pygame, time
from pygame.locals import *
from images import Images
from variables import *
from text import Text
pygame.init()
WINDOW_SIZE = (1280,720)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
size = round(WINDOW_SIZE[1]/9)

class Chest:
    def handleChest():
        if ControllerVar.chestloot >= 0 and ControllerVar.chestloot < 40:
            screen.blit(Images.pt1, ((PlayerVar.playerstats[0]*80)+(90*3.5),PlayerVar.playerstats[1]*80+40-20))
            TimerVar.chest_passed = False
        if ControllerVar.chestloot >= 40 and ControllerVar.chestloot < 80:
            screen.blit(Images.pt2, ((PlayerVar.playerstats[0]*80)+(90*3.5),PlayerVar.playerstats[1]*80+40-20))
            TimerVar.chest_passed = False
        if ControllerVar.chestloot >= 80 and ControllerVar.chestloot < 95:
            screen.blit(Images.pt5, ((PlayerVar.playerstats[0]*80)+(90*3.5),PlayerVar.playerstats[1]*80+40-20))
            TimerVar.chest_passed = False
        if ControllerVar.chestloot >= 95 and ControllerVar.chestloot < 100:
            screen.blit(Images.pt10, ((PlayerVar.playerstats[0]*80)+(90*3.5),PlayerVar.playerstats[1]*80+40-20))
            TimerVar.chest_passed = False

        if TimerVar.chest_init + 1.5 <= time.time() and not TimerVar.chest_passed:
            ControllerVar.chestloot = -1
            TimerVar.chest_passed = True
        text = Text.font.render(str(PlayerVar.points), False, (255,255,255))
        screen.blit(text,Text.textRect)

class Refugee:
    def handleRefugee():
        if Text.txtopen:
            screen.blit(Images.txt,(WINDOW_SIZE[0]/8,WINDOW_SIZE[1]/2+50))
            if Text.nbtNum < len(Text.nbt):
                if Text.globalnum < len(Text.Dialougues[Text.nbt[Text.nbtNum]]):
                    CurrentDialougue = Text.Dialougues[Text.nbt[Text.nbtNum]]
                    if CurrentDialougue[Text.globalnum] != " " and len(CurrentDialougue) > Text.globalnum:
                        if TimerVar.text_init + 0.07 <= time.time():
                            Text.globalstring += CurrentDialougue[Text.globalnum]
                            Text.globalnum += 1
                            pygame.mixer.Sound.stop(Text.voice)
                            pygame.mixer.Sound.play(Text.voice, 0, 0, 0)
                            TimerVar.text_init = time.time()
                    else:
                        if TimerVar.text_init + 0.15 <= time.time():
                            Text.globalstring += CurrentDialougue[Text.globalnum]
                            Text.globalnum += 1
                            TimerVar.text_init = time.time()
                            pygame.mixer.Sound.stop(Text.voice)
            else:
                Text.txtopen = False
                Text.globalnum = 0
                Text.globalstring = ""
                Text.nbtNum = 0
            
            txtbox = Text.font.render(Text.globalstring, False, (255,255,255))
            txtrect = txtbox.get_rect()
            txtrect.x, txtrect.y = [200,500]
            screen.blit(txtbox,txtrect)