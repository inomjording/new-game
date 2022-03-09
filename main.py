import pygame
import sys
from pygame.locals import *
from pygame_animatedgif import AnimatedGifSprite

pygame.init()
DISPLAYSURF = pygame.display.set_mode((320, 180))
bg = pygame.image.load("images/home.png")
you = pygame.image.load("images/a little friend.gif")
pygame.display.set_caption('New Game')

pygame.mixer.init()
pygame.mixer.music.load("sound/two.mp3")
pygame.mixer.music.play(-1)

x = 50
y = 90
step = 5
while True:
    for event in pygame.event.get():
        DISPLAYSURF.blit(bg, (0, 0))
        DISPLAYSURF.blit(you, (x, y))
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            x -= step
        if key_input[pygame.K_UP]:
            y -= step
        if key_input[pygame.K_RIGHT]:
            x += step
        if key_input[pygame.K_DOWN]:
            y += step
        pygame.display.update()
