import pygame, time
from pygame.locals import *
from variables import PlayerVar
pygame.init()
WINDOW_SIZE = (1280,720)
size = round(WINDOW_SIZE[1]/9)

class Voices:
    refugee = pygame.mixer.Sound('Audio\Speech\Refugee.wav')
    refugee.set_volume(0.5)
    deepvoiceText = pygame.mixer.Sound('Audio\Speech\DeepVoice.wav')
    deepvoiceText.set_volume(0.5)

class Text:
    font = pygame.font.Font('Assets\Fonts\Alkhemikal.ttf', 48)
    text = font.render(str(PlayerVar.points), True, (255,255,255))
    textRect = text.get_rect()
    textRect.x = 1000
    textRect.y = 0
    txtopen = False
    globalnum = 0
    globalstring = ""
    nbt = []
    nbtNum = 0
    voice = pygame.mixer.Sound
    playing = False
    Dialougues = [
        "Hello This Is My Text Box",
        "I Am So Happy It Is Working",
        "Flexing My Programming Prowess",
        "Hi Joro!",
        "What Do You Think Of This Game?",
        "Bippity Boopity",
        "Testy Test Mc Test Face",
        "{ @ }",
        "Text box test",
        "It is very cool",
        "19 dollar fortnite giftcard",
        "Who wants it?",
        "And yes, I am giving it away"
        ]