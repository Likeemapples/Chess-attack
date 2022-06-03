import pygame, time
from pygame.locals import *
from variables import PlayerVar, ControllerVar
pygame.init()


class Voices:
    refugee = pygame.mixer.Sound('Audio\Speech\Refugee.wav')
    refugee.set_volume(0.5)
    deepvoiceText = pygame.mixer.Sound('Audio\Speech\DeepVoice.wav')
    deepvoiceText.set_volume(0.5)

class Text:
    font = pygame.font.Font('Assets\Fonts\Alkhemikal.ttf', 64)
    text = font.render(str(PlayerVar.points), True, (255,255,255))
    textRect = text.get_rect()
    textRect.x = ControllerVar.WINDOW_SIZE[0]/1.3
    textRect.y = ControllerVar.WINDOW_SIZE[1]/15
    txtopen = False
    globalnum = 0
    globalstring = ""
    nbt = []
    nbtNum = 0
    voice = pygame.mixer.Sound
    playing = False