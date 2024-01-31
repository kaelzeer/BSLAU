from utils import Utils, Constants
from algorithms.base_alg import Algorithm
from helpers.time_logger import Time_logger

import numpy as np
# from scipy.linalg import lu


class SCR(Algorithm):
    def __init__(self, matrix_num: int = 1) -> None:

        super().__init__(matrix_num)
        self.alg_type = Constants.ALG_TYPE_SCR
        super().post_init()

        self.b = np.zeros((self.limit, self.limit), np.double)
        self.c = np.zeros((self.limit, self.limit), np.double)

        # from lu()
        # self.b1 = np.zeros((self.limit,self.limit),np.double)
        # self.c1 = np.zeros((self.limit,self.limit),np.double)

        Time_logger.get_instance().start_timer_for_event('SCR matrix division')
        self.build_triangle_matrix()
        Time_logger.get_instance().mark_timestamp_for_event('SCR matrix division')

        self.y = np.zeros(self.limit)
        self.x = np.zeros(self.limit)

    def build_triangle_matrix(self):

        # p1, self.b1, self.c1 = lu(self.a)
        # ldu = np.matmul(self.b1,self.c1)

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

        print(f'b:\n')
        for i in range(10):
            for j in range(10):
                print(self.b[i, j], end=' ')
            print()
        print(f'b:\n')

        print(f'c:\n')
        for i in range(10):
            for j in range(10):
                print(self.c[i, j], end=' ')
            print()
        print(f'c:\n')

        # bc = np.matmul(self.b, self.c)

        # print(f'bc:\n')
        # for i in range(10):
        # 	for j in range(10):
        # 		print(bc[i,j], end=' ')
        # 	print()
        # print(f'bc:\n')

    def solve(self):

        sign_p = -1
        sign_p_k = -1
        # y = np.array(self.f)
        y = np.zeros(self.limit)
        maxjp = 0
        j = 0
        A = np.zeros(self.limit)

        while True:
            self.steps += 1
            self.xss = np.array(self.x)
            A[0] = 1
            p = 0
            # repeat
            while True:
                if p > 0:
                    A[p] = 0
                if p % 2 != 0:
                    sign_p = -1
                else:
                    sign_p = 1

                sum_b_y_k = 0
                if j + p == self.limit:
                    todo = True
                for k in range(0, j+p):
                    sum_b_y_k += self.b[j+p, k] * y[k]
                y[j+p] = (self.f[j+p] - sum_b_y_k) / self.b[j+p, j+p]

                for k in range(p):  # necessary inclusive step
                    if (p - 1 - k) % 2 != 0:
                        sign_p_k = -1
                    else:
                        sign_p_k = 1
                    A[p] += sign_p_k * self.c[j+k, j+p] / \
                        self.c[j+k, j+k] * A[k]
                xs = self.x[j]
                self.x[j] = xs + sign_p * A[p] * y[j+p] / self.c[j+p, j+p]
                # self.x[j] = xs + sign_p * A[p] * self.y[j+p] / self.c[j+p,j+p]
                r = abs(xs - self.x[j])
                p += 1
                if maxjp < j + p:
                    maxjp = j + p
                print(f'n: {j}, d: {r}')
                # until
                if (r < Utils.get_first_d(self)) or (j + p >= self.limit):
                    break

            dd = 0.0
            for i in range(j + 1):
                dd = max(dd, abs(self.x[i] - self.xss[i]))
            # do-while-emu exit condition
            print(f'D: {dd}')
            if not self.solve_to_n_answer:
                if dd < Utils.get_second_d(self):
                    break
            else:
                if dd < Utils.get_second_d(self) and j > 13:
                    break
            if j >= self.limit - 1:
                break
            j += 1

        print()
        print(f'd: {r}')
        print(f'n: {j}')
        print(f'j+p={maxjp}')
