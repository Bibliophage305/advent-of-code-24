from advent_of_code import advent

from functools import cache


class Solver(advent.Advent):
    part_1_test_solution = 55312
    part_2_test_solution = 65601038650482

    def process_data(self, data):
        return [[int(x) for x in data[0].strip().split()]]
    
    @cache
    def after_n_blinks(self, stone, n):
        if n == 0:
            return 1
        if stone == 0:
            return self.after_n_blinks(1, n-1)
        s = str(stone)
        if len(s) % 2 == 0:
            return self.after_n_blinks(int(s[:len(s)//2]), n-1) + self.after_n_blinks(int(s[len(s)//2:]), n-1)
        return self.after_n_blinks(stone * 2024, n-1)

    def part_1(self, data):
        return sum(self.after_n_blinks(x, 25) for x in data)

    def part_2(self, data):
        return sum(self.after_n_blinks(x, 75) for x in data)
