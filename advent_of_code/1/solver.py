from advent_of_code import advent
from collections import Counter


class Solver(advent.Advent):
    part_1_test_solution = 11
    part_2_test_solution = 31

    def process_data(self, data):
        pairs = [map(int, line.split()) for line in data]
        return map(list, zip(*pairs))

    def part_1(self, left_list, right_list):
        left_list.sort()
        right_list.sort()
        return sum(abs(left - right) for left, right in zip(left_list, right_list))

    def part_2(self, left_list, right_list):
        left_freq, right_freq = map(Counter, (left_list, right_list))
        return sum(key * val * right_freq[key] for key, val in left_freq.items())
