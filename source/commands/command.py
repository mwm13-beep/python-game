from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def resolve_target(self, game_state) -> None:
        """Push this command to its intended target (unit, tile, system)"""
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def update(self):
        pass
    
