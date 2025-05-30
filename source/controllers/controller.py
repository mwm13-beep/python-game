from __future__ import annotations
from abc import ABC, abstractmethod
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from source.game_state.game_state import GameState

class Controller(ABC):
    @abstractmethod
    def handle_input(self, event: pygame.event.Event, game_state: GameState) -> None:
        pass
