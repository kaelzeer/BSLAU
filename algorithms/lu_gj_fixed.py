from utils import Utils, Constants
from algorithms.base_alg import Algorithm
from time_logger import Time_logger

import numpy as np

np.set_printoptions(precision=8, suppress=True)


class LUGJF(Algorithm):
    def __init__(self, matrix_num: int = 1) -> None:

        super().__init__(matrix_num)
        self.limit = 100
        self.alg_type = Constants.ALG_TYPE_NSCR
        super().post_init()

        self.b = np.zeros((self.limit, self.limit), np.double)
        self.c = np.zeros((self.limit, self.limit), np.double)

        self.y = np.zeros(self.limit)
        self.x = np.zeros(self.limit)

        self.initial_limit = 10

    def make_cell_one(self, cell_row: int, cell_col: int, last_col: int = -1):

        divider = self.c[cell_row][cell_col]
        if cell_row != cell_col or divider == 1:
            return

        if last_col == -1:
            last_col = self.limit if cell_col < Utils.NMAX else Utils.NMAX
        if divider == 0:
            non_zero_element_index = self.get_first_non_zero_col(
                cell_row, cell_col + 1)
            self.c[cell_row], self.c[non_zero_element_index] = self.c[non_zero_element_index], self.c[cell_row]
            divider = self.c[cell_row][cell_col]

        elif divider != 1:
            for col in range(cell_col, last_col):
                self.c[cell_row][col] /= divider
            self.f[cell_row] /= divider
        # self.steps_for_print_step += 1
        # Utils.print_step(self.steps_for_print_step, self.c, self.f, cell_row, cell_col, False)

    def calculate_cell(self, cell_row: int, cell_col: int, last_col: int = -1):

        if cell_row == cell_col or self.c[cell_col][cell_col] != 1.0:
            self.make_cell_one(cell_col, cell_col, last_col)

        if last_col == -1:
            last_col = self.limit if cell_col < Utils.NMAX else Utils.NMAX
        if self.c[cell_row][cell_col] != 0:
            divider = -self.c[cell_row][cell_col]
            for col in range(cell_col, last_col):
                self.c[cell_row][col] += self.c[cell_col][col] * divider
            self.f[cell_row] += self.f[cell_col] * divider

    def get_first_non_zero_col(self, row: int, first_col: int) -> int:

        last_col = self.limit
        for col in range(first_col, last_col):
            if self.a[row][col] != 0:
                return col
        return -1

    def build_triangle_matrix(self):

        for i in range(self.limit):
            for j in range(self.limit):
                if i <= j:
                    sum_b_c_i = 0

                    for k in range(i):
                        sum_b_c_i += self.b[i, k] * self.c[k, j]
                    self.c[i, j] = self.a[i, j] - sum_b_c_i
                if i >= j:
                    sum_b_c_j = 0
                    for k in range(j):
                        sum_b_c_j += self.b[i, k] * self.c[k, j]
                    self.b[i, j] = (self.a[i, j] - sum_b_c_j) / self.c[j, j]

        for i in range(self.limit):
            for left_lower_col in range(i):
                if self.b[i, left_lower_col] != 0:
                    divider = -self.b[i][left_lower_col]
                    for inner_col in range(left_lower_col, i):
                        self.b[i][inner_col] += self.b[left_lower_col][inner_col] * divider
                    self.f[i] += self.f[left_lower_col] * divider

            if self.b[i, i]:
                self.y[i] = self.f[i] / self.b[i, i]

    def solve(self):
        self.build_triangle_matrix()

        Time_logger.get_instance().start_timer_for_event('SCR matrix division')

        self.c_delta = np.zeros(self.limit)
        d = 1.0

        row = 0

        while True:
            print(f'row: {row}')

            # work with self.c moving row by row starting with last_row to 0

            print(f'iterate coords, row: {row}')
            for cur_row in range(row - 1, -1, -1):
                prev_f_row = -1.0
                cur_f_row = self.f[cur_row]
                for cur_col in range(cur_row, row):
                    calculated_this_step = False
                    print(
                        f'cur_row, cur_col : {cur_row}, {cur_col}, ', end='')
                    initial_c_value = self.c[cur_row, cur_col]

                    if cur_row == cur_col:  # on main diagonal
                        if self.c[cur_row, cur_col] == 1:  # opt
                            print()
                            continue
                        # for it_col in range(cur_row, row):  # self.limit ?
                        self.make_cell_one(cur_row, cur_col, -1)
                        calculated_this_step = True
                    else:
                        if self.c[cur_row, cur_col] == 0:  # opt
                            print()
                            continue
                        self.calculate_cell(cur_row, cur_col, -1)
                        calculated_this_step = True

                    if calculated_this_step:
                        prev_f_row = cur_f_row
                        cur_f_row = self.f[cur_row]
                        d = abs(cur_f_row - prev_f_row)

                    print(
                        f'c before: {initial_c_value} c after: {self.c[cur_row, cur_col]}')
                    print(f'calculated this step: {calculated_this_step}')
                    if (calculated_this_step):
                        print(f'\nd: {d}')
                    print(f'row: {row} c\n')
                    for i in range(10):
                        for j in range(10):
                            print(f'{self.c[i, j]} ', end='')
                        print()
                    todo = 1
            row += 1

            # do-while-emu exit condition
            if d < 1e-9 or row > self.limit:  # todo: move d to utils
                break

        Time_logger.get_instance().mark_timestamp_for_event('SCR matrix division')

        print(f'b:\n{self.b}')
        print(f'c:\n{self.c}')
        print(f'y:\n{self.y}')
        print(f'f:\n{self.f}')
