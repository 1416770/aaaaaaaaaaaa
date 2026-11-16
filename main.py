import pygame
import random
from classes.block import Block
from classes.player import Player

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

player = Player(screen, width / 2, 320)

layers = [
    [512, [["diamond", 5], ["gold", 10], ["iron", 20], ["stone", 100]]],
    [448, [["dirt", 100]]],
    [384, [["grass", 100]]],
    [128, [["sky", 100]]],
    [0, [["cloud", 5], ["sky", 100]]]
]

def get_block(x: int, y: int) -> Block:
    for layer in layers:
        if y >= layer[0]:

            luck = random.randint(1, 100)
            for block in layer[1]:
                if luck <= block[1]:
                    return Block(screen, block[0], x, y)
                
            return Block(screen, layer[1][0][0], x, y)

blocks = []
for x in range(0, width, 64):
    for y in range(0, height, 64):
        blocks.append(get_block(x, y))

running = True
delta_time = 0
elapsed = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for block in blocks:
        block.draw()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        player.jump(delta_time)
    if keys_pressed[pygame.K_a]:
        player.move_left(delta_time)
    if keys_pressed[pygame.K_d]:
        player.move_right(delta_time)
    if keys_pressed[pygame.K_SPACE]:
        player.mine(elapsed)

    player.process(delta_time)
    player.draw()

    pygame.display.flip()
    delta_time = clock.tick(60)
    elapsed += delta_time

pygame.quit()