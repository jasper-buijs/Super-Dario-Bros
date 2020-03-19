#!/usr/bin/env python3


# IMPORT
import pygame
from pygame.locals import *
from time import sleep
from random import randint

pygame.init()
pygame.font.init()

# DECLARATIONS
# PyGame
bg_color = []
# Python
ball_list = []
possible_directions = ("+", "-")
number_of_balls = 50
main_font = pygame.font.SysFont("Bauhaus 93", 100)


# CLASSES
# Ball
class Ball:
    def __init__(self, screen, x, y, ball_color, radius, speed, x_direction, y_direction):
        self.x_pos = x
        self.y_pos = y
        self.pos = [x, y]
        self.col = ball_color
        self.rad = radius
        self.win = screen
        self.v = speed
        self.x_dir = x_direction
        self.y_dir = y_direction
        self.draw()

    def move(self, ball_color):
        self.col = ball_color
        if self.x_dir == "+":
            self.x_pos += self.v
        elif self.x_dir == "-":
            self.x_pos -= self.v
        elif self.x_dir != "0":
            print("Error with moving x-co. x-co = {}".format(self.x_dir))
        if self.y_dir == "+":
            self.y_pos += self.v
        elif self.y_dir == "-":
            self.y_pos -= self.v
        elif self.y_dir != "0":
            print("Error with moving y-co. y-co = {}".format(self.y_dir))
        while self.x_pos < self.rad:
            self.x_pos += 1
            self.x_dir = "+"
        while self.y_pos < self.rad:
            self.y_pos += 1
            self.y_dir = "+"
        while self.y_pos > (500 - self.rad):
            self.y_pos -= 1
            self.y_dir = "-"
        while self.x_pos > (1000 - self.rad):
            self.x_pos -= 1
            self.y_dir = "+"
        self.pos = [self.x_pos, self.y_pos]
        self.draw()

    def draw(self):
        pygame.draw.circle(self.win, self.col, self.pos, self.rad)
        if len(ball_list) != number_of_balls:
            pygame.draw.circle(self.win, self.col, [int(1000 - self.rad), int(500 - self.rad)], self.rad)


# MAIN
# Loading screen
def loading_screen(screen, size, icon, mode):
    global number_of_balls, ball_list, bg_color, possible_directions
    for i in range(number_of_balls):
        ball = Ball(screen, randint(0, 1000), randint(0, 500), [255, 255, 255],
                    20, 5, possible_directions[randint(0, 1)], possible_directions[randint(0, 1)])
        ball_list.append(ball)
        sleep(0.005)
    screen.fill([255, 255, 255])
    clock = pygame.time.Clock()
    pygame.display.flip()
    while ball_list:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        bg_color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        colorball = []
        for i in range(3):
            colorball.append(255 - bg_color[i])
        screen.fill(bg_color)
        for ball in ball_list:
            if mode == "hard":
                ball.move(colorball)
            else:
                ball.move([255, 255, 255])
            if ball.pos == [int(1000 - ball.rad), int(500 - ball.rad)]:
                ball_list.remove(ball)
        clock.tick(60)
        pygame.display.flip()
    pygame.draw.polygon(screen, bg_color, [(int(1000 - (0.5 * ball.rad)), int(500 - ball.rad)),
                                           (int(1000 - (1.5 * ball.rad)), int(500 - (0.5 * ball.rad))),
                                           (int(1000 - (1.5 * ball.rad)), int(500 - (1.5 * ball.rad)))])
    text = main_font.render("Super Dario Bros", True, ball.col)
    screen.blit(icon, (int(size[0] / 2) - int(icon.get_rect().width / 2),
                       (int(size[1] / 3) - int(icon.get_rect().height / 2))))
    screen.blit(text, ((int(size[0] / 2) - int(text.get_rect().width / 2),
                        (int(size[1] / 2) - int(text.get_rect().height / 2)))))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if (((position[0] < int(1000 - (0.5 * ball.rad))) and (
                        position[0] > int(1000 - (1.5 * ball.rad)))) and (
                        (position[1] > int(500 - (1.5 * ball.rad))) and (position[1] < int(500 - (0.5 * ball.rad))))):
                    break
        else:
            continue
        break
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if (position[0] < int((size[0] / 2) + 200) and (position[0] > int((size[0] / 2) - 200))) and (
                        (position[1] > int((size[1] / 2) - 60)) and (position[1] < int((size[1] / 2) - 10))):
                    return "normal"
                elif (position[0] < int((size[0] / 2) + 200) and (position[0] > int((size[0] / 2) - 200))) and (
                        (position[1] > int((size[1] / 2) + 10)) and (position[1] < int((size[1] / 2) + 60))):
                    return "hard"
        screen.fill(bg_color)
        screen_color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        ball_color = []
        for rgb_value in screen_color:
            ball_color.append(255 - rgb_value)
        screen.fill(screen_color)
        pygame.draw.rect(screen, ball.col, [(int((size[0] / 2) - 200),
                                             int((size[1] / 2) - 60)),
                                            (int(400), int(50))])
        pygame.draw.rect(screen, ball_color, [(int((size[0] / 2) - 200),
                                               int((size[1] / 2) + 10)),
                                              (int(400), int(50))])
        pygame.display.flip()
