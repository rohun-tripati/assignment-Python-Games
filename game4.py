bif="bg.jpg"
mif="ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)
myfont = pygame.font.SysFont("monospace", 15)
label = myfont.render("Some text!", 1, (255,255,0))

points = [(20,120),(140,140),(110,30)]
color = (255,255,0)


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.lock()
    pygame.draw.polygon(screen,color,points)
    screen.unlock()
    screen.blit(label, (200, 100))
    pygame.display.update()
    
