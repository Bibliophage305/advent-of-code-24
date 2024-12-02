from advent_of_code import advent


class Solver(advent.Advent):
    part_1_test_solution = 2
    part_2_test_solution = 4

    def process_data(self, data):
        return [[list(map(int, line.split())) for line in data]]
    
    def is_safe(self, line):
        if line[0] > line[1]:
            return all(0 < a - b < 4 for a, b in zip(line, line[1:]))
        return all(0 < b - a < 4 for a, b in zip(line, line[1:]))

    def part_1(self, data):
        return sum(map(self.is_safe, data))

    def part_2(self, data):
        return sum(any(self.is_safe(line[:i] + line[i + 1:]) for i in range(len(line))) for line in data)
