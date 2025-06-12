from __future__ import annotations
from abc import ABC, abstractmethod
import pygame
from typing import TYPE_CHECKING
import sys

if TYPE_CHECKING:
    from source.game_state.game_state import GameState

class Controller(ABC):
    def handle_input(self, event: pygame.event.Event, game_state) -> None:
        self.check_for_exit(event)
        self._handle_input(event, game_state)  # must be defined in child

    def check_for_exit(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            response = self.display_quit_warning()
            if response:
                pygame.quit()
                sys.exit()

    def display_quit_warning(self) -> bool:
        # Replace with actual UI dialog later
        print("Unsaved progress will be deleted. Are you sure you want to quit?")
        return True  # Simulate confirmation

    @abstractmethod
    def _handle_input(self, event: pygame.event.Event, game_state) -> None:
        pass