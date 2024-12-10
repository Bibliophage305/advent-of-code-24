from advent_of_code import advent

from collections import defaultdict


class Solver(advent.Advent):
    part_1_test_solution = 36
    part_2_test_solution = 81

    def process_data(self, data):
        data = [row.strip() for row in data]
        graph, trailheads, trailtails = defaultdict(set), set(), set()
        for r_i, row in enumerate(data):
            for c_i, cell in enumerate(row):
                if cell == "0":
                    trailheads.add((r_i, c_i))
                if cell == "9":
                    trailtails.add((r_i, c_i))
                    continue
                for n_r_i, c_r_i in [
                    (r_i + 1, c_i),
                    (r_i, c_i + 1),
                    (r_i - 1, c_i),
                    (r_i, c_i - 1),
                ]:
                    if (
                        0 <= n_r_i < len(data)
                        and 0 <= c_r_i < len(row)
                        and int(cell) + 1 == int(data[n_r_i][c_r_i])
                    ):
                        graph[(r_i, c_i)].add((n_r_i, c_r_i))
        return [graph, trailheads, trailtails]

    def count_trails(self, graph, trailheads, trailtails, only_unique=True):
        total = 0
        for trailhead in trailheads:
            stack, seen = [trailhead], set()
            while stack:
                current = stack.pop()
                if current in seen and only_unique:
                    continue
                seen.add(current)
                if current in trailtails:
                    total += 1
                    continue
                stack += [neighbour for neighbour in graph[current]]
        return total

    def part_1(self, graph, trailheads, trailtails):
        return self.count_trails(graph, trailheads, trailtails)

    def part_2(self, graph, trailheads, trailtails):
        return self.count_trails(graph, trailheads, trailtails, only_unique=False)
