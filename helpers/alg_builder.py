from algorithms.base_alg import Algorithm
from algorithms.gj import GaussJordanoAlg
from algorithms.mpp import MPP
from algorithms.mz import Zeidel
from algorithms.new_alg import NA
from algorithms.recursion_method import RM
from algorithms.scr import SCR


class Algorithm_builder:

    @staticmethod
    def get_alg(alg_type: str, matrix_num: int, change_to_recursion_method: bool) -> Algorithm:
        if alg_type == 'BASE':
            return Algorithm(matrix_num)
        elif alg_type == 'MPP':
            if change_to_recursion_method and matrix_num < 3:
                return RM(matrix_num)
            return MPP(matrix_num)
        elif alg_type == 'MZ':
            if change_to_recursion_method and matrix_num < 3:
                return RM(matrix_num)
            return Zeidel(matrix_num)
        elif alg_type == 'GJ':
            return GaussJordanoAlg(matrix_num)
        elif alg_type == 'SCR':
            return SCR(matrix_num)
        elif alg_type == 'NA':
            return NA(matrix_num)
