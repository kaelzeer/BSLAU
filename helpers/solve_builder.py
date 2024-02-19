from utils import Utils
import math
from helpers.time_logger import Time_logger
import numpy as np
from io import TextIOWrapper


class Solve_builder:

    @staticmethod
    def build_solution(algorithm, output: TextIOWrapper) -> None:
        if algorithm.matrix_num == 1:
            Solve_builder.build_gaussian_example_first_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)
        elif algorithm.matrix_num == 2:
            Solve_builder.build_gaussian_example_second_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)
        elif algorithm.matrix_num == 3:
            Solve_builder.build_full_example_first_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)
        elif algorithm.matrix_num == 4:
            Solve_builder.build_full_example_second_solution(
                algorithm.answers, algorithm.answers_length, algorithm.a0, algorithm.b0, output)
        elif algorithm.matrix_num == 5:
            Solve_builder.build_prac_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)

    @staticmethod
    def build_gaussian_example_first_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        for j in range(limit):
            answer[j] = (b ** j) / (math.factorial(2 * j + 1)
                                    * Utils.ch(limit, math.sqrt(b)))

        Utils.print_answers(answer, 'Original answers:', -1, False, output)
        Utils.print_answers(answer, 'Original answers:', -1, True, output)

    @staticmethod
    def build_gaussian_example_second_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        for j in range(limit):
            answer[j] = (b ** j) / (1 - b)

        Utils.print_answers(answer, 'Original answers:', -1, False, output)
        Utils.print_answers(answer, 'Original answers:', -1, True, output)

    @staticmethod
    def build_full_example_first_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        bi = 1
        for i in range(limit):
            answer[i] = bi / (1 - b)
            bi = bi * b

        # i = 100
        # print(i, b**i/(1 - b))

        Utils.print_answers(answer, 'Original answers:', -1, False, output)
        Utils.print_answers(answer, 'Original answers:', -1, True, output)

    # todo
    @staticmethod
    def build_full_example_second_solution(answer: np.array, limit: int, a: float, b: float, output: TextIOWrapper) -> None:
        bi = 1
        for i in range(limit):
            answer[i] = bi / (1 + a*b)
            bi = bi * b

        # i = 100
        # print(i, b**i/(1 - b))

        Utils.print_answers(answer, 'Original answers:', -1, False, output)
        Utils.print_answers(answer, 'Original answers:', -1, True, output)

    @staticmethod
    def build_prac_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        answer[0] = 1.4138
        answer[1] = 0.0945
        answer[2] = -0.1093
        answer[3] = 0.0770
        answer[4] = -0.0510
        answer[5] = 0.0371
        answer[6] = -0.0264
        answer[7] = 0.0193
        answer[8] = -0.0141
        answer[9] = 0.0103

        Utils.print_answers(answer, 'Original answers:', -1, False, output)
        Utils.print_answers(answer, 'Original answers:', -1, True, output)

    # old
    @staticmethod
    def build_old_first_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        for j in range(limit):
            answer[j] = (math.factorial(j + 1) * b ** j) / (1 - b)

        Utils.print_answers(answer, 'Original answers:', -1, False, output)
        Utils.print_answers(answer, 'Original answers:', -1, True, output)
