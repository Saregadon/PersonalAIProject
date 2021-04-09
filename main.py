import pygame
import time
import random
#change
pygame.init()

#set (Red, Green, Blue) #RGB
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

#sets display for the screen
pygame.display.init()

#sets up clock
clock = pygame.time.Clock()

def grid(screen, screen_width, screen_height, rows):
    distanceBetweenRows = screen_width // rows
    distanceBetweenColumns = screen_height // rows
    x = 0
    y = 0
    for i in range(rows):
        #increase x by distance between rows
        #increase y by distance between columns
        x += distanceBetweenRows
        y += distanceBetweenColumns
        #draw grid
        #1 where we draw (on screen)
        #2 what color (white)
        #3 where we draw again but what place, on x and 0 by y
        #4 size our line, from x until screen width
        pygame.draw.line(screen, white, (x,0), (x, screen_width))
        #4 size our line, from screen_height to y
        pygame.draw.line(screen, white, (0, y), (screen_height, y))

def redraw(screen):
    global screen_width, screen_height, rows
    screen.fill((black))
    grid(screen, screen_width, screen_height, rows)
    pygame.display.update()

def main():
    global screen_width, screen_height, rows
    screen_width = 500 #x values for screen
    screen_height = 500 #y values for screen
    rows = 20

    screen = pygame.display.set_mode((screen_width, screen_height))

    running = True
    while running: #main runner, everything is inside of here
        clock.tick(60)
        #pygame.time.delay(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen.fill(black)
            if event.type == pygame.mouse.get_pressed(3) and event.type == pygame.MOUSEMOTION:
                drawlocation = event.pos
                pygame.draw.line(screen, white, drawlocation, drawlocation)
                pygame.display.update()
                #window.blits(pygame.transform.scale(screen, window.get_rect().size), (0,0))

        pygame.display.update()
        #redraw function
        redraw(screen)
            

#Width = int(input("Please set the Width for the Display: "))
#Height = int(input("Please set the Height for the Display: "))

#https://www.pygame.org/news