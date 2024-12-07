from advent_of_code import advent

import itertools


class Solver(advent.Advent):
    part_1_test_solution = 3749
    part_2_test_solution = 11387

    def process_data(self, data):
        answers, operands = [], []
        for line in data:
            answer, operand = line.split(":")
            answers.append(int(answer.strip()))
            operands.append(list(map(int, operand.strip().split())))
        return [answers, operands]

    def is_possible(self, answer, operands, operators):
        for operators in itertools.product(operators, repeat=len(operands) - 1):
            expression = operands[0]
            for operator, operand in zip(operators, operands[1:]):
                if operator == "+":
                    expression += operand
                elif operator == "*":
                    expression *= operand
                elif operator == "|":
                    expression = int(str(expression) + str(operand))
                if expression > answer:
                    break
            if expression == answer:
                return True
        return False

    def part_1(self, answers, operands):
        return sum(a for a, o in zip(answers, operands) if self.is_possible(a, o, "+*"))

    def part_2(self, answers, operands):
        return sum(
            a for a, o in zip(answers, operands) if self.is_possible(a, o, "+*|")
        )
