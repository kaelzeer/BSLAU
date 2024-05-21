from utils import Utils, Constants
import math
from helpers.time_logger import Time_logger
import numpy as np
from io import TextIOWrapper


class Solve_builder:

    @staticmethod
    def build_solution(algorithm, calc_na_last_answer: bool = False, output: TextIOWrapper = None) -> None:
        if algorithm.matrix_num == 1:
            Solve_builder.build_gaussian_example_first_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, calc_na_last_answer, output)
        elif algorithm.matrix_num == 2:
            Solve_builder.build_gaussian_example_second_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, calc_na_last_answer, output)
        elif algorithm.matrix_num == 3:
            Solve_builder.build_full_example_first_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, calc_na_last_answer, output)
        elif algorithm.matrix_num == 4:
            Solve_builder.build_full_example_second_solution(
                algorithm.answers, algorithm.answers_length, algorithm.a0, algorithm.b0, calc_na_last_answer, output)
        elif algorithm.matrix_num == 5:
            Solve_builder.build_prac_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)
        elif algorithm.matrix_num == 6:
            Solve_builder.build_homogeneous_first_solution(
                algorithm.answers, algorithm.answers_length, algorithm.b0, output)

    @staticmethod
    def build_gaussian_example_first_solution(answer: np.array, limit: int, b: float, calc_na_last_answer: bool = False, output: TextIOWrapper = None) -> None:
        for j in range(limit):
            answer[j] = (b ** j) / (math.factorial(2 * j + 1)
                                    * Utils.ch(limit, math.sqrt(b)))

        Utils.print_answers(answer, 'Original answers:', -1,
                            Constants.PRINT_FLOAT_PRECISION, output)

        if calc_na_last_answer:
            na_last_answer = np.zeros(1)
            j = Constants.LAST_ANSWER_INDEX
            na_last_answer[0] = (b ** j) / (math.factorial(2 * j + 1)
                                            * Utils.ch(limit, math.sqrt(b)))
            Utils.print_answers(na_last_answer, f'Original answers[{j}]:', -1,
                                Constants.PRINT_FLOAT_PRECISION, output)

    @staticmethod
    def build_gaussian_example_second_solution(answer: np.array, limit: int, b: float, calc_na_last_answer: bool = False, output: TextIOWrapper = None) -> None:
        for j in range(limit):
            answer[j] = (b ** j) / (1 - b)

        Utils.print_answers(answer, 'Original answers:', -1,
                            Constants.PRINT_FLOAT_PRECISION, output)

        if calc_na_last_answer:
            na_last_answer = np.zeros(1)
            j = Constants.LAST_ANSWER_INDEX
            na_last_answer[0] = (b ** j) / (1 - b)
            Utils.print_answers(na_last_answer, f'Original answers[{j}]:', -1,
                                Constants.PRINT_FLOAT_PRECISION, output)

    @staticmethod
    def build_full_example_first_solution(answer: np.array, limit: int, b: float, calc_na_last_answer: bool = False, output: TextIOWrapper = None) -> None:
        _bi = 1
        for i in range(limit):
            answer[i] = _bi / (1 - b)
            _bi = _bi * b

        Utils.print_answers(answer, 'Original answers:', -1,
                            Constants.PRINT_FLOAT_PRECISION, output)

        if calc_na_last_answer:
            na_last_answer = np.zeros(1)
            j = Constants.LAST_ANSWER_INDEX
            na_last_answer[0] = b**j/(1 - b)
            Utils.print_answers(na_last_answer, f'Original answers[{j}]:', -1,
                                Constants.PRINT_FLOAT_PRECISION, output)

    @staticmethod
    def build_full_example_second_solution(answer: np.array, limit: int, a: float, b: float, calc_na_last_answer: bool = False, output: TextIOWrapper = None) -> None:
        _bi = 1
        for i in range(limit):
            answer[i] = _bi / (1 + a*b)
            _bi = _bi * b

        Utils.print_answers(answer, 'Original answers:', -1,
                            Constants.PRINT_FLOAT_PRECISION, output)
        if calc_na_last_answer:
            na_last_answer = np.zeros(1)
            j = Constants.LAST_ANSWER_INDEX
            na_last_answer[0] = (b ** j) / (1 + a * b)
            Utils.print_answers(na_last_answer, f'Original answers[{j}]:', -1,
                                Constants.PRINT_FLOAT_PRECISION, output)

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

        Utils.print_answers(answer, 'Original answers:', -1,
                            Constants.PRINT_FLOAT_PRECISION, output)

    @staticmethod
    def build_homogeneous_first_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        for i in range(limit):
            answer[i] = ((-1) ** i) * (np.pi ** (2 * i)) / \
                (math.factorial(2 * i) * 2 ** (2 * i))

        Utils.print_answers(answer, 'Original answers:', -1,
                            Constants.PRINT_FLOAT_PRECISION, output)

    # old
    @staticmethod
    def build_old_first_solution(answer: np.array, limit: int, b: float, output: TextIOWrapper) -> None:
        for j in range(limit):
            answer[j] = (math.factorial(j + 1) * b ** j) / (1 - b)

        Utils.print_answers(answer, 'Original answers:', -1,
                            Constants.PRINT_FLOAT_PRECISION, output)
