from utils import Utils, Constants
from algorithms.base_alg import Algorithm
from time_logger import Time_logger

import numpy as np


class LUGJ(Algorithm):
    def __init__(self, matrix_num: int = 1) -> None:

        super().__init__(matrix_num)
        self.alg_type = Constants.ALG_TYPE_NSCR
        super().post_init()

        self.b = np.zeros((self.limit, self.limit), np.double)
        self.c = np.zeros((self.limit, self.limit), np.double)

        self.y = np.zeros(self.limit)
        self.x = np.zeros(self.limit)

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

        # print(f'b:\n')
        # for i in range(10):
        #     for j in range(10):
        #         print(self.b[i, j], end=' ')
        #     print()
        # print(f'b:\n')

        # print(f'c:\n')
        # for i in range(10):
        #     for j in range(10):
        #         print(self.c[i, j], end=' ')
        #     print()
        # print(f'c:\n')

    def solve(self):

        Time_logger.get_instance().start_timer_for_event('SCR matrix division')

        c_cur_row = 0
        c_cur_col = 1
        self.c_delta = np.zeros(self.limit)

        for row in range(self.limit):
            self.build_b_and_c_matrix(row)

            for left_lower_col in range(row):
                if self.b[row, left_lower_col] != 0:
                    divider = -self.b[row][left_lower_col]
                    for inner_col in range(left_lower_col, row):
                        self.b[row][inner_col] += self.b[left_lower_col][inner_col] * divider
                    self.f[row] += self.f[left_lower_col] * divider

            for right_upper_col in range(c_cur_row + 1, row):

            self.y[row] = self.f[row] / self.b[row, row]
        Time_logger.get_instance().mark_timestamp_for_event('SCR matrix division')

        print(f'b:\n {self.b}')
        print(f'c:\n {self.c}')
        print(f'y:\n {self.y}')
        print(f'f:\n {self.f}')
