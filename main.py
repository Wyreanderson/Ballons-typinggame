import pygame

#start
pygame.init

#window name
pygame.display.set_caption("Ninja Typing")

#screen
screen = pygame.display.set_mode((400, 720))

#fps
clock = pygame.time.Clock()

#window loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)


pygame.quit