from advent_of_code import advent

from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    @classmethod
    def from_arrow(cls, arrow):
        return {
            "^": cls.UP,
            ">": cls.RIGHT,
            "v": cls.DOWN,
            "<": cls.LEFT,
        }[arrow]

    @property
    def turn_right(self):
        return {
            Direction.UP: Direction.RIGHT,
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP,
        }[self]

    @property
    def movement_vector(self):
        return {
            Direction.UP: (-1, 0),
            Direction.RIGHT: (0, 1),
            Direction.DOWN: (1, 0),
            Direction.LEFT: (0, -1),
        }[self]


class Solver(advent.Advent):
    part_1_test_solution = 41
    part_2_test_solution = 6

    def process_data(self, data):
        grid = [list(line.strip()) for line in data]
        direction, pos = None, None
        for r_i, row in enumerate(grid):
            for c_i, cell in enumerate(row):
                if cell in "<^v>":
                    direction = Direction.from_arrow(cell)
                    pos = (r_i, c_i)
                    grid[r_i][c_i] = "."
                    break
            if direction is not None:
                break
        return [grid, direction, pos]

    def get_path(self, grid, direction, pos):
        seen = set()
        while True:
            if (pos, direction) in seen:
                return None
            seen.add((pos, direction))
            next_pos = (
                pos[0] + direction.movement_vector[0],
                pos[1] + direction.movement_vector[1],
            )
            if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
                break
            if grid[next_pos[0]][next_pos[1]] == "#":
                direction = direction.turn_right
            else:
                pos = next_pos
        return {el[0] for el in seen}

    def part_1(self, grid, direction, pos):
        return len(self.get_path(grid, direction, pos))

    def part_2(self, grid, start_direction, start_pos):
        total = 0
        for r_i, c_i in self.get_path(grid, start_direction, start_pos) - {start_pos}:
            grid[r_i][c_i] = "#"
            if self.get_path(grid, start_direction, start_pos) is None:
                total += 1
            grid[r_i][c_i] = "."
        return total
