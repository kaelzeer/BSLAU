from utils import Utils
import math
from helpers.time_logger import Time_logger
import numpy as np
from io import TextIOWrapper


class Solve_builder:

    @staticmethod
    def build_solution(algorithm, output: TextIOWrapper) -> None:
        if algorithm.matrix_num == 1:
            Solve_builder.build_first_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)
        elif algorithm.matrix_num == 2:
            Solve_builder.build_second_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)
        elif algorithm.matrix_num == 3:
            Solve_builder.build_third_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)
        elif algorithm.matrix_num == 4:
            Solve_builder.build_prac_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)

    # @staticmethod
    # def test_build_solution(matrix_num, output: TextIOWrapper) -> None:
    #     answers_length = 10
    #     answers = np.zeros(answers_length)
    #     b0 = 1.5

    #     if matrix_num == 1:
    #         Solve_builder.build_first_solution(
    #             answers, answers_length, b0, output)
    #     elif matrix_num == 2:
    #         Solve_builder.build_second_solution(
    #             answers, answers_length, b0, output)
    #     elif matrix_num == 3:
    #         Solve_builder.build_third_solution(
    #             answers, answers_length, b0, output)
    #     elif matrix_num == 4:
    #         Solve_builder.build_prac_solution(
    #             answers, answers_length, b0, output)

    @staticmethod
    def build_first_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        for j in range(limit):
            answer[j] = (math.factorial(j + 1) * b ** j) / (1 - b)

        print('Original answers:')
        Utils.print_answers(answer, 'Original answers:', -1, False, output)
        Utils.print_answers(answer, 'Original answers:', -1, True, output)

    @staticmethod
    def build_second_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        for j in range(limit):
            answer[j] = (b ** j) / (1 - b)

        print('Original answers:')
        Utils.print_answers(answer, 'Original answers:', -1, False, output)
        Utils.print_answers(answer, 'Original answers:', -1, True, output)

    @staticmethod
    def build_third_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        for j in range(limit):
            answer[j] = (b ** j) / (math.factorial(2 * j + 1)
                                    * Utils.ch(limit, math.sqrt(b)))

        print('Original answers:')
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
