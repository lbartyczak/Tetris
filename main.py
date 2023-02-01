import pygame as pg
import pieces
import sys, random, math

pg.init()
size = width, height = 500, 500
black = 0,0,0
screen = pg.display.set_mode(size)

background = pg.image.load("resources/background.png")
emptyTile = pg.image.load("resources/empty.png")
blue = pg.image.load("resources/blue_piece.png")
green = pg.image.load("resources/green_piece.png")
indigo = pg.image.load("resources/indigo_piece.png")
pink = pg.image.load("resources/pink_piece.png")
purple = pg.image.load("resources/purple_piece.png")
red = pg.image.load("resources/red_piece.png")
yellow = pg.image.load("resources/yellow_piece.png")
one = pg.image.load("resources/one.png")
two = pg.image.load("resources/two.png")
three = pg.image.load("resources/three.png")
four = pg.image.load("resources/four.png")
five = pg.image.load("resources/five.png")
six = pg.image.load("resources/six.png")
seven = pg.image.load("resources/seven.png")
eight = pg.image.load("resources/eight.png")
nine = pg.image.load("resources/nine.png")
zero = pg.image.load("resources/zero.png")
start = pg.image.load("resources/start.png")

images = [emptyTile, blue, green, indigo, pink, purple, red, yellow]
numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
board = [[0 for i in range(20)] for j in range(10)]
clock = pg.time.Clock()
ready = True
val = 0
speed = 500
track = 0
score = 0
level = 1

def draw_background():
    screen.fill(black)
    screen.blit(background, (140,40))

    for i in range(10):
        for j in range(20):
            screen.blit(images[board[i][j]], (150+i*20, 50 + j*20))

    temp = score
    for i in range(5, 0, -1):
        z = int(temp) % int(10)
        temp /= 10
        screen.blit(numbers[z], (360+i*16, 160))

def move(shape, horiz, vert):
    # get position of the shape
    x1, y1 = shape.position[0][0], shape.position[1][0]
    x2, y2 = shape.position[0][1], shape.position[1][1]
    x3, y3 = shape.position[0][2], shape.position[1][2]
    x4, y4 = shape.position[0][3], shape.position[1][3]

    # replace old position with empty tiles
    try:
        board[x1][y1] = 0
        board[x2][y2] = 0
    except:
        None

    board[x3][y3] = 0
    board[x4][y4] = 0

    # fill new position with shape tiles
    board[x1+horiz][y1+vert] = val
    board[x2+horiz][y2+vert] = val
    board[x3+horiz][y3+vert] = val
    board[x4+horiz][y4+vert] = val

    # update shape position
    shape.position[0][0] += horiz
    shape.position[1][0] += vert
    shape.position[0][1] += horiz
    shape.position[1][1] += vert
    shape.position[0][2] += horiz
    shape.position[1][2] += vert
    shape.position[0][3] += horiz
    shape.position[1][3] += vert

def checkBounds(shape , direction):
    # might be able to shorten this by taking in max pos and x and y increment as parameters
    # instead of direction parameter
    # direction: 0 for down, 1 for right, -1 for left
    if direction == 0:
        if max(shape.position[1]) == 19: return False
        else:
            for i in shape.borders[0][shape.orientation]:
                x = shape.position[0][i]
                y = shape.position[1][i] + 1
                if board[x][y] != 0: return False
            return True            
    elif direction == 1:
        if max(shape.position[0]) == 9: return False
        else: 
            for i in shape.borders[1][shape.orientation]:
                x = shape.position[0][i] + 1
                y = shape.position[1][i]
                if board[x][y] != 0: return False
            return True
    else:
        if min(shape.position[0]) == 0: return False
        else: 
            for i in shape.borders[2][shape.orientation]:
                x = shape.position[0][i] - 1
                y = shape.position[1][i]
                if board[x][y] != 0: return False
            return True

def plop(shape):
    # move piece all the way down
    while (checkBounds(shape, 0)):
        move(shape, 0, 1)

def rotate(shape):
    # get space requirements for rotation and check if possible
    # if not move as needed
    req = shape.deltas[shape.orientation][2]
    if req[0] == 1:
        if not checkBounds(shape, 1):
            if checkBounds(shape, -1):
                move(shape, -1, 0)
            else: return
    elif req[0] == -1:
        if not checkBounds(shape, -1):
            if checkBounds(shape, 1):
                move(shape, 1, 0)
            else: return
    elif req[1] >= 1:
        for i in range(req[1]):
            if not checkBounds(shape, 0):
                return  
    elif req[0] >= 1:
        for i in range(req[0]):
            if not checkBounds(shape, 1):
                if not checkBounds(shape, -1):
                    return
                else: move(shape, -1, 0)

    # get deltas and initial position
    x = shape.deltas[shape.orientation][0]
    y = shape.deltas[shape.orientation][1]
    px = shape.position[0]
    py = shape.position[1]

    # erase old orientation in borad and update positions
    for i in range(4):
        board[px[i]][py[i]] = 0
        shape.position[0][i] += x[i]
        shape.position[1][i] += y[i]

    # get new positions and update orientation tracker
    px = shape.position[0]
    py = shape.position[1]
    if shape.orientation == len(shape.deltas)-1: 
        shape.orientation = 0
    else: shape.orientation += 1

    # draw in new shape
    for i in range(4):
        board[px[i]][py[i]] = val

def checkRow(min):
    add = 0
    for i in range(min-4, min+1, 1):
        complete = True
        for j in range(10):
            if board[j][i] == 0: 
                complete = False
                break
        if complete:
            clearRow(i)
            add += 1
    return add * 10     

def clearRow(row):
    for i in range(row, 1, -1):
        for j in range(10):
            board[j][i] = board[j][i-1]

def checkLose():
    for i in range(9):
        if board[i][0] != 0: 
            return True

def newGame():
    screen.blit(start, (150, 175))
    pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                for i in range(20):
                    for j in range(10):
                        board[j][i] = 0
                return


while True: 
    if ready:
        num = random.randrange(10,79)
        
        if num < 20:
            deck = pieces.Sue()
        elif num < 30:
            deck = pieces.Steve()
        elif num < 40:
            deck = pieces.Larry()
        elif num < 50:
            deck = pieces.Lewis()
        elif num < 60:
            deck = pieces.TJ()
        elif num < 70:
            deck = pieces.Igor()
        elif num < 80:
            deck = pieces.Bob()
        ready = False
        val = math.floor(num/10)
        move(deck, 0 , 0)
    
    draw_background()
    pg.display.flip() 

    track += 1
    if (track == speed): 
        if (checkBounds(deck, 0)): move(deck, 0, 1)
        else: 
            if checkLose(): 
                newGame()
                score = 0
                speed = 500
            score += checkRow(max(deck.position[1]))
            ready = True
            if math.floor(score / 100) > level and speed > 50:
                level += 1
                speed -= 50
        track = 0

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()    
            if keys[pg.K_DOWN]:
                plop(deck)
            elif keys[pg.K_LEFT]:
                if checkBounds(deck, -1): move(deck, -1, 0)
            elif keys[pg.K_RIGHT]:
                if checkBounds(deck, 1): move(deck, 1, 0)
            elif keys[pg.K_SPACE]:
                try:
                    rotate(deck)
                except:
                    for i in range(4):
                        if max(deck.position[0]) > 9: move(deck, -1, 0)
                        if min(deck.position[0]) < 0: move(deck, 1, 0)
                    continue


