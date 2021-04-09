import pygame as pg
import pygame.gfxdraw
import time
import random

pygame.init()

#set (Red, Green, Blue) #RGB
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

#sets display for the screen
pygame.display.init()

screen_width = 20 #x values for screen
screen_height = 20 #y values for screen

to_scale = 10

#sets up rectangle

rect_width, rect_height = 2, 2
vel = 2

x, y = 10, 10
#sets screen up
screen = pygame.Surface((screen_width, screen_height))
window = pygame.display.set_mode((screen_width*to_scale, screen_height*to_scale))

framerate = pygame.time.Clock()
framerate.tick(60)

pixelset = pygame.PixelArray(screen)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawlocation = event.pos
            pygame.draw.line(screen, white, drawlocation, drawlocation)
            pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            drawlocation = event.pos
            pygame.draw.line(screen, white, drawlocation, drawlocation)
            pygame.display.update()

    screen.fill(black)
    pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))
    window.blit(pygame.transform.scale(screen, window.get_rect().size), (0,0))
    pygame.display.update()


def Mouse_Position(pos):
    while pygame.event.get() and pygame.mouse.get_focused(): #checks to see if terminal is receiving mouse
        if pygame.mouse.get_focused() == True:
            #while pygame.mouse.get_pressed(num_buttons=3)
                Mouse_drawing(pygame.mouse.get_pos()) 
                #call screen press

#Width = int(input("Please set the Width for the Display: "))
#Height = int(input("Please set the Height for the Display: "))

Mouse_Position(pygame.mouse.get_pos())

#https://www.pygame.org/news