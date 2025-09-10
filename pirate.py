# import the pygame module
import math
import random

import pygame

# will make it easier to use pygame functions
from pygame.draw import line, circle, rect

# initializes the pygame module
pygame.init()

# creates a screen variable of size 800 x 600
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("PIERATE")
pygame.mouse.set_visible(False)

# controls the main game while loop
done = False

# sets the frame rate of the program
clock = pygame.time.Clock()

# colour variables, (R, G, B) from 0-255
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


# your FUNCTIONS go here
def createImg():
    global sky, island, waterB
    for w in range(1, 15):
        imgWhale = pygame.image.load(f'images/whale{w}.png')
        # imgWhale = pygame.transform.scale(imgWhale, (136, 92))
        whale.append(pygame.transform.flip(imgWhale, True, False))


    for u in range(1, 9):
        imgSword = pygame.image.load(f'images/Sword Idle 0{u}.png')
        imgSword = pygame.transform.scale(imgSword, (50, 50))
        sword.append(imgSword)

    for i in range(1, 6):
        imgIdle = pygame.image.load(f'images/Pirate Idle 0{i}.png')
        imgIdle = pygame.transform.scale(imgIdle, (128, 80))
        pirateIdleR.append(imgIdle)
        pirateIdleL.append(pygame.transform.flip(imgIdle, True, False))
        shopPirateIdleR.append(pygame.transform.scale(imgIdle, (256, 160)))

    for c in range(1, 10):
        imgIdle = pygame.image.load(f'images/Crab Idle 0{c}.png')
        imgIdle = pygame.transform.scale(imgIdle, (128, 80))
        crabIdleL.append(imgIdle)
        crabIdleR.append(pygame.transform.flip(imgIdle, True, False))
        shopCrabIdleR.append(pygame.transform.scale(pygame.transform.flip(imgIdle, True, False), (256, 160)))

    for y in range(1, 9):
        imgIdle = pygame.image.load(f'images/Star Idle 0{y}.png')
        imgIdle = pygame.transform.scale(imgIdle, (128, 80))
        starIdleL.append(imgIdle)
        starIdleR.append(pygame.transform.flip(imgIdle, True, False))
        shopStarIdleR.append(pygame.transform.scale(pygame.transform.flip(imgIdle, True, False), (256, 160)))

        imgIdle = pygame.image.load(f'images/Shark Idle 0{y}.png')
        imgIdle = pygame.transform.scale(imgIdle, (128, 80))
        sharkIdleL.append(imgIdle)
        sharkIdleR.append(pygame.transform.flip(imgIdle, True, False))
        shopSharkIdleR.append(pygame.transform.scale(pygame.transform.flip(imgIdle, True, False), (256, 160)))


    for r in range(1, 7):
        imgRun = pygame.image.load(f'images/Pirate Run 0{r}.png')
        imgRun = pygame.transform.scale(imgRun, (128, 80))
        pirateRunR.append(imgRun)
        pirateRunL.append(pygame.transform.flip(imgRun, True, False))

        imgRun = pygame.image.load(f'images/Crab Run 0{r}.png')
        imgRun = pygame.transform.scale(imgRun, (128, 80))
        crabRunL.append(imgRun)
        crabRunR.append(pygame.transform.flip(imgRun, True, False))

        imgRun = pygame.image.load(f'images/Star Run 0{r}.png')
        imgRun = pygame.transform.scale(imgRun, (128, 80))
        starRunL.append(imgRun)
        starRunR.append(pygame.transform.flip(imgRun, True, False))

        imgRun = pygame.image.load(f'images/Shark Run 0{r}.png')
        imgRun = pygame.transform.scale(imgRun, (128, 80))
        sharkRunL.append(imgRun)
        sharkRunR.append(pygame.transform.flip(imgRun, True, False))
    for k in range(1, 9):
        keyImg = pygame.image.load(f'images/key 0{k}.png')
        keyImg = pygame.transform.scale(keyImg, (50, 50))
        keys.append(keyImg)

    for z in range(1, 5):
        windImg = pygame.image.load(f'images/wind{z}.png')
        windImg = pygame.transform.scale(windImg, (91, 136))
        windR.append(windImg)
        windL.append(pygame.transform.flip(windImg, True, False))

    sky = pygame.image.load('images/sky.png')
    sky = pygame.transform.scale(sky, (800, 600))
    island = pygame.image.load('images/island.png')
    island = pygame.transform.scale(island, (1000, 500))

    waterB = pygame.image.load('images/bWater.png')
    waterB = pygame.transform.scale(waterB, (800, 50))
    for w in range(1, 5):
        water = pygame.image.load(f'images/water{w}.png')
        water = pygame.transform.scale(water, (200, 50))
        waterTop.append(water)
    for b in range(1, 7):
        boatImg = pygame.image.load(f'images/ship{b}.png')
        boatImg = pygame.transform.scale(boatImg, (260, 72))
        boatR.append(boatImg)
        boatL.append(pygame.transform.flip(boatImg, True, False))

    for e in range(1, 5):
        birdImg = pygame.image.load(f'images/bird-{e} (dragged).tiff')
        birdImg = pygame.transform.scale(birdImg, (57, 48))
        birdR.append(birdImg)
        birdL.append(pygame.transform.flip(birdImg, True, False))

    for d in range(1, 27):
        letterImg = pygame.image.load(f'images/letter{d}.png')
        letterImg = pygame.transform.scale(letterImg, (20, 22))
        letter.append(letterImg)

    for y in range(0, 10):
        numImg = pygame.image.load(f'images/num{y}.png')
        numImg = pygame.transform.scale(numImg, (20, 22))
        number.append(numImg)

    for b in range(1, 4):
        navImg = pygame.image.load(f'images/nav{b}.png')
        navImg = pygame.transform.scale(navImg, (60, 60))
        nav.append(navImg)

    for q in range(1, 9):
        skullImg = pygame.image.load(f'images/skull0{q}.png')
        skullImg = pygame.transform.scale(skullImg, (48, 56))
        skull.append(skullImg)

    for b in range(1, 10):
        boardImg = pygame.image.load(f'images/board{b}.png')
        boardImg = pygame.transform.scale(boardImg, (100, 100))
        if b < 4:
            board[0].append(boardImg)
        elif b < 7:
            board[1].append(boardImg)
        else:
            board[2].append(boardImg)

    for c in range(1, 5):
        coinImg = pygame.image.load(f'images/coin{c}.png')
        coinImg = pygame.transform.scale(coinImg, (64, 64))
        coin.append(coinImg)

    for n in range(1, 4):
        powerImg = pygame.image.load(f'images/powerBar{n}.png')
        powerImg = pygame.transform.scale(powerImg, (80, 80))
        powerBar.append(powerImg)

    for u in range(1, 4):
        uptabImg = pygame.image.load(f'images/upTab{u}.png')
        uptabImg = pygame.transform.scale(uptabImg, (150, 110))
        upTab.append(uptabImg)



def user():
    global counter, switch, pirateX, pirateY, direction, justJumped, idle, run, jump, jumpSequence, fallSequence, \
        aniFall, onBoat
    if key[pygame.K_a]:
        pirateX -= 5
        idle = False
        run = True
        direction = 1

    elif key[pygame.K_d]:
        pirateX += 5
        idle = False
        run = True
        direction = 0

    else:
        idle = True
        run = False

    if key[pygame.K_SPACE]:
        if not justJumped and not jumpSequence and not fallSequence:
            if onBoat:
                justJumped = True
                jump = True
                jumpSequence = True
    else:
        justJumped = False

    if jumpSequence:
        if pirateY >= 300:
            pirateY -= 3
        else:
            jumpSequence = False
            fallSequence = True

    if fallSequence:
        aniFall = True
        if onBoat:
            if pirateY < 410:
                pirateY += 3
            else:
                fallSequence = False
        else:
            pirateY += 3

    # if pirateX
    oneBoat = 0
    for i in range(0, len(boatX)):
        if boatX[i] + 5 < pirateX + 44 < boatX[i] + 255 or boatX[i] + 5 < pirateX + 84 < boatX[i] + 255:
            oneBoat += 1
            if pirateY <= 410:
                onBoat = True
                pirateX += windSpeed

        if oneBoat == 0:
            onBoat = False
        # circle(screen, BLACK, (boatX[i]+5, 485,), 5, 0)
        # circle(screen, BLACK, (boatX[i] + 255, 485,), 5, 0)
        # circle(screen, BLACK, (pirateX, pirateY+60), 5, 0)
        # circle(screen, BLACK, (pirateX + 44, pirateY), 5, 0)
        # circle(screen, BLACK, (pirateX + 84, pirateY), 5, 0)
    if not onBoat and not jumpSequence or dead:
        pirateY += 3

    if pirateY > 410:
        if onBoat:
            pirateY = 410

    if counter > 6:
        switch += 1
        counter = 0

    if idle:
        if switch > len(idleR) - 1:
            switch = 0
        if direction == 0:
            screen.blit(idleR[switch], (pirateX, pirateY))
        else:
            screen.blit(idleL[switch], (pirateX, pirateY))
    elif run:
        if switch > len(runR)-1:
            switch = 0
        if direction == 0:
            screen.blit(runR[switch], (pirateX, pirateY))
        else:
            screen.blit(runL[switch], (pirateX, pirateY))

    counter += 1


def throw():
    global justThrown, pieRise, pieRun, riseY, runX
    # line(screen, BLACK, (pirateX + 64, pirateY+40), (xMouse, yMouse), 1)
    # line(screen, BLUE, (pirateX + 64, pirateY+40), (xMouse, pirateY+40), 1)
    # line(screen, RED, (xMouse, pirateY+40), (xMouse, yMouse), 1)

    angle = math.atan2(yMouse - (pirateY + 40), xMouse - (pirateX + 64))
    circle(screen, WHITE, (pirateX + 64 + (math.cos(angle) * 45), pirateY + 40 + (math.sin(angle) * 45)), 5, 0)
    circle(screen, BLACK, (pirateX + 64 + (math.cos(angle) * 45), pirateY + 40 + (math.sin(angle) * 45)), 6, 2)

    if clicks[0]:
        if not justThrown:
            justThrown = True
            # print(int(angle*180/math.pi))
            dx = math.cos(angle)
            dy = math.sin(angle)

            # print(dx, dy)
            pieRise.append(dy)
            pieRun.append(dx)
            pieX.append((pirateX + 64) - 18)
            pieY.append(pirateY + 20)
    else:
        justThrown = False

    if len(pieX) > 0:
        for i in range(0, len(pieX)):
            if 0 < pieX[i] + 18 < 800 and 0 < pieY[i] + 19 < 600:
                pieX[i] += pieRun[i] * 3
                pieY[i] += pieRise[i] * 3
            else:
                pieX.remove(pieX[i])
                pieY.remove(pieY[i])
                pieRun.remove(pieRun[i])
                pieRise.remove(pieRise[i])
                break
        for k in range(0, len(pieX)):
            screen.blit(imgPie, (pieX[k], pieY[k]))


def background():
    global waterCounter, switchWater, boatCounter, switchBoat, windCounter, switchWind, windSpeed, boatX, pirateY, \
        pirateX, timeSwitch, boatDirection, addSpikes, addCoins
    screen.blit(sky, (0, 0))
    screen.blit(island, (0, 200))
    screen.blit(waterB, (0, 550))

    if boatCounter >= 10:
        switchBoat += 1
        boatCounter = 0
    if switchBoat > 5:
        switchBoat = 0
    # windSpeed = 1
    for i in range(0, len(boatX)):
        if boatDirection == 0:
            boatX[i] += windSpeed
            if boatX[i] > 800:
                boatX[i] = -270
                addCoins = i
                if haveSpikes:
                    addSpikes = i
            screen.blit(boatR[switchBoat], (boatX[i], 465))
            screen.blit(windR[switchWind], (boatX[i] + 150, 335))
        else:
            boatX[i] -= windSpeed
            if boatX[i] < 0:
                boatX[i] = 1070
            screen.blit(boatL[switchBoat], (boatX[i], 465))
            screen.blit(windL[switchWind], (boatX[i] + 150, 335))

    if windCounter >= 10:
        switchWind += 1
        windCounter = 0
    if switchWind > 3:
        switchWind = 0

    if waterCounter >= 12:
        switchWater += 1
        waterCounter = 0
    if switchWater > 3:
        switchWater = 0
    for g in range(0, 4):
        screen.blit(waterTop[switchWater], (waterX[g], 500))

    waterCounter += 1
    boatCounter += 1
    windCounter += 1


def enemy():
    global birdCounter, switchBird, spawnCounter, timer, amtBird, speedBird, bDirect, haveSpikes, spikeCounter, spikeX, \
        spikeTimer, addSpikes, whaleY, whaleX, whaleSwap, whaleCounter, haveWhale
    if score > 30:
        if not power:
            speedBird = 4
        spawnCounter = 60
    elif score > 20:
        if not power:
            speedBird = 3
        spawnCounter = 80
        haveWhale = True
    elif score > 10:
        spawnCounter = 100
        if not power:
            speedBird = 2
        haveSpikes = True
        spikeCounter = 1
    if haveSpikes:
        if spikeCounter > 0:
            if addSpikes in [0, 1, 2]:
                for k in range(0, spikeCounter):
                    spikeX.append(random.randint(boatX[addSpikes] + 10, boatX[addSpikes] + 220))
                addSpikes = 3
    if len(spikeX) > 0:
        for j in range(0, len(spikeX)):
            screen.blit(spikes, (spikeX[j], 440))
            spikeX[j] += windSpeed

    if timer >= spawnCounter:
        timer = 0
        amtBird += 1
        # print("new bird")
        birdY.append(-50)
        birdX.append(random.randint(-60, 800))
    timer += 1
    if birdCounter >= 9:
        switchBird += 1
        birdCounter = 0
    if switchBird > 3:
        switchBird = 0
    birdCounter += 1
    if amtBird > 0:
        for i in range(0, amtBird):
            angleBird = math.atan2(pirateY + 20 - (birdY[i] + 24), pirateX + 64 - (birdX[i] + 29))
            bx = math.cos(angleBird)
            by = math.sin(angleBird)
            if birdX[i] + 29 < pirateX + 64:
                bDirect = 0
                birdX[i] += bx * speedBird
            elif birdX[i] + 29 > pirateX + 64:
                bDirect = 1
                birdX[i] += bx * speedBird
            if birdY[i] + 24 < pirateY + 20:
                birdY[i] += by * speedBird
            elif birdY[i] + 24 > pirateY + 20:
                birdY[i] += by * speedBird
            if bDirect == 1:
                screen.blit(birdR[switchBird], (birdX[i], birdY[i]))
            else:
                screen.blit(birdL[switchBird], (birdX[i], birdY[i]))

    if whaleCounter >= 6:
        whaleSwap += 1
        whaleCounter = 0
    if whaleSwap > 13:
        whaleSwap = 0
    whaleCounter += 1

    # if haveWhale:


    # t = pygame.time.get_ticks() / 5 % 1000
    # whaleX = t
    # whaleY = math.sin(t / 50) * 90 + 500

    whaleX += 1
    screen.blit(whale[whaleSwap], (whaleX, whaleY))


def collision():
    global amtBird, score, dead, lengthColour
    birdRemove = [[]]
    topPirateY = pirateY + 12
    leftPirateX = pirateX + 44
    botPirateY = pirateY + 60
    rightPirateX = pirateX + 84
    if amtBird > 0:
        for b in range(0, amtBird):
            topBirdY = birdY[b] + 20
            topBirdX = birdX[b] + 5
            botBirdY = birdY[b] + 33
            botBirdX = birdX[b] + 57
            if len(pieX) > 0:
                for p in range(0, len(pieX)):
                    topPieY = pieY[p] + 5
                    topPieX = pieX[p] + 5
                    botPieY = pieY[p] + 25
                    botPieX = pieX[p] + 25
                    if botBirdY > topPieY > topBirdY or botBirdY > botPieY > topBirdY:
                        if botBirdX > topPieX > topBirdX or botBirdX > botPieX > topBirdX:
                            for k in range(0, len(birdRemove)):
                                birdRemove[k].append(birdY.index(birdY[b]))
                                birdRemove[k].append(birdX.index(birdX[b]))
                                birdRemove.append([])
            if botBirdY > topPirateY > topBirdY or botBirdY > botPirateY > topBirdY:
                if botBirdX > leftPirateX > topBirdX or botBirdX > rightPirateX > topBirdX:
                    dead = True
    # circle(screen, BLACK, (pirateX, pirateY + 60), 5, 0)
    # circle(screen, BLACK, (pirateX + 44, pirateY + 12), 5, 0)
    # circle(screen, BLACK, (pirateX + 84, pirateY), 5, 0)
    if len(birdRemove) > 1:
        for i in range(0, len(birdRemove)):
            del birdY[birdRemove[i][0]]
            del birdX[birdRemove[i][1]]
            amtBird -= 1
            score += 1
            lengthColour += 16
            if lengthColour > 160:
                lengthColour = 160
            break
    if len(spikeX) > 0:
        for k in range(0, len(spikeX)):
            if spikeX[k] + 10 < leftPirateX < spikeX[k] + 40 or spikeX[k] + 10 < rightPirateX < spikeX[k] + 40:
                if 455 < botPirateY < 472:
                    dead = True
    if whaleX < pirateX < whaleX + 66 or whaleX < pirateX + 128 < whaleX + 66:
        if whaleY < pirateY + 80:
            dead = True


def death():
    global pirateY, pirateX, dead, fallSequence, jumpSequence, stay, selection, speedBird, windSpeed, endLetters, \
        justClickedD, justClickedU, skullCounter, switchSkull, gameStart, lockerVar, shopVar, justClickedR, \
        justClickedL, mainScreen, justDeadClickedReturn, deadNum, titleEnd, justDead
    if pirateY > 550:
        dead = True
    if pirateX + 128 < 0:
        dead = True
    if pirateX > 800:
        dead = True

    if dead:
        if not justDead:
            gameOverSound.play()
            justDead = True
        fallSequence = False
        jumpSequence = False
        pirateY += 3
        if pirateY > 800:
            speedBird = 0
            windSpeed = 0
            screen.blit(board[0][0], (0, 0))
            screen.blit(board[0][1], (100, 0))
            screen.blit(board[0][1], (200, 0))
            screen.blit(board[0][1], (300, 0))
            screen.blit(board[0][1], (400, 0))
            screen.blit(board[0][1], (500, 0))
            screen.blit(board[0][1], (600, 0))
            screen.blit(board[0][2], (700, 0))

            screen.blit(board[1][0], (0, 100))
            screen.blit(board[1][0], (0, 200))
            screen.blit(board[1][0], (0, 300))
            screen.blit(board[1][0], (0, 400))
            screen.blit(board[1][2], (700, 100))
            screen.blit(board[1][2], (700, 200))
            screen.blit(board[1][2], (700, 300))
            screen.blit(board[1][2], (700, 400))

            screen.blit(board[2][0], (0, 500))
            screen.blit(board[2][1], (100, 500))
            screen.blit(board[2][1], (200, 500))
            screen.blit(board[2][1], (300, 500))
            screen.blit(board[2][1], (400, 500))
            screen.blit(board[2][1], (500, 500))
            screen.blit(board[2][1], (600, 500))
            screen.blit(board[2][2], (700, 500))

            screen.blit(board[1][1], (100, 100))
            screen.blit(board[1][1], (200, 100))
            screen.blit(board[1][1], (300, 100))
            screen.blit(board[1][1], (400, 100))
            screen.blit(board[1][1], (500, 100))
            screen.blit(board[1][1], (600, 100))

            screen.blit(board[1][1], (100, 200))
            screen.blit(board[1][1], (200, 200))
            screen.blit(board[1][1], (300, 200))
            screen.blit(board[1][1], (400, 200))
            screen.blit(board[1][1], (500, 200))
            screen.blit(board[1][1], (600, 200))

            screen.blit(board[1][1], (100, 300))
            screen.blit(board[1][1], (200, 300))
            screen.blit(board[1][1], (300, 300))
            screen.blit(board[1][1], (400, 300))
            screen.blit(board[1][1], (500, 300))
            screen.blit(board[1][1], (600, 300))

            screen.blit(board[1][1], (100, 400))
            screen.blit(board[1][1], (200, 400))
            screen.blit(board[1][1], (300, 400))
            screen.blit(board[1][1], (400, 400))
            screen.blit(board[1][1], (500, 400))
            screen.blit(board[1][1], (600, 400))

            for i in range(0, 3):
                newNav[i] = pygame.transform.scale(nav[i], (80, 100))

            for l in range(1, 4):
                screen.blit(newNav[0], (70, tabY[l] - 50))
                screen.blit(newNav[1], (150, tabY[l] - 50))
                screen.blit(newNav[1], (230, tabY[l] - 50))
                screen.blit(newNav[1], (310, tabY[l] - 50))
                screen.blit(newNav[1], (390, tabY[l] - 50))
                screen.blit(newNav[2], (470, tabY[l] - 50))

            screen.blit(upTab[0], (600, tabY[1] - 50))
            screen.blit(upTab[1], (600, tabY[2] - 50))
            screen.blit(upTab[2], (600, tabY[3] - 50))

            for k in range(0, len(letter)):
                endLetters.append(pygame.transform.scale(letter[k], (40, 40)))


            screen.blit(titleEnd[16], (650, tabY[1] - 20))
            screen.blit(titleEnd[20], (650, tabY[2] - 60))
            screen.blit(titleEnd[8], (650, tabY[2] + 5))
            screen.blit(titleEnd[19], (650, tabY[3] - 35))


            screen.blit(titleEnd[18], (50, 55))
            screen.blit(titleEnd[2], (105, 55))
            screen.blit(titleEnd[14], (160, 55))
            screen.blit(titleEnd[17], (215, 55))
            screen.blit(titleEnd[4], (270, 55))

            screen.blit(titleEnd[2], (50, 140))
            screen.blit(titleEnd[14], (105, 140))
            screen.blit(titleEnd[8], (160, 140))
            screen.blit(titleEnd[13], (215, 140))
            screen.blit(titleEnd[18], (270, 140))


            num = score / 10
            intNum, dec = divmod(num, 1)
            decimal = round(dec * 10)
            floorNum = num.__floor__()

            if floorNum > 9:
                newNum = floorNum / 10
                intNum1, newdec = divmod(newNum, 1)
                newDecimal = round(newdec * 10)
                newfloorNum = newNum.__floor__()
                screen.blit(deadNum[newfloorNum], (deadNumX[0], 55))
                screen.blit(deadNum[newDecimal], (deadNumX[1], 55))
                screen.blit(deadNum[decimal], (deadNumX[2], 55))

            elif floorNum > 0:
                screen.blit(deadNum[floorNum], (deadNumX[0], 55))
                screen.blit(deadNum[decimal], (deadNumX[1], 55))

            else:
                screen.blit(deadNum[score], (deadNumX[0], 55))

            coinNum = gameCoins / 10
            intCoin, coinDec = divmod(coinNum, 1)
            coinDecimal = round(coinDec * 10)
            floorCoin = coinNum.__floor__()

            if floorCoin > 9:
                newNumCoin = floorCoin / 10
                intNum1, newdecCoin = divmod(newNumCoin, 1)
                newDecimalCoin = round(newdecCoin * 10)
                newfloorNumCoin = newNumCoin.__floor__()
                screen.blit(deadNum[newfloorNumCoin], (deadNumX[0], 140))
                screen.blit(deadNum[newDecimalCoin], (deadNumX[1], 140))
                screen.blit(deadNum[coinDecimal], (deadNumX[2], 140))

            elif floorCoin > 0:
                screen.blit(deadNum[floorCoin], (deadNumX[0], 140))
                screen.blit(deadNum[coinDecimal], (deadNumX[1], 140))

            else:
                screen.blit(deadNum[gameCoins], (deadNumX[0], 140))

            screen.blit(endLetters[17], (120, tabY[1] - 28))
            screen.blit(endLetters[4], (175, tabY[1] - 28))
            screen.blit(endLetters[18], (230, tabY[1] - 28))
            screen.blit(endLetters[19], (285, tabY[1] - 28))
            screen.blit(endLetters[0], (340, tabY[1] - 28))
            screen.blit(endLetters[17], (395, tabY[1] - 28))
            screen.blit(endLetters[19], (450, tabY[1] - 28))

            screen.blit(tabLettersImg[1][0], (148, tabY[2] -28))
            screen.blit(tabLettersImg[1][1], (203, tabY[2] -28))
            screen.blit(tabLettersImg[1][2], (258, tabY[2] -28))
            screen.blit(tabLettersImg[1][3], (313, tabY[2] -28))
            screen.blit(tabLettersImg[1][4], (368, tabY[2] -28))
            screen.blit(tabLettersImg[1][5], (423, tabY[2] -28))

            screen.blit(tabLettersImg[2][0], (203, tabY[3] -28))
            screen.blit(tabLettersImg[2][1], (258, tabY[3] -28))
            screen.blit(tabLettersImg[2][2], (313, tabY[3] -28))
            screen.blit(tabLettersImg[2][3], (368, tabY[3] -28))

            if key[pygame.K_DOWN]:
                if not justClickedD:
                    justClickedD = True
                    if 0 <= selection < 2:
                        selection += 1
            else:
                justClickedD = False

            if key[pygame.K_UP]:
                if not justClickedU:
                    justClickedU = True
                    if 2 >= selection > 0:
                        selection -= 1
            else:
                justClickedU = False

            if key[pygame.K_RIGHT]:
                if not justClickedR:
                    justClickedR = True
                    if selection != -1:
                        selection = -1
            else:
                justClickedR = False

            if key[pygame.K_LEFT]:
                if not justClickedL:
                    justClickedL = True
                    if selection == -1:
                        selection = 0
            else:
                justClickedL = False

            if key[pygame.K_SPACE] or key[pygame.K_RETURN]:
                justDeadClickedReturn = True
                dead = False
                gameStart = False
                justDead = False
                if selection == 0:
                    gameStart = True
                    resetGame()
                if selection == 1:
                    lockerVar = True
                if selection == 2:
                    shopVar = True
                if selection == -1:
                    mainScreen = True
                    resetGame()
                    selection = 0


            if skullCounter >= 9:
                switchSkull += 1
                skullCounter = 0
            if switchSkull > 7:
                switchSkull = 0
            if selection >= 0:
                screen.blit(skull[switchSkull], (25, tabY[selection + 1] - 40))
                screen.blit(skull[switchSkull], (545, tabY[selection + 1] - 40))
            else:
                screen.blit(skull[switchSkull], (650, 165))
                screen.blit(skull[switchSkull], (650, 510))


            skullCounter += 1


def navBar():
    global colourBar
    screen.blit(nav[0], (380, 0))
    screen.blit(nav[1], (440, 0))
    screen.blit(nav[1], (500, 0))
    screen.blit(nav[1], (560, 0))
    screen.blit(nav[1], (620, 0))
    screen.blit(nav[1], (680, 0))
    screen.blit(nav[2], (740, 0))

    screen.blit(letter[18], (400, 15))
    screen.blit(letter[2], (422, 15))
    screen.blit(letter[14], (444, 15))
    screen.blit(letter[17], (466, 15))
    screen.blit(letter[4], (488, 15,))

    num = score / 10
    intNum, dec = divmod(num, 1)
    decimal = round(dec * 10)
    floorNum = num.__floor__()

    screen.blit(powerBar[0], (10, -10))
    screen.blit(powerBar[1], (74, -10))
    screen.blit(powerBar[2], (138, -10))
    newColourBar = pygame.transform.scale(colourBar, (lengthColour, 10))
    screen.blit(newColourBar, (50, 25))

    if floorNum > 9:
        newNum = floorNum / 10
        intNum1, newdec = divmod(newNum, 1)
        newDecimal = round(newdec * 10)
        newfloorNum = newNum.__floor__()
        location = numberX[2] + 132
        screen.blit(number[newfloorNum], (numberX[0], 15))
        screen.blit(number[newDecimal], (numberX[1], 15))
        screen.blit(number[decimal], (numberX[2], 15))

        screen.blit(letter[2], (numberX[2] + 40, 15))
        screen.blit(letter[14], (numberX[2] + 66, 15))
        screen.blit(letter[8], (numberX[2] + 88, 15))
        screen.blit(letter[13], (numberX[2] + 110, 15))
        screen.blit(letter[18], (numberX[2] + 132, 15))


    elif floorNum > 0:
        location = numberX[1] + 132

        screen.blit(number[floorNum], (numberX[0], 15))
        screen.blit(number[decimal], (numberX[1], 15))

        screen.blit(letter[2], (numberX[1] + 40, 15))
        screen.blit(letter[14], (numberX[1] + 66, 15))
        screen.blit(letter[8], (numberX[1] + 88, 15))
        screen.blit(letter[13], (numberX[1] + 110, 15))
        screen.blit(letter[18], (numberX[1] + 132, 15))
    else:
        location = numberX[0] + 132
        screen.blit(number[score], (numberX[0], 15))
        screen.blit(letter[2], (numberX[0] + 40, 15))
        screen.blit(letter[14], (numberX[0] + 66, 15))
        screen.blit(letter[8], (numberX[0] + 88, 15))
        screen.blit(letter[13], (numberX[0] + 110, 15))
        screen.blit(letter[18], (numberX[0] + 132, 15))

    coinNum = gameCoins / 10
    intCoin, coinDec = divmod(coinNum, 1)
    coinDecimal = round(coinDec * 10)
    floorCoin = coinNum.__floor__()

    if floorCoin > 9:
        newNumCoin = floorCoin / 10
        intNum1, newdecCoin = divmod(newNumCoin, 1)
        newDecimalCoin = round(newdecCoin * 10)
        newfloorNumCoin = newNumCoin.__floor__()
        screen.blit(number[newfloorNumCoin], (location + 35, 15))
        screen.blit(number[newDecimalCoin], (location + 57, 15))
        screen.blit(number[coinDecimal], (location + 79, 15))

    elif floorCoin > 0:
        screen.blit(number[floorCoin], (location + 35, 15))
        screen.blit(number[coinDecimal], (location + 57, 15))

    else:
        screen.blit(number[gameCoins], (location + 35, 15))


def main():
    global waterCounter, switchWater, letter, justClickedD, justClickedU, selection, mainScreen, shopVar, lockerVar, \
        gameStart, controlVar, skullCounter, switchSkull, justDeadClickedReturn, deadReturnCounter
    if justDeadClickedReturn:
        deadReturnCounter += 1

    if deadReturnCounter == 100:
        justDeadClickedReturn = False
        deadReturnCounter = 0

    screen.blit(sky, (0, 0))
    screen.blit(island, (0, 200))
    screen.blit(waterB, (0, 550))

    if waterCounter >= 12:
        switchWater += 1
        waterCounter = 0
    if switchWater > 3:
        switchWater = 0
    for g in range(0, 4):
        screen.blit(waterTop[switchWater], (waterX[g], 500))

    waterCounter += 1

    for i in range(0, 3):
        newNav[i] = pygame.transform.scale(nav[i], (80, 100))

    for l in range(0, 4):
        screen.blit(newNav[0], (170, tabY[l]))
        screen.blit(newNav[1], (250, tabY[l]))
        screen.blit(newNav[1], (330, tabY[l]))
        screen.blit(newNav[1], (410, tabY[l]))
        screen.blit(newNav[1], (490, tabY[l]))
        screen.blit(newNav[2], (570, tabY[l]))

    for k in range(0, len(titleletterlist)):
        titleLetterImg[k] = pygame.transform.scale(letter[titleletterlist[k]], (100, 111))

    for y in range(0, len(titleX)):
        screen.blit(titleLetterImg[y], (titleX[y], 20))

    for c in range(0, len(tabLetters)):
        for d in range(0, len(tabLetters[c])):
            tabLettersImg[c][d] = pygame.transform.scale(letter[tabLetters[c][d]], (40, 40))

    screen.blit(tabLettersImg[0][0], (275, tabY[0]+22))
    screen.blit(tabLettersImg[0][1], (330, tabY[0]+22))
    screen.blit(tabLettersImg[0][2], (385, tabY[0]+22))
    screen.blit(tabLettersImg[0][3], (440, tabY[0]+22))
    screen.blit(tabLettersImg[0][4], (495, tabY[0]+22))

    screen.blit(tabLettersImg[1][0], (248, tabY[1] + 22))
    screen.blit(tabLettersImg[1][1], (303, tabY[1] + 22))
    screen.blit(tabLettersImg[1][2], (358, tabY[1] + 22))
    screen.blit(tabLettersImg[1][3], (413, tabY[1] + 22))
    screen.blit(tabLettersImg[1][4], (468, tabY[1] + 22))
    screen.blit(tabLettersImg[1][5], (523, tabY[1] + 22))

    screen.blit(tabLettersImg[2][0], (303, tabY[2] + 22))
    screen.blit(tabLettersImg[2][1], (358, tabY[2] + 22))
    screen.blit(tabLettersImg[2][2], (413, tabY[2] + 22))
    screen.blit(tabLettersImg[2][3], (468, tabY[2] + 22))

    screen.blit(tabLettersImg[3][0], (200, tabY[3] + 22))
    screen.blit(tabLettersImg[3][1], (255, tabY[3] + 22))
    screen.blit(tabLettersImg[3][2], (310, tabY[3] + 22))
    screen.blit(tabLettersImg[3][3], (365, tabY[3] + 22))
    screen.blit(tabLettersImg[3][4], (420, tabY[3] + 22))
    screen.blit(tabLettersImg[3][5], (475, tabY[3] + 22))
    screen.blit(tabLettersImg[3][6], (530, tabY[3] + 22))
    screen.blit(tabLettersImg[3][7], (585, tabY[3] + 22))

    if key[pygame.K_DOWN]:
        if not justClickedD:
            justClickedD = True
            if selection < 3:
                selection += 1
    else:
        justClickedD = False

    if key[pygame.K_UP]:
        if not justClickedU:
            justClickedU = True
            if selection > 0:
                selection -= 1
    else:
        justClickedU = False

    if not justDeadClickedReturn:
        if key[pygame.K_SPACE] or key[pygame.K_RETURN]:
            mainScreen = False
            if selection == 0:
                gameStart = True
            elif selection == 1:
                lockerVar = True
            elif selection == 2:
                shopVar = True
            elif selection == 3:
                controlVar = True

    if skullCounter >= 9:
        switchSkull += 1
        skullCounter = 0
    if switchSkull > 7:
        switchSkull = 0
    for g in range(0, 2):
        screen.blit(skull[switchSkull], (skullX[g], tabY[selection]))

    skullCounter += 1


def coins():
    global addCoins, coinCount, switchCoin, gameCoins
    if addCoins in [0, 1, 2]:
        for k in range(0, coinCounter):
            coinX.append(random.randint(boatX[addCoins], boatX[addCoins] + 220))
        addCoins = 3
    if len(coinX) > 0:
        for j in range(0, len(coinX)):
            screen.blit(coin[switchCoin], (coinX[j], 400))
            coinX[j] += windSpeed

    if coinCount >= 10:
        switchCoin += 1
        coinCount = 0
    if switchCoin > 3:
        switchCoin = 0

    coinCount += 1

    leftPirateX = pirateX + 44
    botPirateY = pirateY + 60
    rightPirateX = pirateX + 84
    # if len(coinX) > 0:
    #     circle(screen, BLACK, (coinX[0]+10, 410), 5, 0)
    #     circle(screen, BLACK, (coinX[0]+54, 410), 5, 0)
    #     circle(screen, BLACK, (coinX[0]+10, 454), 5, 0)

    deleteCoin = []

    for k in range(0, len(coinX)):
        if coinX[k] + 10 < leftPirateX < coinX[k] + 54 or coinX[k] + 10 < rightPirateX < coinX[k] + 54:
            if 410 < botPirateY < 454:
                deleteCoin.append(coinX.index(coinX[k]))
    if len(deleteCoin) > 0:
        for i in range(0, len(deleteCoin)):
            del coinX[deleteCoin[i]]
            gameCoins += 1
            coinSound.play()
            break


def resetGame():
    global timeCounter, power, lengthColour, gameCoins, coinCount, switchCoin, addCoins, coinCounter, skullCounter, \
        switchSkull, shopVar, gameStart, lockerVar, controlVar, selection, addSpikes, spikeTimer, spikeCounter, \
        haveSpikes, spawnCounter, speedBird, windSpeed, timeSwitch, dead, onBoat, boatDirection, windCounter, \
        switchWind, amtBird, timer, score, birdCounter, switchBird, waterCounter, switchWater, switchBoat, justThrown, \
        pirateY, pirateX, boatCounter, counter, direction, switch, justJumped, jumpSequence, fallSequence, jump, run, \
        idle, boatX, birdX, birdY, rotateBird, spikeX
    addAccount()
    readAccount()
    spikeX = []
    timeCounter = 0
    power = False
    lengthColour = 0
    gameCoins = 0
    coinCount = 0
    switchCoin = 0
    addCoins = 3
    coinCounter = 1
    skullCounter = 0
    switchSkull = 0
    shopVar = False
    gameStart = True
    lockerVar = False
    controlVar = False
    selection = 0
    addSpikes = 3
    spikeTimer = 0
    spikeCounter = 0
    haveSpikes = False
    spawnCounter = 120
    speedBird = 1
    timeSwitch = 0
    dead = False
    onBoat = True
    boatDirection = 0
    windSpeed = 1
    windCounter = 0
    switchWind = 0
    amtBird = 0
    timer = 0
    score = 0
    birdCounter = 0
    switchBird = 0
    waterCounter = 0
    switchWater = 0
    switchBoat = 0
    boatCounter = 0
    justThrown = False
    pirateX = 400
    pirateY = 410
    counter = 0
    direction = 0
    switch = 0
    justJumped = False
    jumpSequence = False
    fallSequence = False
    jump = False
    run = False
    idle = True
    boatX = [0, 350, 700]
    birdX = []
    birdY = []
    rotateBird = []



def powerUp():
    global power, speedBird, windSpeed, timeCounter, lengthColour, oldWindSpeed, oldSpeedBird, justClickedX
    if key[pygame.K_x]:
        if not justClickedX:
            justClickedX = True
            if lengthColour >= 160:
                power = True
                oldSpeedBird = speedBird
                oldWindSpeed = windSpeed
    else:
        justClickedX = False

    if power:
        speedBird = 1
        windSpeed = 0
        if timeCounter > 30:
            lengthColour -= 16
            timeCounter = 0
        if lengthColour <= 0:
            speedBird = oldSpeedBird
            windSpeed = oldWindSpeed
            power = False
        timeCounter += 1


def shop():
    global mainScreen, shopVar, letter, idleCounter, pirateIdleSwitch, crabIdleSwitch, sharkStarIdleSwitch, \
        keysCounter, keysSwitch, justClickedU, justClickedD, justClickedR, justClickedL, locationKey, deadReturnCounter, \
        justDeadClickedReturn, skins, coinAmt

    if key[pygame.K_ESCAPE]:
        shopVar = False
        mainScreen = True

    screen.blit(sky, (0, 0))

    screen.blit(board[0][0], (25, 0))
    screen.blit(board[0][1], (125, 0))
    screen.blit(board[0][2], (225, 0))

    screen.blit(board[1][0], (25, 100))
    screen.blit(board[1][1], (125, 100))
    screen.blit(board[1][2], (225, 100))

    screen.blit(board[2][0], (25, 200))
    screen.blit(board[2][1], (125, 200))
    screen.blit(board[2][2], (225, 200))

    screen.blit(board[0][0], (25, 300))
    screen.blit(board[0][1], (125, 300))
    screen.blit(board[0][2], (225, 300))

    screen.blit(board[1][0], (25, 400))
    screen.blit(board[1][1], (125, 400))
    screen.blit(board[1][2], (225, 400))

    screen.blit(board[2][0], (25, 500))
    screen.blit(board[2][1], (125, 500))
    screen.blit(board[2][2], (225, 500))

    screen.blit(board[0][0], (350, 0))
    screen.blit(board[0][1], (450, 0))
    screen.blit(board[0][2], (550, 0))

    screen.blit(board[1][0], (350, 100))
    screen.blit(board[1][1], (450, 100))
    screen.blit(board[1][2], (550, 100))

    screen.blit(board[2][0], (350, 200))
    screen.blit(board[2][1], (450, 200))
    screen.blit(board[2][2], (550, 200))

    screen.blit(board[0][0], (350, 300))
    screen.blit(board[0][1], (450, 300))
    screen.blit(board[0][2], (550, 300))

    screen.blit(board[1][0], (350, 400))
    screen.blit(board[1][1], (450, 400))
    screen.blit(board[1][2], (550, 400))

    screen.blit(board[2][0], (350, 500))
    screen.blit(board[2][1], (450, 500))
    screen.blit(board[2][2], (550, 500))

    screen.blit(shopPirateIdleR[pirateIdleSwitch], (47, 115))
    screen.blit(shopSharkIdleR[sharkStarIdleSwitch], (382, 90))
    screen.blit(shopStarIdleR[sharkStarIdleSwitch], (57, 390))
    screen.blit(shopCrabIdleR[crabIdleSwitch], (382, 390))


    screen.blit(deadNum[1], (440, 45))
    screen.blit(deadNum[0], (500, 45))
    screen.blit(deadNum[0], (560, 45))

    screen.blit(deadNum[2], (115, 345))
    screen.blit(deadNum[5], (175, 345))
    screen.blit(deadNum[0], (235, 345))

    screen.blit(deadNum[5], (440, 345))
    screen.blit(deadNum[0], (500, 345))
    screen.blit(deadNum[0], (560, 345))

    screen.blit(upTab[0], (650, tabY[0] - 120))
    screen.blit(upTab[1], (650, tabY[1] - 120))
    screen.blit(upTab[1], (650, tabY[2] - 120))
    screen.blit(upTab[1], (650, tabY[3] - 120))
    screen.blit(upTab[2], (650, tabY[3] - 10))

    screen.blit(titleEnd[2], (700, 70))
    screen.blit(titleEnd[14], (700, 125))
    screen.blit(titleEnd[8], (700, 180))
    screen.blit(titleEnd[13], (700, 235))
    screen.blit(titleEnd[18], (700, 290))

    # coinAmt = 679
    coinNum = coinAmt / 10
    intCoin, coinDec = divmod(coinNum, 1)
    coinDecimal = round(coinDec * 10)
    floorCoin = coinNum.__floor__()

    if floorCoin > 9:
        newNumCoin = floorCoin / 10
        intNum1, newdecCoin = divmod(newNumCoin, 1)
        newDecimalCoin = round(newdecCoin * 10)
        newfloorNumCoin = newNumCoin.__floor__()
        screen.blit(deadNum[newfloorNumCoin], (700, 365))
        screen.blit(deadNum[newDecimalCoin], (700, 420))
        screen.blit(deadNum[coinDecimal], (700, 475))

    elif floorCoin > 0:
        screen.blit(deadNum[floorCoin], (700, 365))
        screen.blit(deadNum[coinDecimal], (700, 420))

    else:
        screen.blit(deadNum[coinDecimal], (700, 365))

    if key[pygame.K_DOWN]:
        if not justClickedD:
            justClickedD = True
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationKey[i][o] == 1:
                        if i == 0:
                            locationKey[i + 1][o] = 1
                            locationKey[i][o] = 0
    else:
        justClickedD = False

    if key[pygame.K_UP]:
        if not justClickedU:
            justClickedU = True
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationKey[i][o] == 1:
                        if i == 1:
                            locationKey[i - 1][o] = 1
                            locationKey[i][o] = 0
    else:
        justClickedU = False

    if key[pygame.K_RIGHT]:
        if not justClickedR:
            justClickedR = True
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationKey[i][o] == 1:
                        if o == 0:
                            locationKey[i][o+1] = 1
                            locationKey[i][o] = 0
                            break
    else:
        justClickedR = False

    if key[pygame.K_LEFT]:
        if not justClickedL:
            justClickedL = True
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationKey[i][o] == 1:
                        if o == 1:
                            locationKey[i][o - 1] = 1
                            locationKey[i][o] = 0
    else:
        justClickedL = False

    if justDeadClickedReturn:
        deadReturnCounter += 1

    if deadReturnCounter == 100:
        justDeadClickedReturn = False
        deadReturnCounter = 0

    if not justDeadClickedReturn:
        if key[pygame.K_RETURN] or key[pygame.K_SPACE]:
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationKey[i][o] == 1:
                        if i == 0 and o == 1:
                            if not skins[1] and coinAmt >= 100:
                                skins[1] = True
                                coinAmt -= 100
                                addAccount()
                                readAccount()
                        if i == 1 and o == 0:
                            if not skins[2] and coinAmt >= 250:
                                skins[2] = True
                                coinAmt -= 250
                                addAccount()
                                readAccount()
                        if i == 1 and o == 1:
                            if not skins[3] and coinAmt >= 500:
                                skins[3] = True
                                coinAmt -= 500
                                addAccount()
                                readAccount()

    for u in range(0, 2):
        for t in range(0, 2):
            if locationKey[u][t] == 1:
                if u == 0:
                    if t == 0:
                        screen.blit(keys[keysSwitch], (55, 210))
                    else:
                        screen.blit(keys[keysSwitch], (380, 210))
                else:
                    if t == 0:
                        screen.blit(keys[keysSwitch], (55, 510))
                    else:
                        screen.blit(keys[keysSwitch], (380, 510))

    if idleCounter > 6:
        idleCounter = 0
        pirateIdleSwitch += 1
        crabIdleSwitch += 1
        sharkStarIdleSwitch += 1

    for i in range(1, 4):
        if not skins[i]:
            screen.blit(imgLock, (lockLocation[i-1][0], lockLocation[i-1][1]))
        else:
            screen.blit(imgUnlock, (lockLocation[i-1][0], lockLocation[i-1][1]))

    if keysCounter > 8:
        keysSwitch += 1
        keysCounter = 0

    if keysSwitch > len(keys) - 1:
        keysSwitch = 0


    if pirateIdleSwitch > len(shopPirateIdleR) - 1:
        pirateIdleSwitch = 0

    if sharkStarIdleSwitch > len(shopSharkIdleR) - 1:
        sharkStarIdleSwitch = 0

    if crabIdleSwitch > len(shopCrabIdleR) - 1:
        crabIdleSwitch = 0

    idleCounter += 1
    keysCounter += 1



def locker():
    global mainScreen, lockerVar, letter, idleCounter, crabIdleSwitch, sharkStarIdleSwitch, pirateIdleSwitch, \
        swordSwitch, justClickedD, justClickedR, justClickedU, justClickedL, justDeadClickedReturn, deadReturnCounter, \
        anchorDrawLocation, idleR, idleL, runL, runR

    if key[pygame.K_ESCAPE]:
        lockerVar = False
        mainScreen = True

    screen.blit(sky, (0, 0))

    screen.blit(board[0][0], (50, 0))
    screen.blit(board[0][1], (150, 0))
    screen.blit(board[0][2], (250, 0))

    screen.blit(board[1][0], (50, 100))
    screen.blit(board[1][1], (150, 100))
    screen.blit(board[1][2], (250, 100))

    screen.blit(board[2][0], (50, 200))
    screen.blit(board[2][1], (150, 200))
    screen.blit(board[2][2], (250, 200))

    screen.blit(board[0][0], (50, 300))
    screen.blit(board[0][1], (150, 300))
    screen.blit(board[0][2], (250, 300))

    screen.blit(board[1][0], (50, 400))
    screen.blit(board[1][1], (150, 400))
    screen.blit(board[1][2], (250, 400))

    screen.blit(board[2][0], (50, 500))
    screen.blit(board[2][1], (150, 500))
    screen.blit(board[2][2], (250, 500))

    screen.blit(board[0][0], (450, 0))
    screen.blit(board[0][1], (550, 0))
    screen.blit(board[0][2], (650, 0))

    screen.blit(board[1][0], (450, 100))
    screen.blit(board[1][1], (550, 100))
    screen.blit(board[1][2], (650, 100))

    screen.blit(board[2][0], (450, 200))
    screen.blit(board[2][1], (550, 200))
    screen.blit(board[2][2], (650, 200))

    screen.blit(board[0][0], (450, 300))
    screen.blit(board[0][1], (550, 300))
    screen.blit(board[0][2], (650, 300))

    screen.blit(board[1][0], (450, 400))
    screen.blit(board[1][1], (550, 400))
    screen.blit(board[1][2], (650, 400))

    screen.blit(board[2][0], (450, 500))
    screen.blit(board[2][1], (550, 500))
    screen.blit(board[2][2], (650, 500))

    if not skins[1]:
        screen.blit(imgQuestionMark, (530, 60))
    else:
        screen.blit(shopSharkIdleR[sharkStarIdleSwitch], (482, 90))

    if not skins[2]:
        screen.blit(imgQuestionMark, (130, 360))
    else:
        screen.blit(shopStarIdleR[sharkStarIdleSwitch], (82, 390))

    if not skins[3]:
        screen.blit(imgQuestionMark, (530, 360))
    else:
        screen.blit(shopCrabIdleR[crabIdleSwitch], (482, 390))

    screen.blit(shopPirateIdleR[pirateIdleSwitch], (72, 115))

    if anchorDrawLocation == 0:
        screen.blit(imgAnchor, (anchorLocation[0][0], anchorLocation[0][1]))
    elif anchorDrawLocation == 1:
        screen.blit(imgAnchor, (anchorLocation[1][0], anchorLocation[1][1]))
    elif anchorDrawLocation == 2:
        screen.blit(imgAnchor, (anchorLocation[2][0], anchorLocation[2][1]))
    elif anchorDrawLocation == 3:
        screen.blit(imgAnchor, (anchorLocation[3][0], anchorLocation[3][1]))





    if key[pygame.K_DOWN]:
        if not justClickedD:
            justClickedD = True
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationAnchor[i][o] == 1:
                        if i == 0:
                            locationAnchor[i + 1][o] = 1
                            locationAnchor[i][o] = 0
    else:
        justClickedD = False

    if key[pygame.K_UP]:
        if not justClickedU:
            justClickedU = True
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationAnchor[i][o] == 1:
                        if i == 1:
                            locationAnchor[i - 1][o] = 1
                            locationAnchor[i][o] = 0
    else:
        justClickedU = False

    if key[pygame.K_RIGHT]:
        if not justClickedR:
            justClickedR = True
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationAnchor[i][o] == 1:
                        if o == 0:
                            locationAnchor[i][o+1] = 1
                            locationAnchor[i][o] = 0
    else:
        justClickedR = False

    if key[pygame.K_LEFT]:
        if not justClickedL:
            justClickedL = True
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationAnchor[i][o] == 1:
                        if o == 1:
                            locationAnchor[i][o - 1] = 1
                            locationAnchor[i][o] = 0
    else:
        justClickedL = False

    for u in range(0, 2):
        for t in range(0, 2):
            if locationAnchor[u][t] == 1:
                if u == 0:
                    if t == 0:
                        screen.blit(sword[swordSwitch], (anchorLocation[0][0] - 10, anchorLocation[0][1] + 165))
                    else:
                        screen.blit(sword[swordSwitch], (anchorLocation[1][0] - 10, anchorLocation[1][1] + 165))
                else:
                    if t == 0:
                        screen.blit(sword[swordSwitch], (anchorLocation[2][0] - 10, anchorLocation[2][1] + 165))
                    else:
                        screen.blit(sword[swordSwitch], (anchorLocation[3][0] - 10, anchorLocation[3][1] + 165))

    if justDeadClickedReturn:
        deadReturnCounter += 1

    if deadReturnCounter == 100:
        justDeadClickedReturn = False
        deadReturnCounter = 0

    if not justDeadClickedReturn:
        if key[pygame.K_RETURN] or key[pygame.K_SPACE]:
            for i in range(0, 2):
                for o in range(0, 2):
                    if locationAnchor[i][o] == 1:
                        if i == 0 and o == 0:
                            anchorDrawLocation = 0
                            idleR = pirateIdleR
                            idleL = pirateIdleL
                            runR = pirateRunR
                            runL = pirateRunL
                        if i == 0 and o == 1:
                            if skins[1]:
                                anchorDrawLocation = 1
                                idleR = sharkIdleR
                                idleL = sharkIdleL
                                runR = sharkRunR
                                runL = sharkRunL
                        if i == 1 and o == 0:
                            if skins[2]:
                                anchorDrawLocation = 2
                                idleR = starIdleR
                                idleL = starIdleL
                                runR = starRunR
                                runL = starRunL
                        if i == 1 and o == 1:
                            if skins[3]:
                                anchorDrawLocation = 3
                                idleR = crabIdleR
                                idleL = crabIdleL
                                runR = crabRunR
                                runL = crabRunL


    if idleCounter > 6:
        idleCounter = 0
        pirateIdleSwitch += 1
        crabIdleSwitch += 1
        sharkStarIdleSwitch += 1
        swordSwitch += 1

    if swordSwitch > len(sword) - 1:
        swordSwitch = 0

    if pirateIdleSwitch > len(shopPirateIdleR) - 1:
        pirateIdleSwitch = 0

    if sharkStarIdleSwitch > len(shopSharkIdleR) - 1:
        sharkStarIdleSwitch = 0

    if crabIdleSwitch > len(shopCrabIdleR) - 1:
        crabIdleSwitch = 0

    idleCounter += 1


def controls():
    global mainScreen, controlVar, letter

    if key[pygame.K_ESCAPE]:
        controlVar = False
        mainScreen = True

    screen.blit(sky, (0, 0))

    screen.blit(board[0][0], (0, 0))
    screen.blit(board[0][1], (100, 0))
    screen.blit(board[0][1], (200, 0))
    screen.blit(board[0][1], (300, 0))
    screen.blit(board[0][1], (400, 0))
    screen.blit(board[0][1], (500, 0))
    screen.blit(board[0][1], (600, 0))
    screen.blit(board[0][2], (700, 0))

    screen.blit(board[1][0], (0, 100))
    screen.blit(board[1][0], (0, 200))
    screen.blit(board[1][0], (0, 300))
    screen.blit(board[1][0], (0, 400))
    screen.blit(board[1][2], (700, 100))
    screen.blit(board[1][2], (700, 200))
    screen.blit(board[1][2], (700, 300))
    screen.blit(board[1][2], (700, 400))

    screen.blit(board[2][0], (0, 500))
    screen.blit(board[2][1], (100, 500))
    screen.blit(board[2][1], (200, 500))
    screen.blit(board[2][1], (300, 500))
    screen.blit(board[2][1], (400, 500))
    screen.blit(board[2][1], (500, 500))
    screen.blit(board[2][1], (600, 500))
    screen.blit(board[2][2], (700, 500))

    screen.blit(board[1][1], (100, 100))
    screen.blit(board[1][1], (200, 100))
    screen.blit(board[1][1], (300, 100))
    screen.blit(board[1][1], (400, 100))
    screen.blit(board[1][1], (500, 100))
    screen.blit(board[1][1], (600, 100))

    screen.blit(board[1][1], (100, 200))
    screen.blit(board[1][1], (200, 200))
    screen.blit(board[1][1], (300, 200))
    screen.blit(board[1][1], (400, 200))
    screen.blit(board[1][1], (500, 200))
    screen.blit(board[1][1], (600, 200))

    screen.blit(board[1][1], (100, 300))
    screen.blit(board[1][1], (200, 300))
    screen.blit(board[1][1], (300, 300))
    screen.blit(board[1][1], (400, 300))
    screen.blit(board[1][1], (500, 300))
    screen.blit(board[1][1], (600, 300))

    screen.blit(board[1][1], (100, 400))
    screen.blit(board[1][1], (200, 400))
    screen.blit(board[1][1], (300, 400))
    screen.blit(board[1][1], (400, 400))
    screen.blit(board[1][1], (500, 400))
    screen.blit(board[1][1], (600, 400))

    for i in range(0, len(letter)):
        controlLetters.append(pygame.transform.scale(letter[i], (30, 33)))

    screen.blit(controlLetters[2], (200, 50))
    screen.blit(controlLetters[14], (255, 50))
    screen.blit(controlLetters[13], (310, 50))
    screen.blit(controlLetters[19], (365, 50))
    screen.blit(controlLetters[17], (420, 50))
    screen.blit(controlLetters[14], (475, 50))
    screen.blit(controlLetters[11], (530, 50))
    screen.blit(controlLetters[18], (585, 50))

    screen.blit(controlLetters[2], (50, 110))
    screen.blit(controlLetters[11], (85, 110))
    screen.blit(controlLetters[8], (120, 110))
    screen.blit(controlLetters[2], (155, 110))
    screen.blit(controlLetters[10], (190, 110))

    screen.blit(controlLetters[23], (250, 110))

    screen.blit(controlLetters[5], (310, 110))
    screen.blit(controlLetters[14], (345, 110))
    screen.blit(controlLetters[17], (380, 110))

    screen.blit(controlLetters[15], (440, 110))
    screen.blit(controlLetters[14], (475, 110))
    screen.blit(controlLetters[22], (510, 110))
    screen.blit(controlLetters[4], (545, 110))
    screen.blit(controlLetters[17], (580, 110))

    screen.blit(controlLetters[20], (640, 110))
    screen.blit(controlLetters[15], (675, 110))

    screen.blit(controlLetters[2], (50, 190))
    screen.blit(controlLetters[11], (85, 190))
    screen.blit(controlLetters[8], (120, 190))
    screen.blit(controlLetters[2], (155, 190))
    screen.blit(controlLetters[10], (190, 190))

    screen.blit(controlLetters[18], (260, 190))
    screen.blit(controlLetters[15], (295, 190))
    screen.blit(controlLetters[0], (330, 190))
    screen.blit(controlLetters[2], (365, 190))
    screen.blit(controlLetters[4], (400, 190))

    screen.blit(controlLetters[19], (460, 190))
    screen.blit(controlLetters[14], (495, 190))

    screen.blit(controlLetters[9], (560, 190))
    screen.blit(controlLetters[20], (595, 190))
    screen.blit(controlLetters[12], (630, 190))
    screen.blit(controlLetters[15], (665, 190))

    screen.blit(controlLetters[11], (50, 270))
    screen.blit(controlLetters[4], (85, 270))
    screen.blit(controlLetters[5], (120, 270))
    screen.blit(controlLetters[19], (155, 270))

    screen.blit(controlLetters[2], (205, 270))
    screen.blit(controlLetters[11], (240, 270))
    screen.blit(controlLetters[8], (275, 270))
    screen.blit(controlLetters[2], (310, 270))
    screen.blit(controlLetters[10], (345, 270))

    screen.blit(controlLetters[19], (405, 270))
    screen.blit(controlLetters[14], (440, 270))

    screen.blit(controlLetters[18], (500, 270))
    screen.blit(controlLetters[7], (535, 270))
    screen.blit(controlLetters[14], (570, 270))
    screen.blit(controlLetters[14], (605, 270))
    screen.blit(controlLetters[19], (640, 270))

    screen.blit(controlLetters[2], (50, 350))
    screen.blit(controlLetters[11], (85, 350))
    screen.blit(controlLetters[8], (120, 350))
    screen.blit(controlLetters[2], (155, 350))
    screen.blit(controlLetters[10], (190, 350))

    screen.blit(controlLetters[0], (250, 350))

    screen.blit(controlLetters[19], (310, 350))
    screen.blit(controlLetters[14], (345, 350))

    screen.blit(controlLetters[12], (405, 350))
    screen.blit(controlLetters[14], (440, 350))
    screen.blit(controlLetters[21], (475, 350))
    screen.blit(controlLetters[4], (510, 350))

    screen.blit(controlLetters[11], (570, 350))
    screen.blit(controlLetters[4], (605, 350))
    screen.blit(controlLetters[5], (640, 350))
    screen.blit(controlLetters[19], (675, 350))

    screen.blit(controlLetters[2], (50, 430))
    screen.blit(controlLetters[11], (85, 430))
    screen.blit(controlLetters[8], (120, 430))
    screen.blit(controlLetters[2], (155, 430))
    screen.blit(controlLetters[10], (190, 430))

    screen.blit(controlLetters[3], (250, 430))

    screen.blit(controlLetters[19], (310, 430))
    screen.blit(controlLetters[14], (345, 430))

    screen.blit(controlLetters[12], (405, 430))
    screen.blit(controlLetters[14], (440, 430))
    screen.blit(controlLetters[21], (475, 430))
    screen.blit(controlLetters[4], (510, 430))

    screen.blit(controlLetters[17], (570, 430))
    screen.blit(controlLetters[8], (605, 430))
    screen.blit(controlLetters[6], (640, 430))
    screen.blit(controlLetters[7], (675, 430))
    screen.blit(controlLetters[19], (710, 430))

    screen.blit(controlLetters[2], (50, 510))
    screen.blit(controlLetters[11], (85, 510))
    screen.blit(controlLetters[8], (120, 510))
    screen.blit(controlLetters[2], (155, 510))
    screen.blit(controlLetters[10], (190, 510))

    screen.blit(controlLetters[4], (250, 510))
    screen.blit(controlLetters[18], (285, 510))
    screen.blit(controlLetters[2], (320, 510))

    screen.blit(controlLetters[19], (380, 510))
    screen.blit(controlLetters[14], (415, 510))

    screen.blit(controlLetters[17], (475, 510))
    screen.blit(controlLetters[4], (510, 510))
    screen.blit(controlLetters[19], (545, 510))
    screen.blit(controlLetters[20], (580, 510))
    screen.blit(controlLetters[17], (615, 510))
    screen.blit(controlLetters[13], (650, 510))


def readAccount():
    global coinAmt, skins
    info = []
    file = open('account.txt')
    content = file.readlines()
    file.close()
    for g in range(0, 2):
        string = ""
        for i in range(0, len(content[g])):
            s = content[g]
            if s[i] == "\n":
                info.append(string)
                break
            else:
                string += s[i]
                if i + 1 == len(content[g]):
                    info.append(string)
    coinAmt = int(info[0])
    for i in range(len(info[1])):
        if info[1][i] == "T":
            skins.append(True)
        elif info[1][i] == "F":
            skins.append(False)


def addAccount():
    global coinAmt, skins, gameCoins
    coinAmt += gameCoins
    appendCoins = str(coinAmt)
    skinStr = ""
    for i in range(0, 4):
        if skins[i]:
            skinStr += "T,"
        if not skins[i]:
            skinStr += "F,"
    with open('account.txt', 'w') as f:
        f.writelines(appendCoins)
        f.writelines('\n')
        f.writelines(skinStr)


# your GLOBAL variables go here
justDead = False
idleCounter = 0
pirateIdleSwitch = 0
crabIdleSwitch = 0
sharkStarIdleSwitch = 0
imgLock = pygame.image.load("images/lock.png")
imgLock = pygame.transform.scale(imgLock, (100, 100))
imgUnlock = pygame.image.load("images/unlock.png")
imgUnlock = pygame.transform.scale(imgUnlock, (100, 100))
lockLocation = [[360, 20], [35, 320], [360, 320]]
anchorLocation = [[100, 50], [500, 50], [100, 350], [500, 350]]
skins = []
deadReturnCounter = 0
deadNumX = [360, 430, 500]
timeCounter = 0
endLetters = []
justClickedX = False
power = False
lengthColour = 0
colourBar = pygame.image.load('images/colour.png')
powerBar = []
gameCoins = 0
coin = []
coinX = []
coinCount = 0
switchCoin = 0
addCoins = 3
coinCounter = 1
coinAmt = 0
controlLetters = []
backgroundMusic = pygame.mixer.Sound("sounds/pirateMusic.mp3")
backgroundMusic.play(-1)
coinSound = pygame.mixer.Sound("sounds/coinSound.mp3")
gameOverSound = pygame.mixer.Sound("sounds/gameOverSound.mp3")
board = [[], [], []]
skull = []
skullX = [112, 660]
skullCounter = 0
switchSkull = 0
justClickedD = False
justClickedU = False
justClickedR = False
justClickedL = False
justDeadClickedD = False
justDeadClickedU = False
justDeadClickedR = False
justDeadClickedL = False
justDeadClickedReturn = False
shopVar = False
gameStart = False
lockerVar = False
controlVar = False
selection = 0
anchorDrawLocation = 0
titleLetterImg = [0, 0, 0, 0, 0, 0, 0]
tabLetters = [[18, 19, 0, 17, 19], [11, 14, 2, 10, 4, 17], [18, 7, 14, 15], [2, 14, 13, 19, 17, 14, 11, 18]]
tabLettersImg = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
newNav = [0, 0, 0]
titleX = [37, 142, 247, 352, 457, 562, 667]
titleletterlist = [15, 8, 4, 17, 0, 19, 4]
tabY = [165, 270, 375, 480]
addSpikes = 3
spikeTimer = 0
spikeCounter = 0
spikeX = []
haveSpikes = False
stay = []
spawnCounter = 120
speedBird = 1
timeSwitch = 0
spikes = pygame.image.load('images/Spikes.png')
dead = False
onBoat = True
boatDirection = 0
windSpeed = 1
boatX = [0, 350, 700]
windCounter = 0
switchWind = 0
windR = []
windL = []
shipLocation = []
birdX = []
birdY = []
rotateBird = []
amtBird = 0
timer = 0
score = 0
birdR = []
birdL = []
boatR = []
boatL = []
waterTop = []
birdCounter = 0
switchBird = 0
waterX = [0, 200, 400, 600]
waterCounter = 0
switchWater = 0
switchBoat = 0
boatCounter = 0
imgPie = pygame.image.load('images/pie.tiff')
imgPie = pygame.transform.scale(imgPie, (36, 38))
runX = 0
riseY = 0
pieX = []
pieY = []
pieRun = []
pieRise = []
justThrown = False
pirateX = 400
pirateY = 410
counter = 0
direction = 0
switch = 0
justJumped = False
jumpSequence = False
fallSequence = False
jump = False
run = False
idle = True
idleR = []
idleL = []
runR = []
runL = []
pirateIdleR = []
pirateIdleL = []
pirateRunR = []
pirateRunL = []
sharkIdleR = []
sharkIdleL = []
sharkRunR = []
sharkRunL = []
crabIdleR = []
crabIdleL = []
crabRunR = []
crabRunL = []
starIdleR = []
starIdleL = []
starRunR = []
starRunL = []
shopSharkIdleR = []
shopCrabIdleR = []
shopPirateIdleR = []
shopStarIdleR = []
pie = []
shipR = []
shipL = []
letter = []
number = []
haveWhale = False
whale = []
whaleX = 0
whaleY = 550
whaleCounter = 0
whaleSwap = 0
nav = []
sword = []
mainScreen = True
displayCrab = False
displayShark = False
displayStar = False
numberX = [523, 545, 567]
upTab = []
imgAnchor = pygame.image.load('images/anchor.png')
imgAnchor = pygame.transform.scale(imgAnchor, (38, 36))
player = 0
keys = []
keysCounter = 0
keysSwitch = 0
locationKey = [[1, 0], [0, 0]]
locationAnchor = [[1, 0], [0, 0]]
bDirect = 0
swordSwitch = 0
imgQuestionMark = pygame.image.load("images/QuestionMark.png")
imgQuestionMark = pygame.transform.scale(imgQuestionMark, (150, 180))
createImg()
idleR = pirateIdleR
idleL = pirateIdleL
runR = pirateRunR
runL = pirateRunL
deadNum = []
for q in range(0, len(number)):
    deadNum.append(pygame.transform.scale(number[q], (50, 50)))
titleEnd = []
for j in range(0, len(letter)):
    titleEnd.append(pygame.transform.scale(letter[j], (50, 50)))


readAccount()

# MAIN LOOP
while not done:
    # makes the background the colour WHITE
    screen.fill(WHITE)

    xMouse, yMouse = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    key = pygame.key.get_pressed()
    if mainScreen:
        main()
    elif shopVar:
        shop()
    elif lockerVar:
        locker()
    elif controlVar:
        controls()
    elif gameStart:
        background()
        user()
        throw()
        enemy()
        collision()
        navBar()
        coins()
        powerUp()
        death()

    # this code allows you to close the window and end the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # this line draws everything into the window all at once
    pygame.display.flip()
    # this line limits the frames per second to 60
    clock.tick(60)

pygame.quit()
