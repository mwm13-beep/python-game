# wall_tile.py

import pygame
from source.tiles.tile import Tile

class WallTile(Tile):
    def draw(self, surface):
        pygame.draw.rect(surface, (150, 75, 0), self.get_rect())

    def isPassable(self):
        return False
