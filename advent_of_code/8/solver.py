from advent_of_code import advent

from collections import defaultdict
from itertools import combinations


class Solver(advent.Advent):
    part_1_test_solution = 14
    part_2_test_solution = 34

    def process_data(self, data):
        antennae = defaultdict(list)
        for r_i, row in enumerate(data):
            for c_i, col in enumerate(row.strip()):
                if col != ".":
                    antennae[col].append((r_i, c_i))
        return [antennae, len(data), len(data[0].strip())]

    def part_1(self, antennae, height, width):
        antinodes = set()
        for locations in antennae.values():
            for a, b in combinations(locations, 2):
                for r_i, c_i in [
                    (2*a[0] - b[0], 2*a[1] - b[1]),
                    (2*b[0] - a[0], 2*b[1] - a[1])
                ]:
                    if 0 <= r_i < height and 0 <= c_i < width:
                        antinodes.add((r_i, c_i))
        return len(antinodes)

    def part_2(self, antennae, height, width):
        antinodes = set()
        for locations in antennae.values():
            for a, b in combinations(locations, 2):
                r_i, c_i = a
                while 0 <= r_i < height and 0 <= c_i < width:
                    antinodes.add((r_i, c_i))
                    r_i -= b[0] - a[0]
                    c_i -= b[1] - a[1]
                r_i, c_i = b
                while 0 <= r_i < height and 0 <= c_i < width:
                    antinodes.add((r_i, c_i))
                    r_i += b[0] - a[0]
                    c_i += b[1] - a[1]
        return len(antinodes)
