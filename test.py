import pygame, os, sys, pickle
from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.set_num_channels(64)
pygame.display.set_caption("Chess Attak")

screen = pygame.display.set_mode((1920,1080), pygame.RESIZABLE)
WINDOW_SIZE = (pygame.display.get_surface().get_size())
loadcentre = pygame.image.load('Assets\Misc\Centreer.png').convert()
loadcentre.set_colorkey((0,0,0))
centre = pygame.transform.scale(loadcentre, WINDOW_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.VIDEORESIZE:
            WINDOW_SIZE = screen.get_size()
            loadcentre = pygame.image.load('Assets\Misc\Centreer.png').convert()
            loadcentre.set_colorkey((0,0,0))
            centre = pygame.transform.scale(loadcentre, WINDOW_SIZE)
            
    
    screen.blit(centre, (0,0))

    pygame.display.flip()