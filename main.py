import pygame
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

screen_width = 500 #x values for screen
screen_height = 500 #y values for screen

to_scale = 10

#sets up rectangle

rect_width, rect_height = 2, 2
vel = 2

#x = int(input('Please input x: '))
#y = int(input('Please input y: '))
#sets screen up
window = pygame.Surface((screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height)) #multiply both by to_scale to scale the surface up?

framerate = pygame.time.Clock()
framerate.tick(60)

pixelset = pygame.PixelArray(screen)

clock = pygame.time.Clock()

running = True
while running: #main runner, everything is inside of here
    clock.tick(60)
    #pygame.time.delay(60)
    for event in pygame.event.get():
        screen.fill(black)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.mouse.get_pressed(3)[0] and event.type == pygame.MOUSEMOTION:
            drawlocation = event.pos
            pygame.draw.line(screen, white, drawlocation, drawlocation)
            pygame.display.update()
            #window.blits(pygame.transform.scale(screen, window.get_rect().size), (0,0))

        pygame.display.update()
            

#Width = int(input("Please set the Width for the Display: "))
#Height = int(input("Please set the Height for the Display: "))

#https://www.pygame.org/news