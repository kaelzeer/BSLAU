from io import TextIOWrapper
import math


class Constants:
    '''
    Limits for matrixes
    '''
    BASE_MATRIX_LIMIT = 100
    FACTORIAL_MATRIX_LIMIT = 80
    '''
    Answers array length
    '''
    ANSWERS_COUNT = 10
    LAST_ANSWER_INDEX = 40
    '''
	General matrix **b** koef
	'''
    B0 = 0.25   # variant std
    # B0 = 0.5  # variant 1
    # B0 = 0.75   # variant 2
    '''
    Full matrix 2 **a** koef
    '''
    # B0_FM2 = 0.25  # variant std
    # A0_FM2 = 2    # variant std
    # B0_FM2 = 0.5  # variant 1
    # A0_FM2 = 1   # variant 1
    B0_FM2 = 0.75  # variant 2
    A0_FM2 = 0.67  # variant 2

    '''
	Algoritm type enum
	'''
    ALG_TYPE_BASE = 'BASE'
    ALG_TYPE_MPP = 'MPP'
    ALG_TYPE_MZ = 'MZ'
    ALG_TYPE_GJ = 'GJ'
    ALG_TYPE_SCR = 'SCR'
    ALG_TYPE_NA = 'NA'

    '''
    Print float precision
    '''
    PRINT_FLOAT_PRECISION = 6


class Utils:
    '''
    Project scoped utility methods
    '''
    __print_lim = 10
    NMAX = 5000

    @staticmethod
    def get_matrix_count() -> int:
        return 5

    @staticmethod
    def print_mat(a: list, f: list, forced_n: int = -1, precision: int = -1, output: TextIOWrapper = None):
        '''
        Print matrix method. Project scoped
        '''
        n = 0
        if forced_n != -1:
            n = forced_n
        else:
            if len(a) < Utils.__print_lim:
                n = len(a)
            else:
                n = Utils.__print_lim
        for row in range(n):
            for col in range(n):
                if precision == -1:
                    precision = Constants.PRINT_FLOAT_PRECISION
                print(f'{a[row][col]:.{precision}f} ', end='')
                if output:
                    print(f'{a[row][col]:.{precision}f} ',
                          end='', file=output)
            if precision == -1:
                print(f'|{f[row]}\n\n', end='')
                if output:
                    print(f'|{f[row]}\n\n', end='', file=output)
            else:
                print(f'|{f[row]:.{precision}f}\n\n', end='')
                if output:
                    print(f'|{f[row]:.{precision}f}\n\n',
                          end='', file=output)

    @staticmethod
    def print_matrix_type_and_number(algorithm, output: TextIOWrapper = None):

        print(f'Matrix: {algorithm.matrix_num}')
        if output:
            print(f'Matrix: {algorithm.matrix_num}', file=output)
        if algorithm.matrix_num == 1:
            print('Gaussian matrix example 1')
            if output:
                print('Gaussian matrix example 1', file=output)
        elif algorithm.matrix_num == 2:
            print('Gaussian matrix example 2')
            if output:
                print('Gaussian matrix example 2', file=output)
        elif algorithm.matrix_num == 3:
            print('Gaussian full example 1')
            if output:
                print('Gaussian full example 1', file=output)
        elif algorithm.matrix_num == 4:
            print('Gaussian full example 2')
            if output:
                print('Gaussian full example 2', file=output)
        elif algorithm.matrix_num == 5:
            print('Gaussian full example 3')
            if output:
                print('Gaussian full example 3', file=output)
        print()
        if output:
            print(file=output)

    @staticmethod
    def print_answers(x: list, answers_title_str: str, ss: int, precision: int = 20, output: TextIOWrapper = None):
        '''
        Print answers of system equation. Project scoped
        '''
        if ss != -1:
            print(f's={ss}')
            if output:
                print(f's={ss}', file=output)
        if answers_title_str != '':
            print(answers_title_str)
            if output:
                print(answers_title_str, file=output)
        l = min(len(x), Utils.__print_lim)
        for i in range(l):
            if x[i] > 10 ** -precision:
                print(f'  {x[i]:.{precision}f}')
                if output:
                    print(f'  {x[i]:.{precision}f}', file=output)
            else:
                print(f'  {x[i]:.{precision}e}')
                if output:
                    print(f'  {x[i]:.{precision}e}', file=output)
        print()
        if output:
            print('', file=output)

    @staticmethod
    def get_limit(matrix_num) -> int:
        '''
        Get limit for specific algorithm and matrix. Project scoped
        '''
        # if matrix_num == 1:
        #     return Constants.FIRST_MATRIX_LIMIT
        # elif matrix_num == 2:
        #     return Constants.SECOND_MATRIX_LIMIT
        if matrix_num == 1 or matrix_num == 3 or matrix_num == 6:
            return Constants.FACTORIAL_MATRIX_LIMIT
        # elif matrix_num == 4:
        #     return Constants.FOURTH_MATRIX_LIMIT
        return Constants.BASE_MATRIX_LIMIT

    @staticmethod
    def get_first_d(algorithm) -> float:
        '''
        Get first delta for specific algorithm and matrix. Project scoped
        '''
        return 1e-9

        if algorithm.alg_type == Constants.ALG_TYPE_MPP:
            if algorithm.matrix_num == 4:
                return 0.0025
        elif algorithm.alg_type == Constants.ALG_TYPE_MZ:
            if algorithm.matrix_num == 7:
                return 1e-6
            return 1e-7
        elif algorithm.alg_type == Constants.ALG_TYPE_GJ:
            if algorithm.matrix_num == 3:
                return 1e-5
            return 1e-6
        elif algorithm.alg_type == Constants.ALG_TYPE_SCR:
            # if algorithm.matrix_num == 5:
            #     return 1e-20
            if algorithm.matrix_num == 8:
                return 1e-20
            return 1e-7
        return 1e-7

    @staticmethod
    def get_second_d(algorithm) -> float:
        '''
        Get second delta for specific algorithm and matrix. Project scoped
        '''
        return 1e-4

        if algorithm.alg_type == Constants.ALG_TYPE_MPP:
            return 1e-3
        elif algorithm.alg_type == Constants.ALG_TYPE_MZ:
            return 1e-3
        elif algorithm.alg_type == Constants.ALG_TYPE_GJ:
            pass
        elif algorithm.alg_type == Constants.ALG_TYPE_SCR:
            # if algorithm.matrix_num == 5:
            #     return 1e-8
            if algorithm.matrix_num == 8:
                return 1e-20
            return 1e-3
        return 1e-3

    @staticmethod
    def ch(limit: int, x: float) -> float:
        s = 0
        for j in range(limit):
            s += (x ** (2 * j)) / math.factorial(2 * j)
        return s
