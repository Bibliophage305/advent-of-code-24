from advent_of_code import advent

from itertools import zip_longest, cycle

class Solver(advent.Advent):
    part_1_test_solution = 1928
    part_2_test_solution = 2858

    def process_data(self, data):
        return [list(map(int, data[0].strip()))]

    def part_1(self, data):
        expanded = []
        for i, (file_size, gap_size) in enumerate(zip_longest(data[::2], data[1::2], fillvalue=0)):
            expanded += [str(i)] * file_size
            expanded += ["."] * gap_size
        i = 0
        while i < len(expanded):
            if expanded[-1] == ".":
                expanded.pop()
                continue
            if expanded[i] == ".":
                expanded[i] = expanded.pop()
            i += 1
        return sum(i * int(c) for i, c in enumerate(expanded))

    def part_2(self, data):
        index = 0
        files, gaps = [], []
        for arr, size in zip(cycle([files, gaps]), data):
            arr.append([index, size])
            index += size
        for file in reversed(files):
            for gap in gaps:
                if file[0] < gap[0]:
                    break
                if file[1] <= gap[1]:
                    file[0] = gap[0]
                    gap[0] += file[1]
                    gap[1] -= file[1]
                    break
        return sum(i * sum(range(file[0], file[0] + file[1])) for i, file in enumerate(files))
    