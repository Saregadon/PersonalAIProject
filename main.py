import pygame as pg
import pygame.gfxdraw

def Screen_initialization(x, y): #sets display for the screen
    pygame.display.init

    screen_width = x
    screen_height = y

    running = True
    while running:
        screen = pygame.display.set_mode([screen_width, screen_height])
        screen.fill([255,255,255])
        #pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    return screen

def Mouse_Position(pos):
    while pygame.event.get() and pygame.mouse.get_focused(): #checks to see if terminal is receiving mouse
        if pygame.mouse.get_focused() == True:
            while pygame.mouse.get_pressed(num_buttons=3)
                Mouse_drawing(pygame.mouse.get_pos()) 
                #call screen press

def Mouse_drawing(pos):
    pygame.gfxdraw.pixel(screen, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[0], color=(0, 0, 128)) #mess with
    return

#Width = int(input("Please set the Width for the Display: "))
#Height = int(input("Please set the Height for the Display: "))

framerate = pygame.time.Clock()
framerate.tick(60)
Screen_initialization(1000, 500)
Mouse_Position(pygame.mouse.get_pos())

#https://www.pygame.org/news