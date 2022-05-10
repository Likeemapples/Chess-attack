################
# Chess Attak #
################

from tabnanny import check
from tkinter import Image
import pygame, sys, random, math, json, pickle, time
from images import Images
from variables import *
from text import *
from objects import *

from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.set_num_channels(64)
pygame.display.set_caption("Chess Attak")

# Pygame Variables
boardRect = pygame.Rect(0 + ControllerVar.size+ControllerVar.WINDOW_SIZE[0]/4.5, ControllerVar.size/1.1,ControllerVar.size*7,ControllerVar.size*7)

def initWorld():
    ChessVar.worldMap = [
        [
            [-2, "Default"],
            [-1, PlayerVar.defaultposition[0]],
            [0, [1,0],Images.chest,0], 
            [1, [2,0],Images.refugee,1,[0,1,2,3,4],Voices.refugee],
            [1, [2,1],Images.refugee,2,[0,1,5,6],Voices.refugee],
            [1, [2,2],Images.refugee,3,[10,11,12],Voices.deepvoiceText],
            [1, [2,3],Images.refugee,4,[8,9],Voices.deepvoiceText],
            [4, [5,0],Images.stairs]
        ],
        [
            [-2, "Outside"],
            [-1, PlayerVar.defaultposition[1]],
            [2, [4,0],Images.pawn,1,"Pawn"],
            [2, [4,5],Images.rook,2,"Rook"],
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
            [-1, PlayerVar.defaultposition[2]],
            [5, [4,4],Images.ladder],
            [4, [5,4],Images.stairs],
            [1, [4,5],Images.cultist,0,[13,14,15,16,17],Voices.deepvoiceText]
        ],
        [
            [-2, "Cave"],
            [-1, PlayerVar.defaultposition[3]],
            [5, [7,6],Images.ladder],
            [4, [0,0],Images.stairs]
        ],
        [
            [-2, "Swamp"],
            [-1, [0,0]],
            [2, [4,0],Images.pawn,1,"Pawn"],
            [2, [4,5],Images.rook,2,"Rook"],
            [5, [0,1],Images.ladder]
        ]
    ]
    for x in range(8):
        for y in range(8):
            if x != 4 and y != 4:
                ChessVar.worldMap[2].append([0, [x,y],Images.chest])
    PlayerVar.defaultposition = [[0,0],[5,0],[4,3]]
    PlayerVar.points = 15
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


initWorld()
# Game Loop
while True:
    ChessVar.objectlist = ChessVar.worldMap[ControllerVar.currentMap] 

    start = time.time()
    # Events
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
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
                    rect = pygame.Rect(0 + (x*ControllerVar.size+(ControllerVar.WINDOW_SIZE[0]/4)), (y*ControllerVar.size+(40)), ControllerVar.size, ControllerVar.size)
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
                temp_rect = pygame.Rect(obj[1][0]*ControllerVar.size+ControllerVar.WINDOW_SIZE[0]/4,obj[1][1]*ControllerVar.size+40,ControllerVar.size,ControllerVar.size)

            # Draw Normal
            if obj[0] == 0 or obj[0] == 3 or obj[0] == 4 or obj[0] == 5:
                ControllerVar.screen.blit(obj[2],temp_rect)
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
            if PlayerVar.playerposition[0] == obj[1][0] and PlayerVar.playerposition[1] == obj[1][1]:
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
                        ChessVar.objectlist.remove(obj)
                    case 3: # Wall
                        PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                    case 4: # Stairs
                        PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                        ControllerVar.currentMap += 1
                        ControllerVar.bulletlist = []
                    case 5: # Ladder
                        PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                        ControllerVar.currentMap -= 1
                        ControllerVar.bulletlist = []
                        

        
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
                        possiblespots = []
                        for i in range(8):
                            possiblespots.append([obj[1][0], i])
                        for b in range(8):
                            possiblespots.append([b, obj[1][1]])
                        
                        checkspot = possiblespots[random.randrange(len(possiblespots))]
                        for obj1 in ChessVar.objectlist:
                            if checkspot == obj1[1] or obj[1] == checkspot or checkspot == PlayerVar.playerposition:
                                print("ommited " + str(checkspot))
                                
                                possiblespots.remove(checkspot)
                                print(possiblespots)
                                checkspot = possiblespots[random.randrange(len(possiblespots))]
                        obj[1] = checkspot

        if ControllerVar.tickrule % 2 == 0 and ControllerVar.sametickrule == False:
            for obj in ChessVar.objectlist:
                if obj[0] == 2:
                    enemyShoot(obj[4],obj)
                    TimerVar.shoot_init = time.time()
        if ControllerVar.sametickrule == False:
            PlayerVar.isHurt = False

        # Handle Player
        
        if not PlayerVar.wading:
            PlayerVar.playerrect.x = ((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4))+(ControllerVar.size/3)
            PlayerVar.playerrect.y = ((PlayerVar.playerposition[1]*ControllerVar.size+40))+(ControllerVar.size/3)
            if PlayerVar.isHurt:
                ControllerVar.screen.blit(Images.hurt,((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4),PlayerVar.playerposition[1]*ControllerVar.size+40-20))
            else:
                ControllerVar.screen.blit(Images.player,((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4),PlayerVar.playerposition[1]*ControllerVar.size+20))
            if ControllerVar.hitboxes:
                pygame.draw.rect(ControllerVar.screen,(0,255,0),PlayerVar.playerrect,1)
        else:
            PlayerVar.playerrect.x = ((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4))+(ControllerVar.size/3)
            PlayerVar.playerrect.y = ((PlayerVar.playerposition[1]*ControllerVar.size+40))+(ControllerVar.size/1.5)
            if PlayerVar.isHurt:
                ControllerVar.screen.blit(Images.wadinghurt,((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4),PlayerVar.playerposition[1]*ControllerVar.size+40-20))
            else:
                ControllerVar.screen.blit(Images.wading,((PlayerVar.playerposition[0]*ControllerVar.size)+(ControllerVar.WINDOW_SIZE[0]/4),PlayerVar.playerposition[1]*ControllerVar.size+20))
            if ControllerVar.hitboxes:
                pygame.draw.rect(ControllerVar.screen,(0,255,0),PlayerVar.playerrect,1)

        # Handle Objects
        Chest.handleChest()

        Refugee.handleRefugee()
        
        # Enemy
        def enemyShoot(firedBy, obj):
            match firedBy:
                case "Pawn": 
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],0,1])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],1,1])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],7,1])
                case "Rook":
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],0,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],2,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],4,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],6,10])
                case "Bishop":
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],1,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],3,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],5,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],7,10])
                case "Queen":
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],0,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],1,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],2,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],3,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],4,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],5,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],6,10])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],7,10])
                case "King":
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],0,1])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],1,1])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],2,1])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],3,1])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],4,1])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],5,1])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],6,1])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],7,1])
                case "Knight":
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],8,2])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],9,2])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],10,2])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],11,2])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],12,2])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],13,2])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],14,2])
                    ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],ControllerVar.size,ControllerVar.size),[0,0],15,2])

        for bullet in ControllerVar.bulletlist:
            pos = bullet[0]
            rect = pygame.Rect(bullet[1].x, bullet[1].y, bullet[1].height/3, bullet[1].width/3)
            change = bullet[2]
            direction = bullet[3]
            distance = bullet[4]
            rect.x = (pos[0]*ControllerVar.size+ControllerVar.WINDOW_SIZE[0]/4)+ControllerVar.size/3+change[0]
            rect.y = (pos[1]*ControllerVar.size+40)+ControllerVar.size/3 + change[1]
            
            match direction:
                case 0:
                    change[1] += 0.5
                case 1:
                    change[0] -= 0.5
                    change[1] += 0.5
                case 2:
                    change[0] -= 0.5
                case 3:
                    change[0] -= 0.5
                    change[1] -= 0.5
                case 4:
                    change[1] -= 0.5
                case 5:
                    change[1] -= 0.5
                    change[0] += 0.5
                case 6:
                    change[0] += 0.5
                case 7:
                    change[0] += 0.5
                    change[1] += 0.5
                # Knight
                case 8:
                    change[0] += 0.25
                    change[1] += 0.5
                case 9:
                    change[0] -= 0.25
                    change[1] += 0.5
                case 10:
                    change[0] += 0.5
                    change[1] += 0.25
                case 11:
                    change[0] -= 0.5
                    change[1] += 0.25
                case 12:
                    change[0] += 0.25
                    change[1] -= 0.5
                case 13:
                    change[0] -= 0.25
                    change[1] -= 0.5
                case 14:
                    change[0] += 0.5
                    change[1] -= 0.25
                case 15:
                    change[0] -= 0.5
                    change[1] -= 0.25

            if abs(change[0]) >= ControllerVar.size*distance or abs(change[1]) >= ControllerVar.size*distance:
                ControllerVar.bulletlist.remove(bullet)
            ControllerVar.screen.blit(Images.bullet,rect)
            if ControllerVar.hitboxes:
                pygame.draw.rect(ControllerVar.screen,(255,0,0),rect, 1)

            if not rect.colliderect(boardRect):
                ControllerVar.bulletlist.remove(bullet)
            #if ControllerVar.tick % 47 == 0:
            if rect.colliderect(PlayerVar.playerrect) and PlayerVar.isHurt == False:
                PlayerVar.points -= 1
                PlayerVar.isHurt = True

        # Reset variables
        PlayerVar.prevspot = PlayerVar.playerposition[0], PlayerVar.playerposition[1]
        ControllerVar.click = False

        match PlayerVar.biome:
            case "Default":
                Images.tiles = [Images.white, Images.black]
                PlayerVar.wading = False
            case "Outside":
                Images.tiles = [Images.grassL, Images.grassD]
                PlayerVar.wading = False
            case "Cultist":
                Images.tiles = [Images.stoneL, Images.stoneD]
                ControllerVar.screen.blit(Images.vignette, (0,0))
                ControllerVar.screen.blit(Images.vignette2, (0,0))
                PlayerVar.wading = False
            case "Cave":
                Images.tiles = [Images.dirtL, Images.dirtD]
                PlayerVar.wading = False
            case "Swamp":
                Images.tiles = [Images.animateWater(Images.waterL,Images.waterD)[0], Images.animateWater(Images.waterL,Images.waterD)[1]]
                PlayerVar.wading = True

        
        text = Text.font.render(str(PlayerVar.points), False, (255,255,255))
        
        pygame.draw.rect(ControllerVar.screen, (255,0,0), (Text.textRect.x, Text.textRect.y, PlayerVar.points/200*ControllerVar.WINDOW_SIZE[0]/5, ControllerVar.WINDOW_SIZE[1]/10))
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

    pygame.display.flip()
    end = time.time()
    #print(ControllerVar.tickrule % 6 == 0, ControllerVar.sametickrule, ControllerVar.tickrule)
    #print(PlayerVar.defaultposition, ControllerVar.tick, ControllerVar.tickrule, len(ControllerVar.bulletlist), "elapsed time:" + str(end-start))