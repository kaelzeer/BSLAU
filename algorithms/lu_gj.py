from utils import Utils, Constants
from algorithms.base_alg import Algorithm
from time_logger import Time_logger

import numpy as np

np.set_printoptions(precision=8, suppress=True)


class LUGJ(Algorithm):
    def __init__(self, matrix_num: int = 1) -> None:

        super().__init__(matrix_num)
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

        if divider != 1:
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

    def build_b_and_c_matrix(self, n: int) -> None:

        for i in range(n):
            sum_b_c_i = 0
            for k in range(i):
                sum_b_c_i += self.b[i, k] * self.c[k, n]
            self.c[i, n] = self.a[i, n] - sum_b_c_i
            if i:
                pass

        for j in range(n):
            sum_b_c_j = 0
            for k in range(j):
                sum_b_c_j += self.b[n, k] * self.c[k, j]
            self.b[n, j] = (self.a[n, j] - sum_b_c_j) / self.c[j, j]

        sum_b_c_n = 0
        for k in range(n):
            sum_b_c_n += self.b[n, k] * self.c[k, n]
        self.c[n, n] = self.a[n, n] - sum_b_c_n
        self.b[n, n] = (self.a[n, n] - sum_b_c_n) / self.c[n, n]

    def solve(self):

        Time_logger.get_instance().start_timer_for_event('SCR matrix division')

        # c_cur_row = 0
        # c_cur_col = 1
        self.c_delta = np.zeros(self.limit)
        d = 0.0

        for row in range(self.initial_limit):
            self.build_b_and_c_matrix(row)

            for left_lower_col in range(row):
                if self.b[row, left_lower_col] != 0:
                    divider = -self.b[row][left_lower_col]
                    for inner_col in range(left_lower_col, row):
                        self.b[row][inner_col] += self.b[left_lower_col][inner_col] * divider
                    self.f[row] += self.f[left_lower_col] * divider

            self.y[row] = self.f[row] / self.b[row, row]

        print('after initial limit:')
        print(f'b:\n{self.b}')
        print(f'c:\n{self.c}')
        print(f'y:\n{self.y}')
        print(f'f:\n{self.f}')

        for row in range(self.initial_limit, self.limit):
            self.build_b_and_c_matrix(row)

            for left_lower_col in range(row):
                if self.b[row, left_lower_col] != 0:
                    divider = -self.b[row][left_lower_col]
                    for inner_col in range(left_lower_col, row):
                        self.b[row][inner_col] += self.b[left_lower_col][inner_col] * divider
                    self.f[row] += self.f[left_lower_col] * divider

            self.y[row] = self.f[row] / self.b[row, row]

            # work with self.c moving row by row starting with last_row to 0

            print(f'iterate coords, row: {row}')
            for cur_row in range(row - 1, -1, -1):
                prev_f_row = 0.0
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
                        self.make_cell_one(cur_row, cur_col, row)
                        calculated_this_step = True
                    else:
                        if self.c[cur_row, cur_col] == 0:  # opt
                            print()
                            continue
                        self.calculate_cell(cur_row, cur_col, row)
                        calculated_this_step = True

                    if calculated_this_step:
                        prev_f_row = cur_f_row
                        cur_f_row = self.f[cur_row]
                        d = abs(cur_f_row - prev_f_row)

                    print(
                        f'c before: {initial_c_value} c after: {self.c[cur_row, cur_col]}')
                    print(f'calculated this step: {calculated_this_step}')
                    if (calculated_this_step):
                        print(f'd: {d}')

        Time_logger.get_instance().mark_timestamp_for_event('SCR matrix division')

        print(f'b:\n{self.b}')
        print(f'c:\n{self.c}')
        print(f'y:\n{self.y}')
        print(f'f:\n{self.f}')
