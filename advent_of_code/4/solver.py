from advent_of_code import advent


class Solver(advent.Advent):
    part_1_test_solution = 18
    part_2_test_solution = 9

    def process_data(self, data):
        return [[line.strip() for line in data]]

    def part_1(self, data):
        WORDS = ("XMAS", "SAMX")
        total = 0
        # horizontal
        for line in data:
            total += sum(map(line.count, WORDS))
        # vertical
        for line in map("".join, zip(*data)):
            total += sum(map(line.count, WORDS))
        # diagonal
        for r_i in range(len(data) - 3):
            # down-right diagonal
            for c_i in range(len(data[r_i]) - 3):
                if "".join(data[r_i + i][c_i + i] for i in range(4)) in WORDS:
                    total += 1
            # down-left diagonal
            for c_i in range(3, len(data[r_i])):
                if "".join(data[r_i + i][c_i - i] for i in range(4)) in WORDS:
                    total += 1
        return total

    def part_2(self, data):
        total = 0
        for r_i in range(1, len(data) - 1):
            for c_i in range(1, len(data[r_i]) - 1):
                if data[r_i][c_i] != "A":
                    continue
                candidate = (
                    data[r_i - 1][c_i - 1]
                    + data[r_i - 1][c_i + 1]
                    + data[r_i + 1][c_i + 1]
                    + data[r_i + 1][c_i - 1]
                )
                if candidate in ("MSSM", "SSMM", "MMSS", "SMMS"):
                    total += 1
        return total
