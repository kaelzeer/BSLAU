from utils import Utils, Constants
from algorithms.base_alg import Algorithm
from helpers.time_logger import Time_logger

import numpy as np

np.set_printoptions(precision=8, suppress=True)


class NA(Algorithm):
    def __init__(self, matrix_num: int = 1) -> None:

        super().__init__(matrix_num)
        self.limit = 100
        self.alg_type = Constants.ALG_TYPE_NA
        super().post_init()

        self.b = np.zeros((self.limit, self.limit), np.double)
        self.c = np.zeros((self.limit, self.limit), np.double)

        self.y = np.zeros(self.limit)
        self.x = np.zeros(self.limit)
        self.steps = 0

        self.initial_limit = 10

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

    def calculate_y_using_podstanovka(self):

        for row in range(self.limit):
            s = 0
            for left_lower_col in range(row):
                s += self.b[row][left_lower_col] * self.y[left_lower_col]
            self.y[row] = (self.f[row] - s) / self.b[row][row]

    def presolve(self) -> None:

        Time_logger.get_instance().start_timer_for_event('SCR matrix division')
        self.build_triangle_matrix()
        Time_logger.get_instance().mark_timestamp_for_event('SCR matrix division')

    def solve(self):

        self.calculate_y_using_podstanovka()

        R = np.zeros(self.limit)

        for i in range(self.limit - 1):
            xs = xs0 = 0
            s = self.y[i]
            self.steps = i
            delta = 1.0
            while (delta > Utils.get_first_d(self) or self.steps - i < 3):
                self.steps += 1
                d = self.c[i][self.steps]
                for k in range(i + 1, self.steps):
                    d -= R[k] * self.c[k][self.steps]
                R[self.steps] = d / self.c[self.steps][self.steps]
                s = s - R[self.steps] * self.y[self.steps]
                xs0 = xs
                xs = s / self.c[i][i]
                delta = abs(xs - xs0)
            self.f[i] = xs
            print(f'i: {i}, iter: {self.steps} xs: {xs}, d: {delta}')
            if (delta and delta < Utils.get_first_d(self) and i > self.answers_length) or self.steps == self.limit - 1:
                break

    def solve_at_index(self, i):

        R = np.zeros(self.limit)

        xs = xs0 = 0
        s = self.y[i]
        self.steps = i
        d = 1.0
        while (d > Utils.get_first_d(self) or self.steps - i < 3):
            self.steps += 1
            d = self.c[i][self.steps]
            for k in range(i + 1, self.steps):
                d -= R[k] * self.c[k][self.steps]
            R[self.steps] = d / self.c[self.steps][self.steps]
            s = s - R[self.steps] * self.y[self.steps]
            xs0 = xs
            xs = s / self.c[i][i]
            d = abs(xs - xs0)
        self.f[i] = xs
        print(f'i: {i}, iter: {self.steps} xs: {xs}, d: {d}')
