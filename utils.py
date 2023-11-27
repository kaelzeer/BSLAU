from io import TextIOWrapper


class Constants:
    '''
    Limits for matrixes
    '''
    BASE_MATRIX_LIMIT = 50
    FIRST_MATRIX_LIMIT = 800
    SECOND_MATRIX_LIMIT = 70
    THIRD_MATRIX_LIMIT = 800
    FOURTH_MATRIX_LIMIT = 70
    FIFTH_MATRIX_LIMIT = 100
    SIXTH_MATRIX_LIMIT = 40
    '''
	Second matrix **b** koef
	'''
    B0 = 1.5

    '''
	Algoritm type enum
	'''
    ALG_TYPE_BASE = 'BASE'
    ALG_TYPE_MPP = 'MPP'
    ALG_TYPE_MZ = 'MZ'
    ALG_TYPE_GJ = 'GJ'
    ALG_TYPE_SCR = 'SCR'
    ALG_TYPE_NSCR = 'NSCR'


class Utils:
    '''
    Project scoped utility methods
    '''
    __print_lim = 10
    NMAX = 5000

    @staticmethod
    def print_mat(a: list, f: list):
        '''
        Print matrix method. Project scoped
        '''
        n = 0
        if len(a) < Utils.__print_lim:
            n = len(a)
        else:
            n = Utils.__print_lim
        for row in range(n):
            for col in range(n):
                print(f'{a[row][col]} ', end='')
            print(f'|{f[row]}\n\n', end='')

    @staticmethod
    def print_mat_to_file(a: list, f: list, output: TextIOWrapper):
        '''
        Print matrix method. Project scoped
        '''
        n = 0
        if len(a) < Utils.__print_lim:
            n = len(a)
        else:
            n = Utils.__print_lim
        for row in range(n):
            for col in range(n):
                print(f'{a[row][col]} ', end='', file=output)
            print(f'|{f[row]}\n\n', end='', file=output)

    @staticmethod
    def print_answers(x: list, ss: int, to_file: bool, output: TextIOWrapper):
        '''
        Print answers of system equation. Project scoped
        '''
        formatted_x = ['{:.20f}'.format(num) for num in x]

        if to_file:
            print(f's={ss}', file=output)
            for i in range(Utils.__print_lim):
                print(formatted_x[i], end=' ', file=output)
            print('', file=output)
        else:
            print(f's={ss}')
            for i in range(Utils.__print_lim):
                print(formatted_x[i], end=' ')
            print()

    @staticmethod
    def print_step(step: int, a: list, f: list, step_row: int, step_col: int, to_zero: bool):
        '''
        Print step of GJ alg. Project scoped
        '''
        if to_zero:
            print(f'\n{step}. calc cell [{step_row},{step_col}] to zero:\n')
        else:
            print(f'\n{step}. calc cell [{step_row},{step_col}] to one:\n')
        for row in range(Utils.__print_lim):
            for col in range(Utils.__print_lim):
                if row == step_row and col == step_col:
                    print(f'[{a[row][col]}] ', end='')
                else:
                    print(f' {a[row][col]}  ', end='')
            print(f'|{f[row]}\n\n', end='')

    @staticmethod
    def print_step_with_output(step: int, a: list, f: list, step_row: int, step_col: int, to_zero: bool, output: TextIOWrapper):
        '''
        Print step of GJ alg. Project scoped
        '''
        if to_zero:
            print(
                f'\n{step}. calc cell [{step_row},{step_col}] to zero:\n', file=output)
        else:
            if step_row == 5 and step_col == 5:
                todo = True
            print(
                f'\n{step}. calc cell [{step_row},{step_col}] to one:\n', file=output)
        print('{', file=output)
        for row in range(Utils.__print_lim):
            for col in range(Utils.__print_lim):
                if row == step_row and col == step_col:
                    print(f'\t[{a[row][col]}] ', end='', file=output)
                else:
                    print(f'\t {a[row][col]}  ', end='', file=output)
            print(f'|{f[row]}', file=output)
        print('}\n', file=output)

    @staticmethod
    def get_limit(algorithm) -> int:
        '''
        Get limit for specific algorithm and matrix. Project scoped
        '''
        if algorithm.matrix_num == 1:
            return Constants.FIRST_MATRIX_LIMIT
        elif algorithm.matrix_num == 2:
            return Constants.SECOND_MATRIX_LIMIT
        elif algorithm.matrix_num == 3:
            return Constants.THIRD_MATRIX_LIMIT
        elif algorithm.matrix_num == 4:
            return Constants.FOURTH_MATRIX_LIMIT
        elif algorithm.matrix_num == 5:
            if algorithm.alg_type == Constants.ALG_TYPE_NSCR:
                return 10
            return Constants.FIFTH_MATRIX_LIMIT
        elif algorithm.matrix_num == 6:
            return Constants.SIXTH_MATRIX_LIMIT
        elif algorithm.matrix_num == 7:
            return Constants.FIRST_MATRIX_LIMIT
        elif algorithm.matrix_num == 8:
            return Constants.SECOND_MATRIX_LIMIT
        return Constants.FIRST_MATRIX_LIMIT

    @staticmethod
    def get_first_d(algorithm) -> float:
        '''
        Get first delta for specific algorithm and matrix. Project scoped
        '''
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
            if algorithm.matrix_num == 5:
                return 1e-20
            if algorithm.matrix_num == 8:
                return 1e-20
            return 1e-7
        return 1e-6

    @staticmethod
    def get_second_d(algorithm) -> float:
        '''
        Get second delta for specific algorithm and matrix. Project scoped
        '''
        if algorithm.alg_type == Constants.ALG_TYPE_MPP:
            return 1e-3
        elif algorithm.alg_type == Constants.ALG_TYPE_MZ:
            return 1e-3
        elif algorithm.alg_type == Constants.ALG_TYPE_GJ:
            pass
        elif algorithm.alg_type == Constants.ALG_TYPE_SCR:
            if algorithm.matrix_num == 5:
                return 1e-8
            if algorithm.matrix_num == 8:
                return 1e-20
            return 1e-3
        return 1e-3
