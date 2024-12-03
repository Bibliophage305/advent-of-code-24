from advent_of_code import advent

import re


class Solver(advent.Advent):
    part_1_test_solution = 161
    part_2_test_solution = 48
    
    test_data_paths = ["test1", "test2"]

    def process_data(self, data):
        return ["".join(data)]
    
    def add_all_muls(self, data):
        return sum(a*b for a, b in (map(int, i.split(',')) for i in re.findall(r'(?<=mul\()\d+,\d+(?=\))', data)))

    def part_1(self, data):
        return self.add_all_muls(data)

    def part_2(self, data):
        split_on_dont = ("do()" + data).split("don't()")
        return sum(sum(map(self.add_all_muls, x.split("do()")[1:])) for x in split_on_dont)
