from source.commands.command import Command
from source.units.unit import Unit

class MoveCommand(Command):
    def __init__(self, unit: Unit, dx: float = 0, dy: float = 0) -> None: 
        self.unit: Unit = unit
        self.dx: float = dx
        self.dy: float = dy
        self.finished: bool = False

    def resolve_target(self):
        if self.unit.curr_command is None:
            self.unit.curr_command = self
        else:
            self.unit.command_queue.append(self)

    def execute(self) -> None:
        pass

    def update(self) -> None:
        pass

    def is_finished(self) -> bool:
        return self.finished
