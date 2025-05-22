# water_tile.py

import pygame
from source.tiles.tile import Tile

class WaterTile(Tile):
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.get_rect())

    def isPassable(self):
        return False
