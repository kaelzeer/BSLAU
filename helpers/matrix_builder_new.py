import math
from helpers.time_logger import Time_logger
import numpy as np
from utils import Utils


def _prac_matrix_alpha(i: int) -> float:
    temp = i * np.pi
    sss = temp * (temp + np.sinh(temp)) / (16 * (np.cosh(temp / 2) ** 2))
    return sss


class NMatrix_builder:

    @staticmethod
    def build_matrix(algorithm) -> None:
        Time_logger.get_instance().start_timer_for_event("matrix_creation")

        if algorithm.matrix_num == 1:
            NMatrix_builder.build_gaussian_example_first(algorithm)
        elif algorithm.matrix_num == 2:
            NMatrix_builder.build_gaussian_example_second(algorithm)
        elif algorithm.matrix_num == 3:
            NMatrix_builder.build_full_example_first(algorithm)
        elif algorithm.matrix_num == 4:
            NMatrix_builder.build_full_example_first(algorithm)
        elif algorithm.matrix_num == 5:
            NMatrix_builder.build_prac_matrix(algorithm)

        Time_logger.get_instance().mark_timestamp_for_event("matrix_creation")

    @staticmethod
    def build_gaussian_example_first(algorithm) -> None:
        _is_gauss_matrix = True
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

        Utils.print_matrix_type_and_number(algorithm)
        Utils.print_mat(algorithm.a, algorithm.f)

    @staticmethod
    def build_gaussian_example_second(algorithm) -> None:
        _is_gauss_matrix = True
        algorithm.f = np.zeros(algorithm.limit)
        algorithm.a = np.zeros((algorithm.limit, algorithm.limit), np.double)

        for j in range(algorithm.limit):
            for p in range(algorithm.limit - j):
                algorithm.a[j, j+p] = 1
            algorithm.f[j] = algorithm.b0 ** j / ((1 - algorithm.b0) ** 2)

    @staticmethod
    def build_full_example_first(algorithm) -> None:
        _is_gauss_matrix = False
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

        bi = 1
        s = 0
        for i in range(algorithm.limit):
            s = s + bi
            algorithm.f[i] = s / (1 - algorithm.b0) ** 2
            for j in range(0, algorithm.limit):
                if i >= j:
                    algorithm.a[i, j] = j + 1
                else:
                    algorithm.a[i, j] = i + 1
            bi = bi * algorithm.b0

    @staticmethod
    def build_prac_matrix(algorithm) -> None:
        _is_gauss_matrix = False
        algorithm.f = np.zeros(algorithm.limit)
        algorithm.a = np.zeros((algorithm.limit, algorithm.limit), np.double)

        for i in range(algorithm.limit):
            for j in range(algorithm.limit):
                algorithm.a[i, j] = pow(pow(
                    2*(i+1)-1, 2)/(pow(2*(i+1)-1, 2)+pow(2*(j+1)-1, 2)), 2)*math.sin((2*(j+1)-1)*math.pi/2)
            algorithm.f[i] = 1
            algorithm.a[i, i] = algorithm.a[i, i] + \
                _prac_matrix_alpha(2*(i+1)-1)*math.sin((2*(i+1)-1)*math.pi/2)

    @staticmethod
    def build_old_first_matrix(algorithm) -> None:
        _is_gauss_matrix = True
        algorithm.f = np.zeros(algorithm.limit)
        algorithm.a = np.zeros((algorithm.limit, algorithm.limit), np.double)

        for j in range(algorithm.limit):
            for p in range(algorithm.limit - j):
                bottom_part = math.factorial(j + p + 1)
                algorithm.a[j, j+p] = 1 / bottom_part
            algorithm.f[j] = algorithm.b0 ** j / ((1 - algorithm.b0) ** 2)
