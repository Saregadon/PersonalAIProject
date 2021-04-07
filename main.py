import pygame as pg
import pygame.gfxdraw
import time
import random

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

#sets display for the screen
pygame.display.init()

screen_width = 800 #x
screen_height = 600 #y

#sets screen up
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)

pixelset = pygame.PixelArray(screen)
pixelset[10][20] = white

clock = pygame.time.Clock()

def Screen_Output():
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            else:
                screen.fill(black)
                pygame.display.flip()
            pygame.display.update()

def Mouse_Position(pos):
    while pygame.event.get() and pygame.mouse.get_focused(): #checks to see if terminal is receiving mouse
        if pygame.mouse.get_focused() == True:
            #while pygame.mouse.get_pressed(num_buttons=3)
                Mouse_drawing(pygame.mouse.get_pos()) 
                #call screen press

def Mouse_drawing(pos):
    pygame.gfxdraw.pixel(screen, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[0], color=(0, 0, 128)) #mess with
    return

#Width = int(input("Please set the Width for the Display: "))
#Height = int(input("Please set the Height for the Display: "))

framerate = pygame.time.Clock()
framerate.tick(60)
Screen_Output()
Mouse_Position(pygame.mouse.get_pos())

#https://www.pygame.org/news