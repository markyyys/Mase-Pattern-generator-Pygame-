import random

from pygame_init import *

running = True
x = 0
y = 0
walls = []
screen.fill((50, 50, 60))
def draw():
    global x, y, walls
    if random.randint(0, 1) == 0:
        walls.append(pygame.draw.line(screen, (110, 110, 100), (x, y), (x + 20, y + 20), 10))
        #walls.append(pygame.draw.line(screen, (160, 160, 150), (x, y), (x + 20, y + 20), 6))
        #walls.append(pygame.draw.line(screen, (210, 210, 200), (x, y), (x + 20, y + 20), 4))

    else:
        walls.append(pygame.draw.line(screen, (70, 70, 80), (x + 20, y), (x, y + 20), 10))
        #walls.append(pygame.draw.line(screen, (120, 120, 130), (x + 20, y), (x, y + 20), 6))
        #walls.append(pygame.draw.line(screen, (170, 170, 180), (x + 20, y), (x, y + 20), 4))

    x += 20
    if x >= WINDOW_SIZE[0] and y < WINDOW_SIZE[1]:
        x = 0
        y += 20


for i in range(800 * 600):
    draw()
while running:
    for e in events:
        if e.type == pygame.QUIT:
            break




    pygame.display.flip()
    clock.tick(60)
pygame.quit()