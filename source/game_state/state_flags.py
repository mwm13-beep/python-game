from enum import Flag, auto


class StateFlag(Flag):
    MENU_OPEN = auto()
    CAMERA_LOCKED = auto()
    INPUT_DISABLED = auto()