from __future__ import annotations
from enum import Enum, auto
import math
from typing import List, TYPE_CHECKING
import pygame
from abc import ABC
from source.commands.command import Command
from source.config import TILE_SIZE
from source.grid import Grid

if TYPE_CHECKING:
    from source.game_state.game_state import GameState

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class UnitState(Enum):
    IDLE = auto()
    MOVING = auto()
    ATTACKING = auto()
    STUNNED = auto()

class Unit(ABC):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        self.velocity = pygame.Vector2(0, 0)
        self.speed = 200  # pixels per second or per frame depending on timing
        self.facing: Direction = Direction.UP
        self.command_queue: List[Command] = []
        self.curr_command: Command = None

    def update_state(self, game_state: GameState):
        self.move(game_state)

    def draw(self, surface: pygame.Surface) -> None:
        radius = TILE_SIZE // 2 - 2
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), radius)
        
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
        pygame.draw.polygon(surface, (0, 0, 0), arrow_points)

    def move(self, game_state: GameState) -> None:
        movement = self.velocity * self.speed * game_state.dt

        prev_x, prev_y = self.x, self.y
        self.x += movement.x
        self.y += movement.y

        # Full movement blocked?
        if not self.is_passable(game_state):
            # Try y-only
            self.x = prev_x
            self.y = prev_y + movement.y
            if self.is_passable(game_state):
                self.change_facing(0, self.y - prev_y)
                return

            # Try x-only
            self.x = prev_x + movement.x
            self.y = prev_y
            if self.is_passable(game_state):
                self.change_facing(self.x - prev_x, 0)
                return

            # Both blocked
            self.x, self.y = prev_x, prev_y
        else:
            # Move succeeded
            self.change_facing(self.x - prev_x, self.y - prev_y)

    def is_passable(self, game_state: GameState) -> bool:
        tiles = game_state.grid.tiles
        radius = TILE_SIZE // 2 - 1  # Slightly inside the tile edge
        center = pygame.Vector2(self.x, self.y)

        # Sample 8 directions around the circle
        for angle_deg in range(0, 360, 45):
            angle_rad = math.radians(angle_deg)
            offset = pygame.Vector2(
                math.cos(angle_rad) * radius,
                math.sin(angle_rad) * radius
            )
            sample_pos = center + offset
            grid_x, grid_y = Grid.screen_to_grid_index(sample_pos.x, sample_pos.y)

            if (
                not (0 <= grid_y < len(tiles)) or
                not (0 <= grid_x < len(tiles[grid_y])) or
                not tiles[grid_y][grid_x].isPassable()
            ):
                return False  # One of the samples hit an impassable tile

        return True  # All points are within passable terrain

    def change_facing(self, dx: float, dy: float) -> None:
        if abs(dx) > abs(dy):
            self.facing = Direction.LEFT if dx < 0 else Direction.RIGHT
        elif dy != 0:
            self.facing = Direction.UP if dy < 0 else Direction.DOWN

        
    # def __init__(self, coordinates, color, id = 0, max_hp = 10, movement = 4, defense = 2, atk = 3, atk_range = 1, atk_anim = None, facing = Direction.UP):
    #     self.x = coordinates[0]
    #     self.y = coordinates[1]
    #     self.color = color
    #     self.id = id
    #     self.max_hp = max_hp
    #     self.current_hp = max_hp
    #     self.movement = movement
    #     self.defense = defense
    #     self.atk = atk
    #     self.atk_range = atk_range
    #     self.atk_anim = atk_anim
    #     self.facing = facing

    # def attack(self, target, grid):
    #     self.change_facing(target.x, target.y)
    #     if self.atk_anim:
    #         return self.atk_anim((self.x, self.y), (target.x, target.y), self.facing, grid)
    #     else:
    #         return None

    # def draw(self, screen, radius, dx = 0, dy = 0):
    #     if dx != 0 or dy != 0:
    #         self.move(dx, dy)
    #     pygame.draw.circle(screen, self.color, (self.x, self.y), radius)

    #     # Define the arrowhead points based on the facing direction
    #     if self.facing == Direction.UP:
    #         arrow_points = [(self.x, self.y - radius), (self.x - 5, self.y - radius + 10), (self.x + 5, self.y - radius + 10)]
    #     elif self.facing == Direction.DOWN:
    #         arrow_points = [(self.x, self.y + radius), (self.x - 5, self.y + radius - 10), (self.x + 5, self.y + radius - 10)]
    #     elif self.facing == Direction.LEFT:
    #         arrow_points = [(self.x - radius, self.y), (self.x - radius + 10, self.y - 5), (self.x - radius + 10, self.y + 5)]
    #     elif self.facing == Direction.RIGHT:
    #         arrow_points = [(self.x + radius, self.y), (self.x + radius - 10, self.y - 5), (self.x + radius - 10, self.y + 5)]

    #     # Draw the arrowhead
    #     pygame.draw.polygon(screen, (0, 0, 0), arrow_points)

    #     # Draw the HP text below the unit
    #     self.draw_hp(screen, radius)

    # def draw_hp(self, screen, radius):
    #     font = pygame.font.Font(None, 16)
    #     hp_text = f"{self.current_hp}/{self.max_hp}"
    #     text_color = (255, 0, 0) if self.current_hp <= self.max_hp // 4 else (255, 255, 255)
    #     text_surf = font.render(hp_text, True, text_color)
    #     text_rect = text_surf.get_rect(center=(self.x, self.y + radius + 15))
    #     screen.blit(text_surf, text_rect)

    # def take_damage(self, attacker):
    #     self.current_hp -= attacker.atk - self.defense
    #     return self.current_hp <= 0