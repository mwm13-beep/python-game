from __future__ import annotations
from typing import TYPE_CHECKING
from source.controllers.controller import Controller
import pygame
from source.game_state.state_flags import StateFlag
from typing import Set

if TYPE_CHECKING:
    from source.game_state.game_state import GameState

class ExplorationController(Controller):
    def __init__(self) -> None:
        self.held_keys: Set[int] = set()

    def handle_input(self, event: pygame.event.Event, game_state: GameState) -> None:
        player = game_state.player

        if not game_state.flags[StateFlag.MENU_OPEN]:
            if event.type == pygame.KEYDOWN:
                self.held_keys.add(event.key)
            elif event.type == pygame.KEYUP:
                self.held_keys.discard(event.key)  # No error if key not present

            # Resolve velocity based on current held keys
            vx = vy = 0
            if pygame.K_w in self.held_keys or pygame.K_UP in self.held_keys:
                vy -= 1
            if pygame.K_s in self.held_keys or pygame.K_DOWN in self.held_keys:
                vy += 1
            if pygame.K_a in self.held_keys or pygame.K_LEFT in self.held_keys:
                vx -= 1
            if pygame.K_d in self.held_keys or pygame.K_RIGHT in self.held_keys:
                vx += 1

            player.velocity.x = vx
            player.velocity.y = vy


