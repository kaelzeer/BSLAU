from algorithms.mpp import MPP

from time_logger import Time_logger
from utils import Utils, Constants

from matrix_builder import Matrix_builder

import numpy as np
import math


def custom_formatter(x):
    return f"{x:.20f}"  # only for matrix 8
    return f"{x:.10f}"  # for other matrixes


np.set_printoptions(formatter={'float': custom_formatter})

'''
Matrix choice
'''
# matrix_num = 1
# print(f'Matrix {matrix_num}')
# alg = MPP(matrix_num)
# Matrix_builder.build_first_matrix(alg)
# print()

# matrix_num = 2
# print(f'Matrix {matrix_num}')
# alg = MPP(matrix_num)
# Matrix_builder.build_second_matrix(alg)
# print()

# matrix_num = 3
# print(f'Matrix {matrix_num}')
# alg = MPP(matrix_num)
# Matrix_builder.build_third_matrix(alg)
# print()

# Mukhin-4.pdf
matrix_num = 5
print(f'Matrix {matrix_num}')
alg = MPP(matrix_num)
Matrix_builder.build_prac_matrix(alg)
print()

# Mukhin.pdf
# matrix_num = 6
# print(f'Matrix {matrix_num}')
# alg = MPP(matrix_num)
# Matrix_builder.build_re_first_matrix(alg)
# print()
# answers = np.zeros(alg.limit)
# for j in range(alg.limit):
# 	upper_part = math.factorial(j + 1) * (alg.b0 ** j)
# 	lower_part = 1 - alg.b0
# 	answers[j] = upper_part / lower_part
# print(f'answers: {answers}')

# Mukhin-2.pdf
# matrix_num = 7
# print(f'Matrix {matrix_num}')
# alg = MPP(matrix_num)
# Matrix_builder.build_re_second_matrix(alg)
# print()
# answers = np.zeros(alg.limit)
# for j in range(alg.limit):
# 	upper_part = alg.b0 ** j
# 	lower_part = 1 - alg.b0
# 	answers[j] = upper_part / lower_part
# print(f'answers: {answers}')

# Mukhin-3.pdf
# matrix_num = 8
# print(f'Matrix {matrix_num}')
# alg = MPP(matrix_num)
# Matrix_builder.build_re_third_matrix(alg)
# print()
# answers = np.zeros(alg.limit)
# for j in range(alg.limit):
# 	upper_part = alg.b0 ** j
# 	lower_part = math.factorial(2 * j + 1) * np.cosh(math.sqrt(alg.b0))
# 	answers[j] = upper_part / lower_part
# print(f'answers: {answers}')
