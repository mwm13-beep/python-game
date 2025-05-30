import pygame
from source.units.unit import Unit

class Player(Unit):
    def __init__(self, x: float, y:float , sprite: pygame.Surface = None) -> None:
        super().__init__(x, y)
        self.sprite = sprite

    def draw(self, surface: pygame.Surface) -> None:
        if self.sprite is not None:
            rect = self.sprite.get_rect(center=(self.x, self.y))
            surface.blit(self.sprite, rect)
        else:
            super().draw(surface)