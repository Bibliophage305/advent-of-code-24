from advent_of_code import advent
from collections import Counter


class Solver(advent.Advent):
    part_1_test_solution = 11
    part_2_test_solution = 31

    def process_data(self, data):
        left_list, right_list = [], []
        for line in data:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
        return left_list, right_list

    def part_1(self, left_list, right_list):
        left_list.sort()
        right_list.sort()
        return sum(abs(left - right) for left, right in zip(left_list, right_list))

    def part_2(self, left_list, right_list):
        frequency = Counter(right_list)
        return sum(val * frequency[val] for val in left_list)
