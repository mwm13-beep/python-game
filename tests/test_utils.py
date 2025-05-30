TILE_SIZE = 32

test_map_basic = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

class DummyGameState:
    def __init__(self):
        self.dt = 1
        self.flags = {}
