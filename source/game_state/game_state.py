from __future__ import annotations
from enum import Enum, auto, Flag
from typing import List, Tuple
from source.commands.command import Command
from source.controllers.controller import Controller
from source.controllers.exploration_controller import ExplorationController
from source.grid import Grid
from source.units.player import Player
from collections import deque
from source.units.unit import Unit
from source.game_state.state_flags import StateFlag

class GameMode(Enum):
    COMBAT = auto()
    DIALOGUE = auto()
    EXPLORING = auto()

class GameState:
    def __init__(self, grid: Grid) -> None:
        x, y = Grid.screen_to_grid_center(60,60)
        self.player: Player = Player(x, y)
        self.controller: Controller = ExplorationController()
        self.dt: float = 0
        self.command_queue: deque[Command] = deque()
        self.grid: Grid = grid        
        self.obj_in_grid = [self.player]    
        self.current_turn: int = 0
        self.turn_order: List[Unit] = []
        self.selection = None
        self.camera_position: Tuple[float, float] = (0, 0)
        self.mode = GameMode.EXPLORING
        self.flags: dict[StateFlag, bool] = {
            StateFlag.MENU_OPEN: False,
            StateFlag.CAMERA_LOCKED: False,
            StateFlag.INPUT_DISABLED: False,
        }