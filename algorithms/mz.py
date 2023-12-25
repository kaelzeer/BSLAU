from utils import Utils, Constants
from algorithms.base_alg import Algorithm

import numpy as np


class Zeidel(Algorithm):

    def __init__(self, matrix_num: int = 1) -> None:

        super().__init__(matrix_num)
        self.alg_type = Constants.ALG_TYPE_MZ
        super().post_init()

        self.xss = np.zeros(self.limit)
        self.xs = np.zeros(self.limit)

    def solve(self):

        s = 0.0
        d = 0.0
        x0 = 0.0

        n = 3
        self.steps = 3

        while True:

            self.steps += 1
            self.xss = np.array(self.xs)

            while True:

                d = 0.0
                for i in range(n):
                    s = 0.0
                    for j in range(n):
                        if i != j:
                            s += self.a[i][j] * self.xs[j]
                    x0 = self.xs[i]
                    self.xs[i] = (self.f[i] - s) / self.a[i][i]
                    d2 = abs(x0 - self.xs[i])
                    d = max(d, d2)
                # do-while emul condition
                if d < Utils.get_first_d(self):
                    print(f'n: {n}, d: {d}')
                    break

            d = 0.0
            for i in range(n):
                d = max(d, abs(self.xs[i] - self.xss[i]))
            n += 1
            if d < 0.0012:
                print(f'n: {self.n}, DD: {d}')

            # do-while emul condition
            if not self.solve_to_n_answer:
                if d < Utils.get_second_d(self):
                    break
            else:
                if d < Utils.get_second_d(self) and n > 13:
                    break
            if n >= self.limit:
                break
