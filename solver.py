from algorithms.mpp import MPP
from algorithms.mz import Zeidel
from algorithms.gj import GaussJordanoAlg
from algorithms.scr import SCR
from algorithms.new_alg import NA

from helpers.time_logger import Time_logger
from utils import Utils, Constants
from helpers.solve_builder import Solve_builder
from helpers.alg_builder import Algorithm_builder

import numpy as np


'''
matrix_num = 1 - gaussian example 1
matrix_num = 2 - gaussian example 2
matrix_num = 3 - full example 1
matrix_num = 4 - full example 2
matrix_num = 5 - full example 3
'''

# for matrix_num in range(1, Utils.get_matrix_count() + 1):
matrix_num = 6
if matrix_num == 6:
    # alg_type = 'BASE'
    # alg_type = 'GJ'

    # alg_type = 'MPP'
    # alg_type = 'MZ'
    # alg_type = 'SCR'
    alg_type = 'NA'

    # if alg_type == 'MPP' and matrix_num > 2:
    #     break

    _CALC_NA_LAST_ANSWER = alg_type == 'NA' and matrix_num != 5
    alg = Algorithm_builder.get_alg(alg_type, matrix_num, False)

    '''
    needed for some methods solve to n answer ignoring delta check or solve only first n answers instead of all answers
    '''
    alg.set_solve_to_n_answer(True)
    filename = ''
    if matrix_num == 4:
        filename = f'{alg.alg_type}_Matrix_{matrix_num}_B_{alg.b0}_A_{alg.a0}_february.txt'
    elif matrix_num == 5:
        filename = f'{alg.alg_type}_Matrix_{matrix_num}_february.txt'
    else:
        filename = f'{alg.alg_type}_Matrix_{matrix_num}_B_{alg.b0}_february.txt'

    with open(filename, 'w') as output:

        Utils.print_matrix_type_and_number(alg, output)
        Utils.print_mat(alg.a, alg.f, 6, 8, output)

        if matrix_num == 3:
            todo = True

        alg.presolve()
        Time_logger.get_instance().start_timer_for_event('algorithm_solve')
        alg.solve()
        # alg.solve_with_output(output) # GJ with steps
        Time_logger.get_instance().mark_timestamp_for_event('algorithm_solve')

        print()
        answers = list
        if alg.alg_type == Constants.ALG_TYPE_MPP or alg.alg_type == Constants.ALG_TYPE_MZ:
            answers = alg.xs
        elif alg.alg_type == Constants.ALG_TYPE_GJ:
            answers = alg.f_check
        elif alg.alg_type == Constants.ALG_TYPE_SCR:
            answers = alg.x
        elif alg.alg_type == Constants.ALG_TYPE_NA:
            answers = alg.f
        Utils.print_answers(answers, 'answers:', alg.steps,
                            Constants.PRINT_FLOAT_PRECISION, output)

        # if _CALC_NA_LAST_ANSWER:
        #     i = Constants.LAST_ANSWER_INDEX
        #     alg.solve_at_index(i)
        #     na_last_answer = np.zeros(1)
        #     na_last_answer[0] = alg.f[i]
        #     Utils.print_answers(na_last_answer, f'answer[{i}]:', alg.steps,
        #                         Constants.PRINT_FLOAT_PRECISION, output)

        Solve_builder.build_solution(alg, _CALC_NA_LAST_ANSWER, output)

        Time_logger.get_instance().print_events(output)
