from utils import Utils
import math
from helpers.time_logger import Time_logger
import numpy as np


def prac_matrix_alpha(i: int) -> float:
    temp = i * np.pi
    sss = temp * (temp + np.sinh(temp)) / (16 * (np.cosh(temp / 2) ** 2))
    return sss


class NMatrix_builder:

    @staticmethod
    def build_matrix(algorithm) -> None:

        Time_logger.get_instance().start_timer_for_event("matrix_creation")

        if algorithm.matrix_num == 1:
            NMatrix_builder.build_first_matrix(algorithm)
        elif algorithm.matrix_num == 2:
            NMatrix_builder.build_second_matrix(algorithm)
        elif algorithm.matrix_num == 3:
            NMatrix_builder.build_third_matrix(algorithm)
        elif algorithm.matrix_num == 4:
            NMatrix_builder.build_prac_matrix(algorithm)

        Time_logger.get_instance().mark_timestamp_for_event("matrix_creation")

    @staticmethod
    def build_first_matrix(algorithm, matmul: bool = True) -> None:

        algorithm.f = np.zeros(algorithm.limit)
        algorithm.a = np.zeros((algorithm.limit, algorithm.limit), np.double)

        for j in range(algorithm.limit):
            for p in range(algorithm.limit - j):
                bottom_part = math.factorial(j + p + 1)
                algorithm.a[j, j+p] = 1 / bottom_part
            algorithm.f[j] = algorithm.b0 ** j / ((1 - algorithm.b0) ** 2)
            if j != 0:
                algorithm.f[j] += algorithm.f[j - 1]

        print('Original matrix:')
        Utils.print_mat(algorithm.a, algorithm.f, 6, 6)
        if matmul:
            lower_triangle_mat = np.zeros((algorithm.limit, algorithm.limit))

            for i in range(algorithm.limit):
                for j in range(algorithm.limit):
                    if i >= j:
                        lower_triangle_mat[i, j] = 1

            print('lower triangle matrix:')
            Utils.print_mat(lower_triangle_mat, algorithm.f)
            algorithm.a = np.matmul(lower_triangle_mat, algorithm.a)

        print('lower_triangle * matrix:')
        Utils.print_mat(algorithm.a, algorithm.f)

    @staticmethod
    def build_second_matrix(algorithm, matmul: bool = True) -> None:

        algorithm.f = np.zeros(algorithm.limit)
        algorithm.a = np.zeros((algorithm.limit, algorithm.limit), np.double)

        for j in range(algorithm.limit):
            for p in range(algorithm.limit - j):
                algorithm.a[j, j+p] = 1
            algorithm.f[j] = algorithm.b0 ** j / ((1 - algorithm.b0) ** 2)
            if j != 0:
                algorithm.f[j] += algorithm.f[j - 1]

        print('Original matrix:')
        Utils.print_mat(algorithm.a, algorithm.f, 6, 6)
        if matmul:
            lower_triangle_mat = np.zeros((algorithm.limit, algorithm.limit))

            for i in range(algorithm.limit):
                for j in range(algorithm.limit):
                    if i >= j:
                        lower_triangle_mat[i, j] = 1

            print('lower triangle matrix:')
            Utils.print_mat(lower_triangle_mat, algorithm.f)
            algorithm.a = np.matmul(lower_triangle_mat, algorithm.a)

        print('lower_triangle * matrix:')
        Utils.print_mat(algorithm.a, algorithm.f)

    @staticmethod
    def build_third_matrix(algorithm, matmul: bool = True) -> None:

        algorithm.f = np.zeros(algorithm.limit)
        algorithm.a = np.zeros(
            (algorithm.limit, algorithm.limit), np.longdouble)

        bj = 1
        a = 1
        for j in range(algorithm.limit):
            algorithm.f[j] = bj
            bj = bj * algorithm.b0
            if j > 0:
                a = a * (2 * j - 1) * (2 * j)
            algorithm.a[j, j] = a
            ap = a
            for p in range(1, algorithm.limit - j):
                ap = ap * (2 * j + 2 * p - 1) * (2 * j + 2 * p) / \
                    ((2 * p - 1) * (2 * p))
                algorithm.a[j, j+p] = ap
                algorithm.f[j] = algorithm.b0 ** j
                if j != 0:
                    algorithm.f[j] += algorithm.f[j - 1]

        print('Original matrix:')
        Utils.print_mat(algorithm.a, algorithm.f, 6, 6)
        if matmul:
            lower_triangle_mat = np.zeros((algorithm.limit, algorithm.limit))

            for i in range(algorithm.limit):
                for j in range(algorithm.limit):
                    if i >= j:
                        lower_triangle_mat[i, j] = 1

            print('lower triangle matrix:')
            Utils.print_mat(lower_triangle_mat, algorithm.f)
            algorithm.a = np.matmul(lower_triangle_mat, algorithm.a)

        print('lower_triangle * matrix:')
        Utils.print_mat(algorithm.a, algorithm.f)

    @staticmethod
    def build_prac_matrix(algorithm) -> None:

        algorithm.f = np.zeros(algorithm.limit)
        algorithm.a = np.zeros((algorithm.limit, algorithm.limit), np.double)

        for i in range(algorithm.limit):
            for j in range(algorithm.limit):
                algorithm.a[i, j] = pow(pow(
                    2*(i+1)-1, 2)/(pow(2*(i+1)-1, 2)+pow(2*(j+1)-1, 2)), 2)*math.sin((2*(j+1)-1)*math.pi/2)
            algorithm.f[i] = 1
            algorithm.a[i, i] = algorithm.a[i, i] + \
                prac_matrix_alpha(2*(i+1)-1)*math.sin((2*(i+1)-1)*math.pi/2)

        print('Original matrix:')
        Utils.print_mat(algorithm.a, algorithm.f, 6, 6)
