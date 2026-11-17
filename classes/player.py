# evil messy code

import pygame
import os
from classes.block import Block

pygame.font.init()

comic_sans_ms = pygame.font.SysFont("Comic Sans MS", 15)

def clamp(number: float, min: float, max: min) -> float:
    if number > max:
        return max
    elif number < min:
        return min
    else:
        return number

class Player:
    surface: pygame.surface
    rect: pygame.Rect
    gravity = 0.4
    speed = 0.5
    jump_power = 5
    last_mined = 0
    mining_cooldown = 250
    last_floor = 0
    mined = {}

    def __init__(self, surface: pygame.surface, x: int, y: int):
        self.surface = surface

        image = pygame.image.load(os.path.join("resources", "player.png")).convert_alpha()
        self.image = image

        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.rect = rect

    def get_nearest_breakable_block(self, blocks: list[Block]) -> Block:
        player_position = pygame.Vector2(self.rect.midbottom)
        nearest_block = None
        nearest_distance = 10000

        for block in blocks:
            if block.is_breakable():
                block_position = pygame.Vector2(block.rect.midtop)
                if player_position.y <= block_position.y and (player_position.x - block_position.x) < 32 :
                    distance = player_position.distance_to(block_position)
                    if distance < nearest_distance:
                        nearest_distance = distance
                        nearest_block = block

        return nearest_block

    def is_grounded(self, blocks: list[Block]) -> bool:
        nearest_block = self.get_nearest_breakable_block(blocks)
        self.last_floor = nearest_block.rect.top
        
        return self.rect.bottom == nearest_block.rect.top
    
    def is_above_ground(self, blocks: list[Block]) -> bool:
        nearest_block = self.get_nearest_breakable_block(blocks)
        self.last_floor = nearest_block.rect.top
        
        return self.rect.bottom >= nearest_block.rect.top

    # gravity and jumping could be heavily improved
    def process(self, delta_time: float, blocks: list[Block]):
        if not self.is_above_ground(blocks):
            self.rect.bottom = clamp(self.rect.bottom + self.gravity * delta_time, 0, self.last_floor)

        screen = self.surface
        index = 0
        for ore, amount in self.mined.items():
            text_surface = comic_sans_ms.render(f"{ore}: {amount}", True, (0, 0, 0))
            screen.blit(text_surface, (0, index))
            index += comic_sans_ms.get_height()

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def can_jump(self, blocks: list[Block]) -> bool:
        player_position = pygame.Vector2(self.rect.midtop)

        for block in blocks:
            if block.is_breakable():
                block_position = pygame.Vector2(block.rect.midbottom)
                if abs((block_position.x - player_position.x)) <= 16 and block_position.y == player_position.y:
                    return False
        return self.is_grounded(blocks) and True

    def jump(self, delta_time: float, blocks: list[Block]):
        if self.can_jump(blocks):
            self.rect.y -= self.jump_power * delta_time

    def move_left(self, delta_time: float):
        self.rect.x -= self.speed * delta_time

    def move_right(self, delta_time: float):
        self.rect.x += self.speed * delta_time

    def mine(self, blocks: list[Block]):
        ticks = pygame.time.get_ticks()
        if (ticks - self.last_mined) >= self.mining_cooldown:
            self.last_mined = ticks

            nearest_block = self.get_nearest_breakable_block(blocks)
            if nearest_block:
                nearest_block.destroy()