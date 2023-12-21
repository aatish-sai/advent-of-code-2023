from dataclasses import dataclass


@dataclass
class Tile:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def get_boundary(self):
        return [
            Tile(self.x - 1, self.y),
            Tile(self.x + 1, self.y),
            Tile(self.x, self.y - 1),
            Tile(self.x, self.y + 1),
        ]

    def valid(self, map):
        if self.x < 0 or self.x >= len(map):
            return False
        if self.y < 0 or self.y >= len(map[0]):
            return False

        if map[self.x][self.y] == "#":
            return False
        return True

    def valid2(self, map):
        new_x = self.x
        new_y = self.y
        if self.x < 0:
            new_x = self.x % len(map)
        if self.x >= len(map):
            new_x = self.x % len(map)
        if self.y < 0:
            new_y = self.y % len(map[0])
        if self.y >= len(map[0]):
            new_y = self.y % len(map[0])

        if map[new_x][new_y] == "#":
            return False
        return True


map = []

initial_position = set()

traveled_tiles = set()
start = Tile


def load_input(filename: str):
    global start
    with open(filename, "r") as file:
        x = 0
        while line := file.readline():
            if "S" in line:
                start.x = x
                start.y = line.index("S")
                initial_position.add(Tile(x, line.index("S")))
            map.append([x for x in line.strip()])
            x += 1


def solve():
    steps = 0
    travel_steps = initial_position
    while steps < 500:
        next_step = set()
        while travel_steps:
            tile = travel_steps.pop()
            traveled_tiles.add(tile)

            for boundary in tile.get_boundary():
                if boundary.valid2(map):
                    next_step.add(boundary)
        travel_steps = next_step
        steps += 1

    print(len(next_step))


if __name__ == "__main__":
    load_input("test.txt")
    solve()
