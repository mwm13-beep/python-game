import pygame

class Unit:
    def __init__(self, coordinates, color, id = 0, hp = 10, movement = 4, defense = 2, atk = 3):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.color = color
        self.id = id
        self.hp = hp
        self.movement = movement
        self.defense = defense
        self.atk = atk

    def move(self, dx, dy):
        self.x = dx
        self.y = dy

    def draw(self, screen, radius):
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)