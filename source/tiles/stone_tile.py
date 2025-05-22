# stone_tile.py

import pygame
from source.tiles.tile import Tile

class StoneTile(Tile):
    def draw(self, surface):
        pygame.draw.rect(surface, (128, 128, 128), self.get_rect())

    def isPassable(self):
        return False
