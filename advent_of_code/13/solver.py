from advent_of_code import advent


class Solver(advent.Advent):
    part_1_test_solution = 480
    part_2_test_solution = 875318608908

    def process_data(self, data):
        machines = []
        for button_a, button_b, prize in zip(data[::4], data[1::4], data[2::4]):
            machine = []
            _, x_val, y_val = button_a.strip().split("+")
            machine.append((int(x_val.split(",")[0]), int(y_val)))
            _, x_val, y_val = button_b.strip().split("+")
            machine.append((int(x_val.split(",")[0]), int(y_val)))
            _, x_val, y_val = prize.strip().split("=")
            machine.append((int(x_val.split(",")[0]), int(y_val)))
            machines.append(machine)
        return [machines]

    def solve(self, a_x, a_y, b_x, b_y, t_x, t_y):
        # haven't taken into account det=0 but it doesn't seem to be a problem
        determinant = a_x * b_y - a_y * b_x
        x = b_y * t_x - b_x * t_y
        y = a_x * t_y - a_y * t_x
        if x % determinant == 0 and y % determinant == 0:
            a_presses = x // determinant
            b_presses = y // determinant
            if a_presses >= 0 and b_presses >= 0:
                return 3 * a_presses + b_presses
        return 0

    def part_1(self, machines):
        return sum(
            self.solve(a_x, a_y, b_x, b_y, t_x, t_y)
            for (a_x, a_y), (b_x, b_y), (t_x, t_y) in machines
        )

    def part_2(self, machines):
        return sum(
            self.solve(a_x, a_y, b_x, b_y, t_x + 10000000000000, t_y + 10000000000000)
            for (a_x, a_y), (b_x, b_y), (t_x, t_y) in machines
        )
