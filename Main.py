#!/usr/bin/env python3


# IMPORT
import Game
import Load
import pygame

# DECLARATIONS
# PyGame
WHITE = [255, 255, 255]
size = [1000, 500]

pygame.init()
# Python


# MAIN
# Load
icon = pygame.image.load('Dario_stash_icon.png')
pic = pygame.image.load('Dario_stash.png')
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
pygame.display.set_caption("Super Dario Bros")
pygame.display.set_icon(icon)
pygame.display.flip()

mode = Load.loading_screen(screen, size, pic, mode="normal")


# Program
screen.fill(WHITE)
pygame.display.flip()

if mode == "normal":
    Game.normal_mode(screen, size)
elif mode == "hard":
    Game.hard_mode(screen, size)
else:
    print("This line will never be executed!")
