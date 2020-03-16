#!/usr/bin/env python3


# IMPORT
import pygame
import os
from pygame.locals import *
from time import sleep
from random import randint

pygame.init()
pygame.font.init()

# DECLARATIONS
# PyGame
global nob, balllist
# Python
balllist = []
nob = 50
fontsize = 100
font1 = pygame.font.SysFont("Bauhaus 93", fontsize)


# CLASSES
# Ball
class Ball:
    def __init__(self, screen, x, y, fillcolor, radius, speed, xdir, ydir):
        self.posx = x
        self.posy = y
        self.pos = [x, y]
        self.col = fillcolor
        self.rad = radius
        self.wind = screen
        self.speed = speed
        self.dirx = xdir
        self.diry = ydir
        self.draw()

    def move(self, fillcolor):
        self.col = fillcolor
        if self.dirx == "+":
            self.posx += self.speed
        elif self.dirx == "-":
            self.posx -= self.speed
        elif self.dirx != "0":
            print("Error with moving x-co. x-co = {}".format(self.dirx))
        if self.diry == "+":
            self.posy += self.speed
        elif self.diry == "-":
            self.posy -= self.speed
        elif self.diry != "0":
            print("Error with moving y-co. y-co = {}".format(self.diry))
        while self.posx < self.rad:
            self.posx += 1
            self.dirx = "+"
        while self.posy < self.rad:
            self.posy += 1
            self.diry = "+"
        while self.posy > (500 - self.rad):
            self.posy -= 1
            self.diry = "-"
        while self.posx > (1000 - self.rad):
            self.posx -= 1
            self.diry = "+"
        self.pos = [self.posx, self.posy]
        self.draw()

    def draw(self):
        pygame.draw.circle(self.wind, self.col, self.pos, self.rad)
        if len(balllist) != nob:
            pygame.draw.circle(self.wind, self.col, [int(1000 - self.rad), int(500 - self.rad)], self.rad)


# MAIN
# Loading screen
def loading_screen(screen, size, icon, mode):
    signs = ("+", "-")
    for i in range(nob):
        ball = Ball(screen, randint(0, 1000), randint(0, 500), [255, 255, 255],
                    20, 5, signs[randint(0, 1)], signs[randint(0, 1)])
        balllist.append(ball)
        sleep(0.005)
    screen.fill([255, 255, 255])
    clock = pygame.time.Clock()
    pygame.display.flip()
    while balllist:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
        colorbg = [randint(0, 255), randint(0, 255), randint(0, 255)]
        colorball = []
        for i in range(3):
            colorball.append(255 - colorbg[i])
        screen.fill(colorbg)
        for baall in balllist:
            if mode == "hard":
                baall.move(colorball)
            else:
                baall.move([255, 255, 255])
            if baall.pos == [int(1000 - baall.rad), int(500 - baall.rad)]:
                balllist.remove(baall)
        clock.tick(60)
        pygame.display.flip()
    pygame.draw.polygon(screen, colorbg, [(int(1000 - (0.5 * baall.rad)), int(500 - baall.rad)),
                                          (int(1000 - (1.5 * baall.rad)), int(500 - (0.5 * baall.rad))),
                                          (int(1000 - (1.5 * baall.rad)), int(500 - (1.5 * baall.rad)))])
    tekst = font1.render("Super Dario Bros", True, baall.col)
    iconrender = screen.blit(icon, (int(size[0] / 2) - int(icon.get_rect().width / 2), (int(size[1] / 3) - int(icon.get_rect().height / 2))))
    screen.blit(tekst, ((int(size[0] / 2) - int(tekst.get_rect().width / 2), (int(size[1] / 2) - int(tekst.get_rect().height / 2)))))
    pygame.display.flip()
    button_to_presss = True
    while button_to_presss:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
            if event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if (((position[0] < int(1000 - (0.5 * baall.rad))) and (
                        position[0] > int(1000 - (1.5 * baall.rad)))) and (
                        (position[1] > int(500 - (1.5 * baall.rad))) and (position[1] < int(500 - (0.5 * baall.rad))))):
                    button_to_presss = False
    button_to_presss = "none"
    while button_to_presss == "none":
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
            if event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if (position[0] < int((size[0] / 2) + 200) and (position[0] > int((size[0] / 2) - 200))) and (
                        (position[1] > int((size[1] / 2) - 60)) and (position[1] < int((size[1] / 2) - 10))):
                    button_to_presss = "normal"
                elif (position[0] < int((size[0] / 2) + 200) and (position[0] > int((size[0] / 2) - 200))) and (
                        (position[1] > int((size[1] / 2) + 10)) and (position[1] < int((size[1] / 2) + 60))):
                    button_to_presss = "hard"
                return button_to_presss
        screen.fill(colorbg)
        fillcolor = [randint(0, 255), randint(0, 255), randint(0, 255)]
        negcolor = []
        for rgbvalue in fillcolor:
            negcolor.append(255 - rgbvalue)
        screen.fill(fillcolor)
        pygame.draw.rect(screen, baall.col, [(int((size[0] / 2) - 200), int((size[1] / 2) - 60)),
                                             (int(400), int(50))])
        pygame.draw.rect(screen, negcolor, [(int((size[0] / 2) - 200), int((size[1] / 2) + 10)),
                                            (int(400), int(50))])
        pygame.display.flip()
