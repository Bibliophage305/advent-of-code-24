from advent_of_code import advent

import re


class Solver(advent.Advent):
    part_1_test_solution = 161
    part_2_test_solution = 48

    test_data_paths = ["test1", "test2"]

    def process_data(self, data):
        return ["".join(data).replace("\n", "")]

    def add_all_muls(self, data):
        return sum(
            a * b
            for a, b in (
                map(int, i.split(","))
                for i in re.findall(r"(?<=mul\()\d+,\d+(?=\))", data)
            )
        )

    def part_1(self, data):
        return self.add_all_muls(data)

    def part_2(self, data):
        return self.add_all_muls(re.sub(r"don't\(\).*?(do\(\)|$)", "", data))
