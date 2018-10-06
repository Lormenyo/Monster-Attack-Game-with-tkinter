""" This is just a guessing game with two players; the computer and the user. The computer automatically hides a bomb
in one of the monsters body using random indexing. The player has 15 seconds to choose which monster has the bomb
and kill it; Else they all blow up.This game can be used by kids in place of rock, paper, scissors. Let the users log in
once on their first try. Log in their attempts in the game. Use the data Science to predict the player."""

import pygame

import random

import time

from tkinter import *
from tkinter import messagebox

tk = Tk()

line_width = 10
width = 900
height = 600

#        R  G  B
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)
gray = (197, 197, 197)
pink = (255, 170, 255)
bright_red = (100, 0, 0)
bright_green = (0, 100, 0)
bright_blue = (0, 0, 100)

colour = [red, blue, green, purple, black, gray, pink]
car_width = 175
car_height = 200

pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Memrace')
clock = pygame.time.Clock()

carImg = pygame.image.load('img/tnk.png')
monsImg = pygame.image.load('img/mon.jpg')
monsImg2 = pygame.image.load('img/he.jpg')
monsImg3 = pygame.image.load('img/ter.jpg')
monsImg4 = pygame.image.load('img/ha.jpg')
introImg = pygame.image.load('img/rar.jpg')
fImg = pygame.image.load('img/fball.png')
brickImg = pygame.image.load('img/brik.jpg')
pauseImg = pygame.image.load('img/bor.jpg')

img_list = [monsImg, monsImg2, monsImg3, monsImg4]
lock = []

HELP = "The various monsters have different numbers; " \
       " guess the monster with the bomb by " \
       "clicking on the respective number on your keyboard. " \
       "If you don't kill the right " \
       "monster , you will get bombed"

pause = False


def index():
    for img, num in enumerate(img_list):
        lock.append((img, num))
    print(lock)


def rotated(xpos, ypos):
    angle = 0
    while True:
        rot_img = pygame.transform.rotate(carImg, angle)
        gameDisplay.blit(rot_img, (xpos, ypos))
        angle += 30



# def countdown():
#     end_time = 20
#     while end_time > 0:
#         m, s = divmod(end_time, 60)
#         h, m = divmod(m, 60)
#         time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
#
#         smallText = pygame.font.SysFont("arial", 30, bold=True)
#         TextSurf, TextRect = text_objects(time_left + "\r", smallText)
#         gameDisplay.blit(TextSurf, (700, 555))
#
#         time.sleep(1)
#         end_time -= 1


def maze():
    M = 19
    N = 13
    block = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1,
             1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
             1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    bx = 0
    by = 0
    for i in range(0, M * N):
        if block[bx + (by * M)] == 1:
            gameDisplay.blit(brickImg, (bx * 44, by * 44))

        bx = bx + 1
        if bx > M - 1:
            bx = 0
            by = by + 1


def objects(x, y):
    gameDisplay.blit(carImg, (x, y))
    gameDisplay.blit(monsImg3, (width-219, height-219))
    gameDisplay.blit(monsImg4, (50, height-219))
    gameDisplay.blit(monsImg2, (50, 50))
    gameDisplay.blit(monsImg, (width-219, 50))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2), (height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display("You crashed")


def game_help():
    tk.wm_withdraw()
    messagebox.showinfo('HELP', HELP)


def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 100)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((width / 2), (height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(pauseImg, (width/2 - 110, height/2 - 300))

        button("Continue",  150, 450, 100, 50,  green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    game_help()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects("Monsqaeda", largeText)
        TextRect.center = ((width / 2), (height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(introImg, ((width / 2) - 65, (height / 2) - 300))

        button("PLAY", 250, 450, 100, 50, green, bright_green, game_loop)
        button("HELP", 400, 450, 100, 50, blue, bright_blue, game_help)
        button("EXIT", 550, 450, 100, 50, red, bright_red, quitgame)

        display_text = pygame.font.SysFont('calibri', 15)
        TSurf, TRect = text_objects("Press P to pause, H for help", display_text)
        TRect.center = ((width / 2), 530)
        gameDisplay.blit(TSurf, TRect)

        pygame.display.update()
        clock.tick(15)


def button(message, x, y, w, h,  inactive, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive, (x, y, w, h))

    smallText = pygame.font.SysFont('arial', 20, bold=True)
    textSurf, textRect = text_objects(message, smallText)
    textRect.center = ((x+(w / 2)),   (y+(h / 2)))
    gameDisplay.blit(textSurf, textRect)


def game_loop():

    global pause

    x = (width*0.45)
    y = (height*0.60)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5

                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
                elif event.key == pygame.K_h:
                    game_help()
                elif event.key == pygame.K_r:
                    global carImg
                    carImg = pygame.transform.rotate(carImg, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)

        # top line
        # pygame.draw.rect(gameDisplay, black, [0, 0, width-50, line_width])
        # bottom line
        # pygame.draw.rect(gameDisplay, black, [0, height-50, width-50, line_width])
        # left line
        # pygame.draw.rect(gameDisplay, black, [0, 0, line_width, height-50])
        # right line
        # pygame.draw.rect(gameDisplay, black, [width-50, 0, line_width, height + line_width-50])

        objects(x, y)
        button("PAUSE", 250, 560, 100, 50, green, bright_green, paused)
        maze()
        # countdown()
        pygame.display.update()
        clock.tick(60)


# index()
game_intro()
game_loop()
pygame.quit()
quit()


