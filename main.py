import operator as op
from functools import partial, reduce
from itertools import chain
from collections import UserList
import pygame
from pygame.locals import *
from pygame.math import Vector2 as vector

pygame.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)
background = Color(161, 161, 161)
foreground = Color(255, 255, 255)
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
screen_rect = screen.get_rect()
fps = 0

STEP = USEREVENT + 0

post_event = lambda e:pygame.event.post(pygame.event.Event(e))

while True:
  clock.tick(30)
  fps = clock.get_fps()
  screen.fill(background)
  
  if pygame.event.get(QUIT):
    break
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        pygame.event.post(pygame.event.Event(QUIT))
  
  screen.blit(font.render(str(int(fps)), 0, foreground), (0, 0))
  pygame.display.flip()
pygame.quit()
