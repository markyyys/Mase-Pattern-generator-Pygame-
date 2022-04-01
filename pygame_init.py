import pygame
from settings import *

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Monopoly")
clock = pygame.time.Clock()
events = pygame.event.get()