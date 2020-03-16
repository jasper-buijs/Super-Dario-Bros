#!/usr/bin/env python3


# IMPORT
import pygame
from pygame.locals import *
from random import randint

# DECLARATIONS
# PyGame
global bgcolor, bgcolordire, cloudlist, clock
bgcolor = [255, 255, 255]
bgcolordire = [-1, 1, 0]
clock = pygame.time.Clock()
# Python
cloudlist = []


# CLASSES
# Cloud
class Cloud:
    def __init__(self, screen, position, screensize, color, radius, speed):
        self.posx = position[0]
        self.posy = position[1]
        self.pos = position
        self.wind = screen
        self.windsize = screensize
        self.col = color
        self.rad = radius
        self.speed = speed
        self.draw()

    def move(self, color):
        self.col = color
        if self.posx > self.speed:
            self.posx -= self.speed
            self.pos[0] = self.posx
        else:
            self.posx = self.windsize[0]
            self.pos[0] = self.posx
            self.posy = randint(0, self.windsize[1])
            self.pos[1] = self.posy

    def draw(self):
        pygame.draw.circle(self.wind, self.col, self.pos, self.rad)


# MAIN
# normal mode
def normal_mode(screen, size):
    print("launching normal mode", screen)
    for i in range(20):
        cloud = Cloud(screen, [randint(0, size[0]), randint(0, size[1])], size, [0, 0, 0], 10, 2)
        cloudlist.append(cloud)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        print(bgcolor)
        screen.fill(bgcolor)
        for i in range(3):
            if bgcolordire[i] == -1:
                if bgcolor[i] != 0:
                    bgcolor[i] -= 1
                else:
                    bgcolordire[i] = 0
                    if i != 2:
                        bgcolordire[i + 1] = -1
                    else:
                        bgcolordire[0] = -1
                    if i == 0:
                        bgcolordire[2] = 1
                    elif i == 1:
                        bgcolordire[0] = 1
                    else:
                        bgcolordire[1] = 1
            elif bgcolordire[i] == 1:
                if bgcolor[i] != 255:
                    bgcolor[i] += 1
        for cloud in cloudlist:
            cloud.move([255, 255, 255])
            cloud.draw()
        pygame.display.flip()
        clock.tick(60)


# hard mode
def hard_mode(screen, size):
    print("size:\t", size)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        global bgcolor
        print(bgcolor)
        screen.fill(bgcolor)
        pygame.display.flip()
        bgcolor = [randint(0, 255), randint(0, 255), randint(0, 255)]
