from utils import Utils, Constants
from algorithms.base_alg import Algorithm
import math

import numpy as np


class MPP(Algorithm):

    def __init__(self, matrix_num: int = 1) -> None:

        super().__init__(matrix_num)
        self.alg_type = Constants.ALG_TYPE_MPP
        super().post_init()

        self.x = np.zeros(self.limit)
        self.xs = np.zeros(self.limit)
        self.xss = np.zeros(self.limit)
        self.n = 0

    def solve(self):

        self.n = 3
        d = 0.0
        s = 0.0
        inner_steps = 0

        while True:
            self.steps += 1
            self.xss = np.array(self.xs)

            while True:
                inner_steps += 1
                self.x = np.array(self.xs)
                for i in range(self.n):
                    s = 0.0
                    for j in range(self.n):
                        if i != j:
                            s += self.a[i][j] * self.x[j]
                            if math.isinf(s):
                                todo = True
                    self.xs[i] = (self.f[i] - s) / self.a[i][i]
                d = 0.0
                for i in range(self.n):
                    d = max(d, abs(self.x[i] - self.xs[i]))
                # do-while-emu exit condition
                if d < Utils.get_first_d(self):
                    print(f'n: {self.n}, d: {d}')
                    break

            dd = 0.0
            for i in range(self.n - 1):
                dd = max(dd, abs(self.xs[i] - self.xss[i]))
            self.n += 1
            if dd < 0.0012:
                print(f'n: {self.n}, DD: {dd}')
            # do-while-emu exit condition
            if not self.solve_to_n_answer:
                if dd < Utils.get_second_d(self):
                    break
            else:
                if dd < Utils.get_second_d(self) and self.n > 13:
                    break
            if self.n >= self.limit:
                break

        print()
        print(f'd: {d}')
        print(f'n: {self.n}')
