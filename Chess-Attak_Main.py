################
# Chess Attak #
################

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
WINDOW_SIZE = (1280,720)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((300,200))

size = round(WINDOW_SIZE[1]/9)

boardRect = pygame.Rect(0 + size+90*3, size,size*7,size*7)

worldMap = [
    [
        [-1, PlayerVar.defaultposition[0]],
        [0, [1,0],Images.chest,0], 
        [1, [2,0],Images.refugee,1,[0,1,2,3,4],Voices.refugee],
        [1, [2,1],Images.refugee,2,[0,1,5,6],Voices.refugee],
        [1, [2,2],Images.refugee,3,[0,7],Voices.deepvoiceText],
        [1, [2,3],Images.refugee,4,[8,9],Voices.deepvoiceText],
        [4, [5,0],Images.stairs]
    ],
    [
        [-1, PlayerVar.defaultposition[1]],
        [2, [4,0],Images.pawn,5,"Pawn"],
        [2, [4,5],Images.rook,6,"Rook"],
        [2, [4,6],Images.bishop,7,"Bishop"],
        [2, [4,7],Images.queen,8,"Queen"],
        [2, [4,3],Images.king,9,"King"],
        [2, [4,2],Images.knight,9,"Knight"],
        [5, [5,1],Images.ladder]
    ]
] # object(object type, object pos(object x, object y), image, count, nbt) # [0,[1,0],chest,0,1]

# Game Loop
while True:
    
    objectlist = worldMap[ControllerVar.currentMap] 

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
            if event.key == K_z:
                Text.globalnum = 0
                Text.globalstring = ""
                Text.nbtNum += 1
            if event.key == K_e:
                ControllerVar.hitboxes = not ControllerVar.hitboxes
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                ControllerVar.click = True
    

    # Draw Table
    screen.blit(Images.table, (0,0))


    # Mouse
    mx, my = pygame.mouse.get_pos()
    mouse = pygame.Rect(mx,my,1,1)


    # Initialize Chess
    if ChessVar.tilecount <= 64:
        for y in range(8):
            for x in range(8):
                rect = pygame.Rect(0 + (x*size+(90*3.5)), (y*size+(40)), size, size)
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
                #objectlist.append([0,[x,y],Images.chest]) # DRAW CHEST EVERYWHERE
                
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
        if rect.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,0,0),rect)
        elif tile[5] == 0:
            pygame.draw.rect(screen, (0,0,0), rect)
        else:
            pygame.draw.rect(screen, (255,255,255), rect)

    # Initialize and Handle Objects
    for obj in objectlist:
        temp_rect = pygame.Rect((obj[1][0]*80)+(90*3.5),(obj[1][1]*80)+40,size,size)
        if obj[0] == 0 or obj[0] == 3 or obj[0] == 4 or obj[0] == 5:
            screen.blit(obj[2],temp_rect)
            if ControllerVar.hitboxes:
                pygame.draw.rect(screen,(0,0,255),temp_rect,1)
        elif obj[0] != -1:
            temp_rect.y -= 20
            screen.blit(obj[2],temp_rect)
            if ControllerVar.hitboxes:
                pygame.draw.rect(screen,(0,0,255),temp_rect,1)
        
        match obj[0]:
            case -1: # Player
                PlayerVar.playerposition = PlayerVar.defaultposition[ControllerVar.currentMap]
                PlayerVar.defaultposition[ControllerVar.currentMap] = PlayerVar.playerposition
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
                    objectlist.remove(obj)
                case 1: # Refugee
                    TimerVar.text_init = time.time()
                    Text.nbt = obj[4]
                    Text.voice = obj[5]
                    Text.txtopen = True
                    PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                case 2: # Enemy
                    PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                    objectlist.remove(obj)
                case 3: # Wall
                    PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                case 4: # Stairs
                    PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                    ControllerVar.currentMap += 1
                    ControllerVar.bulletlist = []
                case 5: # Stairs
                    PlayerVar.playerposition[0], PlayerVar.playerposition[1] = PlayerVar.prevspot
                    ControllerVar.currentMap -= 1
                    ControllerVar.bulletlist = []
                    
    if TimerVar.shoot_init + 1.5 <= time.time():
        for obj in objectlist:
            if obj[0] == 2:
                enemyShoot(obj[4],obj)
                TimerVar.shoot_init = time.time()
    
    if TimerVar.move_init + 3 <= time.time():
        for obj in objectlist:
            if obj[0] == 2:
                if obj[4] == "Pawn":
                    for obj1 in objectlist:
                        if obj[1][1] + 1 == obj1[1][1] and obj[1][0] == obj1[1][0] and obj != obj1:
                            TimerVar.canMove = False
                    if obj[1][1] != 7 and TimerVar.canMove:
                        obj[1][1] += 1
                    TimerVar.move_init = time.time()


    # Handle Player
    PlayerVar.playerrect.x = ((PlayerVar.playerposition[0]*80)+(90*3.5))+(size/3)
    PlayerVar.playerrect.y = ((PlayerVar.playerposition[1]*80+40))+(size/3)
    screen.blit(Images.player,((PlayerVar.playerposition[0]*80)+(90*3.5),PlayerVar.playerposition[1]*80+40-20))
    if ControllerVar.hitboxes:
        pygame.draw.rect(screen,(0,255,0),PlayerVar.playerrect,1)


    Chest.handleChest()

    Refugee.handleRefugee()
    
    # Enemy
    def enemyShoot(firedBy, obj):
        match firedBy:
            case "Pawn": 
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],0,1])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],1,1])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],7,1])
            case "Rook":
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],0,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],2,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],4,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],6,10])
            case "Bishop":
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],1,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],3,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],5,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],7,10])
            case "Queen":
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],0,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],1,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],2,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],3,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],4,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],5,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],6,10])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],7,10])
            case "King":
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],0,1])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],1,1])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],2,1])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],3,1])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],4,1])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],5,1])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],6,1])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],7,1])
            case "Knight":
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],8,2])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],9,2])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],10,2])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],11,2])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],12,2])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],13,2])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],14,2])
                ControllerVar.bulletlist.append([obj[1],pygame.Rect(obj[1][0],obj[1][1],size,size),[0,0],15,2])

    for bullet in ControllerVar.bulletlist:
        pos = bullet[0]
        rect = pygame.Rect(bullet[1].x, bullet[1].y, bullet[1].height/3, bullet[1].width/3)
        change = bullet[2]
        direction = bullet[3]
        distance = bullet[4]
        rect.x = (pos[0]*80+90*3.5)+size/3+change[0]
        rect.y = (pos[1]*80+40)+size/3 + change[1]
        
        match direction:
            case 0:
                change[1] += 1
            case 1:
                change[0] -= 1
                change[1] += 1
            case 2:
                change[0] -= 1
            case 3:
                change[0] -= 1
                change[1] -= 1
            case 4:
                change[1] -= 1
            case 5:
                change[1] -= 1
                change[0] += 1
            case 6:
                change[0] += 1
            case 7:
                change[0] += 1
                change[1] += 1
            # Knight
            case 8:
                change[0] += 0.5
                change[1] += 1
            case 9:
                change[0] -= 0.5
                change[1] += 1
            case 10:
                change[0] += 1
                change[1] += 0.5
            case 11:
                change[0] -= 1
                change[1] += 0.5
            case 12:
                change[0] += 0.5
                change[1] -= 1
            case 13:
                change[0] -= 0.5
                change[1] -= 1
            case 14:
                change[0] += 1
                change[1] -= 0.5
            case 15:
                change[0] -= 1
                change[1] -= 0.5


        if abs(change[0]) >= size*distance or abs(change[1]) >= size*distance:
            ControllerVar.bulletlist.remove(bullet)
        screen.blit(Images.bullet,rect)
        if ControllerVar.hitboxes:
            pygame.draw.rect(screen,(255,0,0),rect, 1)

        if not rect.colliderect(boardRect):
            ControllerVar.bulletlist.remove(bullet)

        if rect.colliderect(PlayerVar.playerrect):
            PlayerVar.points -= 1

    # Reset variables
    PlayerVar.prevspot = PlayerVar.playerposition[0], PlayerVar.playerposition[1]
    ControllerVar.click = False


    pygame.display.flip()
    print(len(ControllerVar.bulletlist))
    end = time.time()
    print("elapsed time:" + str(end-start))