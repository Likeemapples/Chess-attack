################
# Chess Attak #
################

import pygame, sys, random, math, json, pickle, time, os
from images import Images
from variables import *
from text import *
from objects import *

# Init things
#Images.initImages()

from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.set_num_channels(64)
pygame.display.set_caption("Chess Attak")

# Pygame Variables
boardRect = pygame.Rect(0 + ControllerVar.size+ControllerVar.WINDOW_SIZE[0]/6, ControllerVar.size/1.1,ControllerVar.size*7,ControllerVar.size*7)

def initWorld():
    ChessVar.worldMap = [
        [
            [-2, "Default"],
            [-1, [0,0]],
            [0, [1,0],Images.chest,0], 
            [1, [2,0],Images.refugee,1,["Hello This Is My Text Box","I Am So Happy It Is Working","Flexing My Programming Prowess","What Do You Think Of This Game?"],Voices.refugee],
            [1, [2,1],Images.refugee,2,["Hello This Is My Text Box","I Am So Happy It Is Working","Bippity Boopity","Testy Test Mc Test Face"],Voices.refugee],
            [1, [2,2],Images.refugee,3,["19 dollar fortnite giftcard","Who wants it?","And yes, I am giving it away"],Voices.deepvoiceText],
            [1, [4,3],Images.tree,4,["ASdasfaF","End my suffering"],Voices.deepvoiceText],
            [4, [5,0],Images.stairs]
        ],
        [
            [-2, "Outside"],
            [-1, [5,0]],
            #[2, [4,0],Images.pawn,1,"Pawn",False],
            [2, [4,5],Images.rook,2,"Rook",False],
            # [3, [4,0],Images.wall],
            # [3, [4,1],Images.wall],
            # [3, [4,2],Images.wall],
            # [3, [4,3],Images.wall],
            # [3, [4,4],Images.wall],
            # [3, [4,6],Images.wall],
            # [3, [4,7],Images.wall],
            # [3, [0,5],Images.wall],
            # [3, [1,5],Images.wall],
            # [3, [2,5],Images.wall],
            # [3, [3,5],Images.wall],
            # [3, [5,5],Images.wall],
            # [3, [6,5],Images.wall],
            # [3, [7,5],Images.wall],
            #[2, [4,6],Images.bishop,3,"Bishop"],
            #[2, [4,7],Images.queen,4,"Queen"],
            #[2, [4,3],Images.king,5,"King"],
            #[2, [4,2],Images.knight,6,"Knight"],
            [5, [5,1],Images.ladder],
            [4, [0,0],Images.stairs]
        ],
        [
            [-2, "Cultist"],
            [-1, [4,3]],
            [5, [4,4],Images.ladder],
            [4, [5,4],Images.stairs],
            [1, [4,5],Images.cultist,0,["No one came to my party...","Welp! That sucks"],Voices.deepvoiceText]
        ],
        [
            [-2, "Cave"],
            [-1, [7,7]],
            [5, [7,6],Images.ladder],
            [4, [0,0],Images.stairs]
        ],
        [
            [-2, "Swamp"],
            [-1, [0,0]],
            # [2, [4,0],Images.pawn,1,"Pawn",False],
            # [2, [4,5],Images.rook,2,"Rook",False],
            [6, [4,4],['Assets\Tiles\waterlight1.png','Assets\Tiles\waterlight2.png']],
            [6, [4,5],['Assets\Tiles\waterdark1.png','Assets\Tiles\waterdark2.png']],
            [6, [4,3],['Assets\Tiles\waterdark1.png','Assets\Tiles\waterdark2.png']],
            [6, [3,4],['Assets\Tiles\waterdark1.png','Assets\Tiles\waterdark2.png']],
            [6, [5,4],['Assets\Tiles\waterdark1.png','Assets\Tiles\waterdark2.png']],
            [5, [0,1],Images.ladder],
            [4, [7,2],Images.stairs,3]
        ],
        [
            [-2, "Graveyard"],
            [-1, [0,7],0],
            [5, [1,7],Images.ladder,1],
            [3, [3,5],Images.gravestone,2],
            [4, [7,2],Images.stairs,3],
            [1, [5,6],Images.cultist,4,["I wonder if the dead can still hear us","If they can i have a lot of apologizing to do","Anyways, Go away now, i have some mourning to do"],Voices.deepvoiceText],

        ]
    ]
    for x in range(8):
        for y in range(8):
            if x != 4 and y != 4:
                ChessVar.worldMap[2].append([0, [x,y],Images.chest])
            #ChessVar.worldMap[0].append([6, [x,y],['Assets\Tiles\waterlight1.png','Assets\Tiles\waterlight2.png']])
    ChessVar.worldMap[0].append([2, [6,7],Images.rook,2,"Rook",False])

    # for _ in range(8):
    #     map = []
    #     BiomeN = random.randrange(0,4)
    #     Biome = "Default"
    #     match BiomeN:
    #         case 0:
    #             Biome = "Default"
    #         case 1:
    #             Biome = "Outside"
    #         case 2:
    #             Biome = "Cultist"
    #         case 3:
    #             Biome = "Cave"
    #         case 4:
    #             Biome = "Swamp"
    #     ladderpos = [random.randrange(1,7),random.randrange(1,7)]
    #     playerpos = [ladderpos[0],ladderpos[1]-1]
    #     stairpos = [random.randrange(0,7),random.randrange(0,7)]
    #     while stairpos == ladderpos or stairpos == playerpos:
    #         stairpos = [random.randrange(0,7),random.randrange(0,7)]
    #     ChessVar.worldMap.append([])
    #     enemies = []
    #     for num in range(random.randrange(1,4)):
    #         enemypos = [random.randrange(0,7),random.randrange(0,7)]
    #         while enemypos == ladderpos or enemypos == playerpos or enemypos == stairpos:
    #             enemypos = [random.randrange(0,7),random.randrange(0,7)]
    #         enemytype = random.randrange(0,1)
    #         enemyimage = pygame.image
    #         enemyname = ""
    #         match enemytype:
    #             case 0:
    #                 enemyimage = Images.pawn
    #                 enemyname = "Pawn"
    #             case 1:
    #                 enemyimage = Images.rook
    #                 enemyname = "Rook"
    #         enemies.append([2, enemypos, enemyimage,num,enemyname,False])
    #         print(ChessVar.worldMap[_])
    #         ChessVar.worldMap[_].clear()
    #         ChessVar.worldMap.append([
    #             [-2, Biome],
    #             [-1, playerpos],
    #             [5, ladderpos, Images.ladder],
    #             [4, stairpos, Images.stairs],
    #             enemies
    #         ])
    #     #ChessVar.worldMap.append([map])
    #     print(ChessVar.worldMap[_])

    
    PlayerVar.points = 1
    PlayerVar.playerposition = [0,0]
    ControllerVar.currentMap = 0
    ChessVar.objectlist = ChessVar.worldMap[ControllerVar.currentMap] 
    ControllerVar.bulletlist = []
    PlayerVar.isHurt = False
    Text.globalnum = 0
    Text.globalstring = ""
    Text.txtopen = False
    Text.nbtNum = 0
    Text.nbt = []

    def sortByY(obj):
        if obj[0] != -2 and obj[0] != -1:
            return obj[1][1]
        else:
            return -1

    for map in ChessVar.worldMap:
        map.sort(key=sortByY)

initWorld()
# Game Loop
while True:
    
    ChessVar.objectlist = ChessVar.worldMap[ControllerVar.currentMap]
    #resizeDisplay(ControllerVar.screen, ControllerVar.WINDOW_SIZE, ControllerVar.size)

    start = time.time()
    # Events

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            print("resized")
            # resizeDisplay(ControllerVar.screen,ControllerVar.WINDOW_SIZE,ControllerVar.size)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if not Text.txtopen:
                if event.key == K_d or event.key == K_RIGHT: 
                    PlayerVar.playerposition[0] += 1
                if event.key == K_a or event.key == K_LEFT:
                    PlayerVar.playerposition[0] -= 1
                if event.key == K_w or event.key == K_UP:
                    PlayerVar.playerposition[1] -= 1
                if event.key == K_s or event.key == K_DOWN:
                    PlayerVar.playerposition[1] += 1
            if event.key == K_z and Text.txtopen:
                Text.globalnum = 0
                Text.globalstring = ""
                Text.nbtNum += 1
            if event.key == K_e:
                ControllerVar.hitboxes = not ControllerVar.hitboxes
            if event.key == K_r:
                if ControllerVar.gameover == True:
                    ControllerVar.gameover = False
                    initWorld()
                else:
                    ControllerVar.gameover = True
                
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                ControllerVar.click = True
    
    if not ControllerVar.gameover:

        # Draw Table
        ControllerVar.screen.blit(Images.table, (0,0))

        # Mouse
        mx, my = pygame.mouse.get_pos()
        mouse = pygame.Rect(mx,my,1,1)

        # Initialize Chess
        if ChessVar.tilecount <= 64:
            for y in range(8):
                for x in range(8):
                    rect = pygame.Rect(0 + (x*ControllerVar.size+(ControllerVar.WINDOW_SIZE[0]/4.9)), (y*ControllerVar.size+(40)), ControllerVar.size, ControllerVar.size)
                    if (y % 2) == 0:
                        if (x % 2) == 0:
                            ChessVar.chesstiles.append([rect.x, rect.y, 1, rect, ChessVar.tilecount, 1])
                        else:
                            ChessVar.chesstiles.append([rect.x, rect.y, 1, rect, ChessVar.tilecount, 0])
                    else:
                        if (x % 2) == 0:
                            ChessVar.chesstiles.append([rect.x, rect.y, 1, rect, ChessVar.tilecount, 0])
                        else:
                            ChessVar.chesstiles.append([rect.x, rect.y, 1, rect, ChessVar.tilecount, 1])
                    #ChessVar.objectlist.append([0,[x,y],Images.chest]) # DRAW CHEST EVERYWHERE
                    
                    ChessVar.tilecount += 1

        # Handle Chess    
        if PlayerVar.playerposition[0] < 0:
            PlayerVar.playerposition[0] = 0
        if PlayerVar.playerposition[0] > 7:
            PlayerVar.playerposition[0] = 7
        if PlayerVar.playerposition[1] < 0:
            PlayerVar.playerposition[1] = 0
        if PlayerVar.playerposition[1] > 7:
            PlayerVar.playerposition[1] = 7

        for tile in ChessVar.chesstiles:
            rect = tile[3]
            # if rect.collidepoint((mx,my)):
            #     pygame.draw.rect(ControllerVar.screen,(255,0,0),rect)
            if tile[5] == 0:
                ControllerVar.screen.blit(Images.tiles[1], rect)
            else:
                ControllerVar.screen.blit(Images.tiles[0], rect)

        # Initialize and Handle Objects
        for obj in ChessVar.objectlist:
            if obj[0] != -1 and obj[0] != -2:
                temp_rect = pygame.Rect(obj[1][0]*ControllerVar.size+ControllerVar.WINDOW_SIZE[0]/4.9,obj[1][1]*ControllerVar.size+40,ControllerVar.size,ControllerVar.size)

            # Draw Normal
            if obj[0] == 0 or obj[0] == 3 or obj[0] == 4 or obj[0] == 5:
                ControllerVar.screen.blit(obj[2],temp_rect)
                if ControllerVar.hitboxes:
                    pygame.draw.rect(ControllerVar.screen,(0,0,255),temp_rect,1)

            # Draw Animated
            elif obj[0] == 6:
                ControllerVar.screen.blit(Images.animate(obj[2][0],obj[2][1]),temp_rect)
                if ControllerVar.hitboxes:
                    pygame.draw.rect(ControllerVar.screen,(0,0,255),temp_rect,1)

            
            # Draw Offset
            elif obj[0] != -1 and obj[0] != -2:
                temp_rect.y -= 20
                ControllerVar.screen.blit(obj[2],temp_rect)
                if ControllerVar.hitboxes:
                    pygame.draw.rect(ControllerVar.screen,(0,0,255),temp_rect,1)
            
            match obj[0]:
                case -1: # Player
                    PlayerVar.playerposition = obj[1]
                    obj[1] = PlayerVar.playerposition
                case -2: # Biome
                    PlayerVar.biome = obj[1]
            if PlayerVar.playerposition == obj[1]:
                if not obj[0] == 6:
                    PlayerVar.wading = False
                match obj[0]:
                    case 0: # Chest
                        ControllerVar.chestloot = random.randrange(0,100)
                        TimerVar.chest_init = time.time()
                        if ControllerVar.chestloot >= 0 and ControllerVar.chestloot < 40:
                            PlayerVar.points += 1
                        if ControllerVar.chestloot >= 40 and ControllerVar.chestloot < 80:
                            PlayerVar.points += 2
                        if ControllerVar.chestloot >= 80 and ControllerVar.chestloot < 95:
                            PlayerVar.points += 5
                        if ControllerVar.chestloot >= 95 and ControllerVar.chestloot < 100:
                            PlayerVar.points += 10
                        ChessVar.objectlist.remove(obj)
                    case 1: # Refugee
                        TimerVar.text_init = time.time()
                        Text.nbt = obj[4]
                        Text.voice = obj[5]
                        Text.txtopen = True
                        PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                    case 2: # Enemy
                        PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                        match obj[4]:
                            case "Pawn":
                                PlayerVar.points += 1
                                ControllerVar.chestloot = 10
                            case "Rook":
                                PlayerVar.points += 2
                                ControllerVar.chestloot = 50
                        ChessVar.objectlist.remove(obj)
                    case 3: # Wall
                        PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                    case 4: # Stairs
                        if ControllerVar.currentMap == len(ChessVar.worldMap)-1:
                            TimerVar.text_init = time.time()
                            Text.nbt = ["There's nothing down here"]
                            Text.voice = ""
                            Text.txtopen = True
                            PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                        else:
                            PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                            ControllerVar.currentMap += 1
                            ControllerVar.bulletlist = []
                    case 5: # Ladder
                        if ControllerVar.currentMap == 0:
                            TimerVar.text_init = time.time()
                            Text.nbt = ["It leads to nothing"]
                            Text.voice = ""
                            Text.txtopen = True
                            PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                        else:
                            PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                            ControllerVar.currentMap -= 1
                            ControllerVar.bulletlist = []
                    case 6: # Water
                        PlayerVar.wading = True
                    
                
        
        if ControllerVar.tickrule % 6 == 0 and ControllerVar.sametickrule == False:
            for obj in ChessVar.objectlist:
                if obj[0] == 2:
                    TimerVar.canMove = True
                    if obj[4] == "Pawn":
                        for obj1 in ChessVar.objectlist:
                            if obj[1][1] + 1 == obj1[1][1] and obj[1][0] == obj1[1][0] and obj != obj1 or obj[1][1] + 1 == PlayerVar.playerposition[1] and obj[1][0] == PlayerVar.playerposition[0]:
                                TimerVar.canMove = False
                        if obj[1][1] != 7 and TimerVar.canMove:
                            obj[1][1] += 1
                            TimerVar.canMove = False
                        TimerVar.move_init = time.time()

                    if obj[4] == "Rook":
                        storedir = [False,False,False,False]
                        possiblespots = []

                        for x in range(8):
                            for obj1 in ChessVar.objectlist:
                                if obj[1][0] - x == obj1[1][0] and obj[1][1] == obj1[1][1] and obj1[0] != 6 and obj != obj1:
                                    storedir[0] = True
                                if obj[1][0] + x == obj1[1][0] and obj[1][1] == obj1[1][1] and obj1[0] != 6 and obj != obj1: 
                                    storedir[1] = True
                            if not storedir[0] and not obj[1][0] - x < 0:
                                possiblespots.append([x,obj[1][1]])
                            if not storedir[1] and not obj[1][0] + x >= 8:
                                possiblespots.append([obj[1][0] + x, obj[1][1]])

                        for y in range(8):
                            for obj1 in ChessVar.objectlist:
                                if obj[1][1] - y == obj1[1][1] and obj[1][0] == obj1[1][0] and obj1[0] != 6 and obj != obj1:
                                    storedir[2] = True
                                if obj[1][1] + y == obj1[1][1] and obj[1][0] == obj1[1][0] and obj1[0] != 6 and obj != obj1: 
                                    storedir[3] = True
                            if not storedir[2] and not obj[1][1] - y < 0:
                                possiblespots.append([obj[1][0],y])
                            if not storedir[3] and not obj[1][1] + y >= 8:
                                possiblespots.append([obj[1][0], obj[1][1] + y])
                        
                        if len(possiblespots) > 0:
                            checkspot = possiblespots[random.randrange(len(possiblespots))]
                            while checkspot == obj[1]:
                                possiblespots.remove(checkspot)
                                checkspot = possiblespots[random.randrange(len(possiblespots))]
                            while checkspot == PlayerVar.playerposition:
                                possiblespots.remove(checkspot)
                                checkspot = possiblespots[random.randrange(len(possiblespots))]
                            for obj1 in ChessVar.objectlist:
                                while checkspot == obj1[1] and obj1 != obj:
                                    possiblespots.remove(checkspot)
                                    checkspot = possiblespots[random.randrange(len(possiblespots))]
                            obj[1] = checkspot
                        

        if ControllerVar.tickrule % 2 == 0 and ControllerVar.sametickrule == False:
            for obj in ChessVar.objectlist:
                if obj[0] == 2:
                    enemyShoot(obj[4],obj)
                    TimerVar.shoot_init = time.time()
                    for obj1 in ChessVar.objectlist:
                        if obj[1] == obj1[1]:
                            match obj[4]:
                                case "Rook":
                                    if obj1[0] == 6:
                                        obj[2] = Images.rookswim
                                        obj[5] = True
                                    else:
                                        obj[2] = Images.rook
                                        obj[5] = False
        if ControllerVar.sametickrule == False:
            PlayerVar.isHurt = False

        # Handle Player
        
        if not PlayerVar.wading:
            PlayerVar.playerrect.x = ((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4.9))+(ControllerVar.size/3)
            PlayerVar.playerrect.y = ((PlayerVar.playerposition[1]*ControllerVar.size+40))+(ControllerVar.size/3)
            if PlayerVar.isHurt:
                ControllerVar.screen.blit(Images.hurt,((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4.9),PlayerVar.playerposition[1]*ControllerVar.size+40-20))
            else:
                ControllerVar.screen.blit(Images.player,((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4.9),PlayerVar.playerposition[1]*ControllerVar.size+20))
            if ControllerVar.hitboxes:
                pygame.draw.rect(ControllerVar.screen,(0,255,0),PlayerVar.playerrect,1)
        else:
            PlayerVar.playerrect.x = ((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4.9))+(ControllerVar.size/3)
            PlayerVar.playerrect.y = ((PlayerVar.playerposition[1]*ControllerVar.size+40))+(ControllerVar.size/1.5)
            if PlayerVar.isHurt:
                ControllerVar.screen.blit(Images.wadinghurt,((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4.9),PlayerVar.playerposition[1]*ControllerVar.size+40-20))
            else:
                ControllerVar.screen.blit(Images.wading,((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4.9),PlayerVar.playerposition[1]*ControllerVar.size+20))
            if ControllerVar.hitboxes:
                pygame.draw.rect(ControllerVar.screen,(0,255,0),PlayerVar.playerrect,1)

        # Handle Objects
        Chest.handleChest()

        Refugee.handleRefugee()
        
        # Enemy
        
        for bullet in ControllerVar.bulletlist:
            pos = bullet[0]
            rect = pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size/3,ControllerVar.size/3)
            change = bullet[1]
            direction = bullet[2]
            distance = bullet[3]
            rect.x = (pos[0]*ControllerVar.size+ControllerVar.WINDOW_SIZE[0]/4.9)+ControllerVar.size/3+change[0]
            if bullet[4] == True:
                rect.y = (pos[1]*ControllerVar.size+40)+ControllerVar.size/1.5 + change[1]
            else:
                rect.y = (pos[1]*ControllerVar.size+40)+ControllerVar.size/3 + change[1]
            
            if ControllerVar.tick % 3 == 0:
                change[0] += direction[0]
                change[1] += direction[1]

            if abs(change[0]) >= ControllerVar.size*distance or abs(change[1]) >= ControllerVar.size*distance:
                ControllerVar.bulletlist.remove(bullet)
            ControllerVar.screen.blit(Images.bullet,rect)
            if ControllerVar.hitboxes:
                pygame.draw.rect(ControllerVar.screen,(255,0,0),rect, 1)

            if not rect.colliderect(boardRect):
                ControllerVar.bulletlist.remove(bullet)

            if rect.colliderect(PlayerVar.playerrect) and PlayerVar.isHurt == False:
                PlayerVar.points -= 1
                PlayerVar.isHurt = True

        # Reset variables
        PlayerVar.prevspot = PlayerVar.playerposition[0], PlayerVar.playerposition[1]
        ControllerVar.click = False

        match PlayerVar.biome:
            case "Default":
                Images.tiles = [Images.white, Images.black]
                #PlayerVar.wading = False
                #Images.fogLevel(1)
            case "Outside":
                Images.tiles = [Images.grassL, Images.grassD]
                #PlayerVar.wading = False
                #Images.fogLevel(2)
            case "Cultist":
                Images.tiles = [Images.stoneL, Images.stoneD]
                ControllerVar.screen.blit(Images.vignette, (0,0))
                ControllerVar.screen.blit(Images.vignette2, (0,0))
                #PlayerVar.wading = False
                Images.fogLevel(2)
            case "Cave":
                Images.tiles = [Images.dirtL, Images.dirtD]
                #PlayerVar.wading = False
                #Images.fogLevel(4)
            case "Swamp":
                Images.tiles = [Images.swampL,Images.swampD]
                #Images.tiles = [Images.animateWater(Images.waterL,Images.waterD)[0], Images.animateWater(Images.waterL,Images.waterD)[1]]
                #PlayerVar.wading = True
            case "Graveyard":
                Images.tiles = [Images.graveyardL,Images.graveyardD]
                Images.fogLevel(3)

        
        text = Text.font.render(str(PlayerVar.points), False, (255,255,255))
        
        if PlayerVar.points > -1 and PlayerVar.points < 6:
            pygame.draw.rect(ControllerVar.screen, (255,0,0), (Text.textRect.x, Text.textRect.y, PlayerVar.points/5*ControllerVar.WINDOW_SIZE[0]/5, ControllerVar.WINDOW_SIZE[1]/10))
        elif PlayerVar.points > 5 and PlayerVar.points < 16:
            pygame.draw.rect(ControllerVar.screen, (255,0,0), (Text.textRect.x, Text.textRect.y, ControllerVar.WINDOW_SIZE[0]/5,ControllerVar.WINDOW_SIZE[1]/10))

            pygame.draw.rect(ControllerVar.screen, (255,122,0), (Text.textRect.x, Text.textRect.y, PlayerVar.points/15*ControllerVar.WINDOW_SIZE[0]/5, ControllerVar.WINDOW_SIZE[1]/10))
        elif PlayerVar.points > 15 and PlayerVar.points < 31:
            pygame.draw.rect(ControllerVar.screen, (255,122,0), (Text.textRect.x, Text.textRect.y, ControllerVar.WINDOW_SIZE[0]/5,ControllerVar.WINDOW_SIZE[1]/10))

            pygame.draw.rect(ControllerVar.screen, (255,255,0), (Text.textRect.x, Text.textRect.y, PlayerVar.points/30*ControllerVar.WINDOW_SIZE[0]/5, ControllerVar.WINDOW_SIZE[1]/10))
        elif PlayerVar.points > 30 and PlayerVar.points < 61:
            pygame.draw.rect(ControllerVar.screen, (255,255,0), (Text.textRect.x, Text.textRect.y, ControllerVar.WINDOW_SIZE[0]/5,ControllerVar.WINDOW_SIZE[1]/10))

            pygame.draw.rect(ControllerVar.screen, (0,255,122), (Text.textRect.x, Text.textRect.y, PlayerVar.points/60*ControllerVar.WINDOW_SIZE[0]/5, ControllerVar.WINDOW_SIZE[1]/10))
        elif PlayerVar.points > 60 and PlayerVar.points < 121:
            pygame.draw.rect(ControllerVar.screen, (0,255,122), (Text.textRect.x, Text.textRect.y, ControllerVar.WINDOW_SIZE[0]/5,ControllerVar.WINDOW_SIZE[1]/10))

            pygame.draw.rect(ControllerVar.screen, (0,0,255), (Text.textRect.x, Text.textRect.y, PlayerVar.points/120*ControllerVar.WINDOW_SIZE[0]/5, ControllerVar.WINDOW_SIZE[1]/10))
        elif PlayerVar.points > 120 and PlayerVar.points < 241:
            pygame.draw.rect(ControllerVar.screen, (0,0,255), (Text.textRect.x, Text.textRect.y, ControllerVar.WINDOW_SIZE[0]/5,ControllerVar.WINDOW_SIZE[1]/10))

            pygame.draw.rect(ControllerVar.screen, (255,0,255), (Text.textRect.x, Text.textRect.y, PlayerVar.points/240*ControllerVar.WINDOW_SIZE[0]/5, ControllerVar.WINDOW_SIZE[1]/10))
        else:
            pygame.draw.rect(ControllerVar.screen, (255,0,255), (Text.textRect.x, Text.textRect.y, ControllerVar.WINDOW_SIZE[0]/5,ControllerVar.WINDOW_SIZE[1]/10))
        ControllerVar.screen.blit(text,(ControllerVar.WINDOW_SIZE[0]/1.175,ControllerVar.WINDOW_SIZE[1]/12))
        ControllerVar.screen.blit(Images.bar, Text.textRect)

        if Text.txtopen:
            ControllerVar.screen.blit(Images.txt,(ControllerVar.WINDOW_SIZE[0]/6,ControllerVar.WINDOW_SIZE[1]/1.8))
        txtbox = Text.font.render(Text.globalstring, False, (255,255,255))
        txtrect = txtbox.get_rect()
        txtrect.x, txtrect.y = [ControllerVar.WINDOW_SIZE[0]/5,ControllerVar.WINDOW_SIZE[1]/1.45]
        ControllerVar.screen.blit(txtbox,txtrect)
    else:
        ControllerVar.screen.blit(Images.gameover,(0,0))

    if PlayerVar.points <= 0:
        ControllerVar.gameover = True

    # Tick
    ControllerVar.sametickrule = True
    if TimerVar.tick_init + 0.0025 <= time.time():
        if ControllerVar.tick >= 240:
            ControllerVar.tick = 0
            if ControllerVar.tickrule >= 5:
                ControllerVar.tickrule = 0
                ControllerVar.sametickrule = False
            else:
                ControllerVar.tickrule += 1
                ControllerVar.sametickrule = False
        else:
            ControllerVar.tick += 1
            ControllerVar.sametickrule = True
        TimerVar.tick_init = time.time()

    ControllerVar.screen.blit(Images.centre, (0,0))
    
    #print(ControllerVar.screen, (ControllerVar.display.get_size()))
    # if ControllerVar.display.get_height() > ControllerVar.display.get_width() / ControllerVar.ASPECT_RATIO:
    #     print("1")
    #     ControllerVar.display.blit(pygame.transform.scale(ControllerVar.screen, (ControllerVar.display.get_width(), int(ControllerVar.display.get_width() / ControllerVar.ASPECT_RATIO))), (0, 0))
    # else:
    #     print("2")
    #     ControllerVar.display.blit(pygame.transform.scale(ControllerVar.screen, (int(ControllerVar.display.get_height() * ControllerVar.ASPECT_RATIO), ControllerVar.display.get_height())), (0, 0))
    # #ControllerVar.display.blit(pygame.transform.scale(ControllerVar.ControllerVar.display, (ControllerVar.display.get_size())), (0, 0))
    #scaled = pygame.transform.smoothscale(ControllerVar.screen,ControllerVar.display.get_size())
    #ControllerVar.display.blit(ControllerVar.screen,(0,0))

    pygame.display.flip()
    end = time.time()