import pygame

pygame.init()
win = pygame.display.set_mode((1024, 1024))
clock = pygame.time.Clock()

pygame.display.set_caption("Cat Adventure")

walkRight = [pygame.image.load('cat/Walk (1).png'),pygame.image.load('cat/Walk (2).png'),pygame.image.load('cat/Walk (3).png'),pygame.image.load('cat/Walk (4).png'),pygame.image.load('cat/Walk (5).png'),pygame.image.load('cat/Walk (6).png'),pygame.image.load('cat/Walk (7).png'),pygame.image.load('cat/Walk (8).png'),pygame.image.load('cat/Walk (9).png'),pygame.image.load('cat/Walk (10).png')]
walkLeft = [pygame.image.load('cat/Walk (11).png'),pygame.image.load('cat/Walk (12).png'),pygame.image.load('cat/Walk (13).png'),pygame.image.load('cat/Walk (14).png'),pygame.image.load('cat/Walk (15).png'),pygame.image.load('cat/Walk (16).png'),pygame.image.load('cat/Walk (17).png'),pygame.image.load('cat/Walk (18).png'),pygame.image.load('cat/Walk (19).png'),pygame.image.load('cat/Walk (20).png')]
JumpMove = [pygame.image.load('cat/Jump (1).png'),pygame.image.load('cat/Jump (2).png'),pygame.image.load('cat/Jump (3).png'),pygame.image.load('cat/Jump (4).png'),pygame.image.load('cat/Jump (5).png'),pygame.image.load('cat/Jump (6).png'),pygame.image.load('cat/Jump (7).png'),pygame.image.load('cat/Jump (8).png')]
playerStand = pygame.image.load('cat/Idle (1).png')
bg2 = pygame.image.load ('backgroundColorGrass.png')
bg = pygame.image.load ('backgroundColorForest.png')

x = 0
y = 200
width = 285
heigth = 440
speed = 3

Jump = False
JumpTomp = 10

left = False
right = False
spriteCount = 0

bgx = 0
bgx2 = 1024
bgxmin = -500

def drawWindow():
    global spriteCount
    global bgx
    global bgx2
    win.blit(bg, (bgx,0))
    win.blit(bg2, (bgx2,0))

    if spriteCount +1 >= 30:
        spriteCount = 0

    if right:
        win.blit(walkRight[spriteCount // 3], (x,y))
        spriteCount += 1
    elif left:
        win.blit(walkLeft[spriteCount // 3], (x,y))
        spriteCount += 1
    elif Jump:
        win.blit(JumpMove[spriteCount // 4], (x,y))
        spriteCount += 1
    else:
        win.blit(playerStand, (x,y))
    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > -110:
        x -= speed
        if bgx < -5:
            bgx += 4
            bgx2 = bgx + 1024
        else:
            pass
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 634:
        x += speed
        bgx -= 4
        bgx2 = bgx + 1024
        left = False
        right = True
    else:
        left = False
        right = False
    if not(Jump):
            if keys[pygame.K_SPACE]:
                Jump = True
    else:
        if JumpTomp >= -10:
            if JumpTomp < 0:
                y += (JumpTomp ** 2) / 2
            else:
                y -= (JumpTomp ** 2) / 2
            JumpTomp -= 1
        else:
            Jump = False
            JumpTomp = 10
    drawWindow()
pygame.quit()
