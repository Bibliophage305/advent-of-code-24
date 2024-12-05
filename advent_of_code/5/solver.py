from advent_of_code import advent

from functools import cmp_to_key


class Solver(advent.Advent):
    part_1_test_solution = 143
    part_2_test_solution = 123

    def process_data(self, data):
        rules, candidates = set(), []
        finding_rules = True
        for line in data:
            line = line.strip()
            if not line:
                finding_rules = False
                continue
            if finding_rules:
                rule = tuple(line.split("|"))
                rules.add(rule)
            else:
                candidates.append(line.split(","))

        def comparator(a, b):
            if (a, b) in rules:
                return -1
            if (b, a) in rules:
                return 1
            return 0

        return [candidates, comparator]

    def part_1(self, candidates, comparator):
        total = 0
        for candidate in candidates:
            if candidate == sorted(candidate, key=cmp_to_key(comparator)):
                total += int(candidate[len(candidate) // 2])
        return total

    def part_2(self, candidates, comparator):
        total = 0
        for candidate in candidates:
            sorted_candidate = sorted(candidate, key=cmp_to_key(comparator))
            if candidate != sorted_candidate:
                total += int(sorted_candidate[len(candidate) // 2])
        return total
