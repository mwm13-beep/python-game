import pygame
from direction import Direction

class Unit:
    def __init__(self, coordinates, color, id = 0, max_hp = 10, movement = 4, defense = 2, atk = 3, atk_range = 1, atk_anim = None, facing = Direction.UP):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.color = color
        self.id = id
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.movement = movement
        self.defense = defense
        self.atk = atk
        self.atk_range = atk_range
        self.atk_anim = atk_anim
        self.facing = facing

    def attack(self, target, grid):
        self.change_facing(target.x, target.y)
        if self.atk_anim:
            return self.atk_anim((self.x, self.y), (target.x, target.y), self.facing, grid)
        else:
            return None

    def move(self, dx, dy):
        self.change_facing(dx, dy)
        self.x = dx
        self.y = dy

    def change_facing(self, x, y):
        if x < self.x:
            self.facing = Direction.LEFT
        elif x > self.x:
            self.facing = Direction.RIGHT
        elif y < self.y:
            self.facing = Direction.UP
        else:
            self.facing = Direction.DOWN

    def draw(self, screen, radius, dx = 0, dy = 0):
        if dx != 0 or dy != 0:
            self.move(dx, dy)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)

        # Define the arrowhead points based on the facing direction
        if self.facing == Direction.UP:
            arrow_points = [(self.x, self.y - radius), (self.x - 5, self.y - radius + 10), (self.x + 5, self.y - radius + 10)]
        elif self.facing == Direction.DOWN:
            arrow_points = [(self.x, self.y + radius), (self.x - 5, self.y + radius - 10), (self.x + 5, self.y + radius - 10)]
        elif self.facing == Direction.LEFT:
            arrow_points = [(self.x - radius, self.y), (self.x - radius + 10, self.y - 5), (self.x - radius + 10, self.y + 5)]
        elif self.facing == Direction.RIGHT:
            arrow_points = [(self.x + radius, self.y), (self.x + radius - 10, self.y - 5), (self.x + radius - 10, self.y + 5)]

        # Draw the arrowhead
        pygame.draw.polygon(screen, (0, 0, 0), arrow_points)

    def take_damage(self, attacker):
        self.current_hp -= attacker.atk - self.defense
        return self.current_hp <= 0