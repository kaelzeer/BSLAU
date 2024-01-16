from utils import Utils, Constants
from algorithms.base_alg import Algorithm
from time_logger import Time_logger

import numpy as np

np.set_printoptions(precision=8, suppress=True)


class LUGJP(Algorithm):
    def __init__(self, matrix_num: int = 1) -> None:

        super().__init__(matrix_num)
        self.alg_type = Constants.ALG_TYPE_LUGJ
        super().post_init()

        self.b_orig = np.zeros((self.limit, self.limit), np.double)
        self.c_orig = np.zeros((self.limit, self.limit), np.double)

        self.b = np.zeros((self.limit, self.limit), np.double)
        self.c = np.zeros((self.limit, self.limit), np.double)

        self.y = np.zeros(self.limit)
        self.f_orig = np.ones(self.limit)

        self.initial_limit = 10

    def make_cell_one(self, matrix: np.array, answers_vec: np.array, cell_row: int, cell_col: int, last_col: int = -1):

        divider = matrix[cell_row][cell_col]
        if cell_row != cell_col or divider == 1:
            return

        if last_col == -1:
            last_col = self.limit if cell_col < Utils.NMAX else Utils.NMAX
        if divider == 0:
            non_zero_element_index = self.get_first_non_zero_col(
                cell_row, cell_col + 1)
            matrix[cell_row], matrix[non_zero_element_index] = matrix[non_zero_element_index], matrix[cell_row]
            divider = matrix[cell_row][cell_col]

        elif divider != 1:
            for col in range(cell_col, last_col):
                matrix[cell_row][col] /= divider
            answers_vec[cell_row] /= divider
        # self.steps_for_print_step += 1
        # Utils.print_step(self.steps_for_print_step, matrix, answers_vec, cell_row, cell_col, False)

    def calculate_cell(self, matrix: np.array, answers_vec: np.array, cell_row: int, cell_col: int, last_col: int = -1):

        if cell_row == cell_col or matrix[cell_col][cell_col] != 1.0:
            self.make_cell_one(matrix, answers_vec,
                               cell_col, cell_col, last_col)

        if last_col == -1:
            last_col = self.limit if cell_col < Utils.NMAX else Utils.NMAX
        if matrix[cell_row][cell_col] != 0:
            divider = -matrix[cell_row][cell_col]
            for col in range(cell_col, last_col):
                matrix[cell_row][col] += matrix[cell_col][col] * divider
            answers_vec[cell_row] += self.f[cell_col] * divider

    def get_first_non_zero_col(self, row: int, first_col: int) -> int:

        last_col = self.limit
        for col in range(first_col, last_col):
            if self.a[row][col] != 0:
                return col
        return -1

    def build_b_and_c_matrix(self, n: int) -> None:

        for i in range(n):
            sum_b_c_i = 0
            for k in range(i):
                sum_b_c_i += self.b[i, k] * self.c_orig[k, n]
            self.c_orig[i, n] = self.a[i, n] - sum_b_c_i

        for j in range(n):
            sum_b_c_j = 0
            for k in range(j):
                sum_b_c_j += self.b[n, k] * self.c_orig[k, j]
            self.b[n, j] = (self.a[n, j] - sum_b_c_j) / self.c_orig[j, j]

        sum_b_c_n = 0
        for k in range(n):
            sum_b_c_n += self.b[n, k] * self.c_orig[k, n]
        self.c_orig[n, n] = self.a[n, n] - sum_b_c_n
        self.b[n, n] = (self.a[n, n] - sum_b_c_n) / self.c_orig[n, n]
        self.c[n, n] = self.c_orig[n, n]

        for i in range(n):
            self.c[i, n] = self.c_orig[i, n]

    def calculate_y_using_podstanovka(self, row):

        s = 0
        for left_lower_col in range(row):
            s += self.b[row][left_lower_col] * self.y[left_lower_col]
        self.y[row] = (self.f[row] - s) / self.b[row][row]

    def solve(self):

        Time_logger.get_instance().start_timer_for_event('SCR matrix division')

        self.c_delta = np.zeros(self.limit)
        d = 1.0
        row = 0

        while True:
            print(f'solve: row: {row}')
            # self.build_b_and_c_matrix_without_orig(row)
            self.build_b_and_c_matrix(row)

            self.calculate_y_using_podstanovka(row)

            # work with self.c moving row by row starting with last_row to 0

            # print(f'iterate coords, row: {row}')
            for cur_row in range(row - 1, -1, -1):
                prev_f_row = -1.0
                cur_f_row = self.f[cur_row]
                for cur_col in range(cur_row, row):
                    calculated_this_step = False
                    # print(
                    #     f'cur_row, cur_col : {cur_row}, {cur_col}, ', end='')
                    initial_c_value = self.c[cur_row, cur_col]

                    if cur_row == cur_col:  # on main diagonal
                        if self.c[cur_row, cur_col] == 1:  # opt
                            # print()
                            continue
                        # for it_col in range(cur_row, row):  # self.limit ?
                        self.make_cell_one(
                            self.c, self.f, cur_row, cur_col, -1)
                        calculated_this_step = True
                    else:
                        if self.c[cur_row, cur_col] == 0:  # opt
                            # print()
                            continue
                        self.calculate_cell(
                            self.c, self.f, cur_row, cur_col, -1)
                        calculated_this_step = True

                    if calculated_this_step:
                        prev_f_row = cur_f_row
                        cur_f_row = self.f[cur_row]
                        d = abs(cur_f_row - prev_f_row)

                    # print(
                    #     f'c before: {initial_c_value} c after: {self.c[cur_row, cur_col]}')
                    # print(f'calculated this step: {calculated_this_step}')
                    # if (calculated_this_step):
                    #     print(f'd: {d}')

            # print(f'{row} c\n')
            # for i in range(10):
            #     for j in range(10):
            #         print(f'{self.c[i, j]} ', end='')
            #     print()

            row += 1

            # do-while-emu exit condition
            if d < 1e-10 or row > self.limit:  # todo: move d to utils
                break

        Time_logger.get_instance().mark_timestamp_for_event('SCR matrix division')

        print(f'b:\n{self.b}')
        print(f'c:\n{self.c}')
        print(f'y:\n{self.y}')
        print(f'f:\n{self.f}')
