import pygame
from pygame.locals import *
pygame.init()
from variables import *

class Images:
    # Objects
    loadchest = pygame.image.load('Assets\Misc\Chest.png').convert()
    loadchest.set_colorkey((0,0,0))
    chest = pygame.transform.scale(loadchest, (ControllerVar.size,ControllerVar.size))

    loadrefugee = pygame.image.load('Assets\Chess Pieces\BeatenPawn.png').convert()
    loadrefugee.set_colorkey((0,0,0))
    refugee = pygame.transform.scale(loadrefugee, (ControllerVar.size,ControllerVar.size))

    loadwall = pygame.image.load('Assets\Tiles\Dark Stone.png').convert()
    loadwall.set_colorkey((0,0,0))
    wall = pygame.transform.scale(loadwall, (ControllerVar.size,ControllerVar.size))

    loadstairs = pygame.image.load('Assets\Tiles\Trapdoor.png').convert()
    loadstairs.set_colorkey((0,0,0))
    stairs = pygame.transform.scale(loadstairs, (ControllerVar.size,ControllerVar.size))

    loadladder = pygame.image.load('Assets\Misc\Ladder.png').convert()
    loadladder.set_colorkey((0,0,0))
    ladder = pygame.transform.scale(loadladder, (ControllerVar.size,ControllerVar.size))

    loadsinkhole = pygame.image.load('Assets\Tiles\SinkHole.png').convert()
    loadsinkhole.set_colorkey((0,0,0))
    sinkhole = pygame.transform.scale(loadsinkhole, (ControllerVar.size,ControllerVar.size))

    loadcultist = pygame.image.load('Assets\Chess Pieces\Cultist.png').convert()
    loadcultist.set_colorkey((0,0,0))
    cultist = pygame.transform.scale(loadcultist, (ControllerVar.size,ControllerVar.size))

    # Points 
    loadpt1 = pygame.image.load('Assets\Misc\plus_one.png').convert()
    loadpt1.set_colorkey((0,0,0))
    pt1 = pygame.transform.scale(loadpt1, (ControllerVar.size,ControllerVar.size))

    loadpt2 = pygame.image.load('Assets\Misc\plus_two.png').convert()
    loadpt2.set_colorkey((0,0,0))
    pt2 = pygame.transform.scale(loadpt2, (ControllerVar.size,ControllerVar.size))

    loadpt5 = pygame.image.load('Assets\Misc\plus_five.png').convert()
    loadpt5.set_colorkey((0,0,0))
    pt5 = pygame.transform.scale(loadpt5, (ControllerVar.size,ControllerVar.size))

    loadpt10 = pygame.image.load('Assets\Misc\plus_ten.png').convert()
    loadpt10.set_colorkey((0,0,0))
    pt10 = pygame.transform.scale(loadpt10, (ControllerVar.size,ControllerVar.size))

    # UI
    loadtxt = pygame.image.load('Assets\Misc\TXT_BOX.png').convert()
    txt = pygame.transform.scale(loadtxt, (ControllerVar.WINDOW_SIZE[0]/1.5,ControllerVar.WINDOW_SIZE[1]/3))

    loadtable = pygame.image.load('Assets\Misc\Table.png').convert()
    table = pygame.transform.scale(loadtable, ControllerVar.WINDOW_SIZE)

    loadbar = pygame.image.load('Assets\Misc\Bar.png').convert()
    loadbar.set_colorkey((0,0,0))
    bar = pygame.transform.scale(loadbar, (ControllerVar.WINDOW_SIZE[0]/5,ControllerVar.WINDOW_SIZE[1]/10))

    loadgameover = pygame.image.load('Assets\Misc\Game Over.png').convert()
    gameover = pygame.transform.scale(loadgameover, ControllerVar.WINDOW_SIZE)

    loadvignette = pygame.image.load('Assets\Misc\Vignette.png').convert()
    loadvignette.set_colorkey((0,0,0))
    loadvignette.set_alpha(100)
    vignette = pygame.transform.scale(loadvignette, ControllerVar.WINDOW_SIZE)

    loadvignette2 = pygame.image.load('Assets\Misc\Vignette2.png').convert()
    loadvignette2.set_colorkey((0,0,0))
    loadvignette.set_alpha(200)
    vignette2 = pygame.transform.scale(loadvignette2, ControllerVar.WINDOW_SIZE)

    # Player
    loadplayer = pygame.image.load('Assets\Chess Pieces\Pawn.png').convert()
    loadplayer.set_colorkey((0,0,0))
    player = pygame.transform.scale(loadplayer, (ControllerVar.size, ControllerVar.size))

    loadhurt = pygame.image.load('Assets\Chess Pieces\PlayerHurt.png').convert()
    loadhurt.set_colorkey((0,0,0))
    hurt = pygame.transform.scale(loadhurt, (ControllerVar.size, ControllerVar.size))

    loadwading = pygame.image.load('Assets\Chess Pieces\PlayerInLiquid.png').convert()
    loadwading.set_colorkey((0,0,0))
    wading = pygame.transform.scale(loadwading, (ControllerVar.size, ControllerVar.size))

    loadwadinghurt = pygame.image.load('Assets\Chess Pieces\PlayerInLiquidHurt.png').convert()
    loadwadinghurt.set_colorkey((0,0,0))
    wadinghurt = pygame.transform.scale(loadwadinghurt, (ControllerVar.size, ControllerVar.size))

    # Enemies
    loadbullet = pygame.image.load('Assets\Chess Pieces\Bullet.png').convert()
    loadbullet.set_colorkey((0,0,0))
    bullet = pygame.transform.scale(loadbullet, (ControllerVar.size/3,ControllerVar.size/3))

    loadpawn = pygame.image.load('Assets\Chess Pieces\Enemy Pawn.png').convert()
    loadpawn.set_colorkey((0,0,0))
    pawn = pygame.transform.scale(loadpawn, (ControllerVar.size,ControllerVar.size))

    loadbishop = pygame.image.load('Assets\Chess Pieces\Enemy Bishop.png').convert()
    loadbishop.set_colorkey((0,0,0))
    bishop = pygame.transform.scale(loadbishop, (ControllerVar.size,ControllerVar.size))

    loadguard = pygame.image.load('Assets\Chess Pieces\Enemy Guard.png').convert()
    loadguard.set_colorkey((0,0,0))
    guard = pygame.transform.scale(loadguard, (ControllerVar.size,ControllerVar.size))

    loadking = pygame.image.load('Assets\Chess Pieces\Enemy King.png').convert()
    loadking.set_colorkey((0,0,0))
    king = pygame.transform.scale(loadking, (ControllerVar.size,ControllerVar.size))

    loadknight = pygame.image.load('Assets\Chess Pieces\Enemy Knight.png').convert()
    loadknight.set_colorkey((0,0,0))
    knight = pygame.transform.scale(loadknight, (ControllerVar.size,ControllerVar.size))

    loadqueen = pygame.image.load('Assets\Chess Pieces\Enemy Queen.png').convert()
    loadqueen.set_colorkey((0,0,0))
    queen = pygame.transform.scale(loadqueen, (ControllerVar.size,ControllerVar.size))

    loadrook = pygame.image.load('Assets\Chess Pieces\Enemy Rook.png').convert()
    loadrook.set_colorkey((0,0,0))
    rook = pygame.transform.scale(loadrook, (ControllerVar.size,ControllerVar.size))

    # Tiles
    loaddarkgrass = pygame.image.load('Assets\Tiles\Dark Grass.png').convert()
    loaddarkgrass.set_colorkey((0,0,0))
    grassD = pygame.transform.scale(loaddarkgrass, (ControllerVar.size,ControllerVar.size))
    loadlightgrass = pygame.image.load('Assets\Tiles\Light Grass.png').convert()
    loadlightgrass.set_colorkey((0,0,0))
    grassL = pygame.transform.scale(loadlightgrass, (ControllerVar.size,ControllerVar.size))

    loadblack = pygame.image.load('Assets\Tiles\Black.png').convert()
    loadblack.set_colorkey((0,0,0))
    black = pygame.transform.scale(loadblack, (ControllerVar.size,ControllerVar.size))
    loadwhite = pygame.image.load('Assets\Tiles\White.png').convert()
    loadwhite.set_colorkey((0,0,0))
    white = pygame.transform.scale(loadwhite, (ControllerVar.size,ControllerVar.size))

    loaddarkstone = pygame.image.load('Assets\Tiles\Dark Stone.png').convert()
    loaddarkstone.set_colorkey((0,0,0))
    stoneD = pygame.transform.scale(loaddarkstone, (ControllerVar.size,ControllerVar.size))
    loadlightstone = pygame.image.load('Assets\Tiles\Light Stone.png').convert()
    loadlightstone.set_colorkey((0,0,0))
    stoneL = pygame.transform.scale(loadlightstone, (ControllerVar.size,ControllerVar.size))

    loaddarkdirt = pygame.image.load('Assets\Tiles\Dark Dirt.png').convert()
    loaddarkdirt.set_colorkey((0,0,0))
    dirtD = pygame.transform.scale(loaddarkdirt, (ControllerVar.size,ControllerVar.size))
    loadlightdirt = pygame.image.load('Assets\Tiles\Light Dirt.png').convert()
    loadlightdirt.set_colorkey((0,0,0))
    dirtL = pygame.transform.scale(loadlightdirt, (ControllerVar.size,ControllerVar.size))


    waterD = pygame.image.load('Assets\Tiles\waterdark1.png').convert()

    waterL = pygame.image.load('Assets\Tiles\waterdark1.png').convert()


    def animateWater(waterL,waterD):
        if ControllerVar.tickrule % 2 == 0: #and ControllerVar.sametickrule == False:
            loaddarkwater = pygame.image.load('Assets\Tiles\waterdark1.png').convert()
            loaddarkwater.set_colorkey((0,0,0))
            waterD = pygame.transform.scale(loaddarkwater, (ControllerVar.size,ControllerVar.size))
            loadlightwater = pygame.image.load('Assets\Tiles\waterlight1.png').convert()
            loadlightwater.set_colorkey((0,0,0))
            waterL = pygame.transform.scale(loadlightwater, (ControllerVar.size,ControllerVar.size))
        elif ControllerVar.tickrule % 2 == 1: #and ControllerVar.sametickrule == False:
            loaddarkwater = pygame.image.load('Assets\Tiles\waterdark2.png').convert()
            loaddarkwater.set_colorkey((0,0,0))
            waterD = pygame.transform.scale(loaddarkwater, (ControllerVar.size,ControllerVar.size))
            loadlightwater = pygame.image.load('Assets\Tiles\waterlight2.png').convert()
            loadlightwater.set_colorkey((0,0,0))
            waterL = pygame.transform.scale(loadlightwater, (ControllerVar.size,ControllerVar.size))
        return waterL,waterD

    tiles = [white, black]