from algorithms.mpp import MPP
from algorithms.mz import Zeidel
from algorithms.gj import GaussJordanoAlg
from algorithms.scr import SCR
from algorithms.new_alg import NA

from helpers.time_logger import Time_logger
from utils import Utils, Constants
from helpers.solve_builder import Solve_builder


'''
matrix_num = 1 - gaussian example 1
matrix_num = 2 - gaussian example 2
matrix_num = 3 - full example 1
matrix_num = 4 - full example 2
matrix_num = 5 - full example 3
'''

for matrix_num in range(1, Utils.get_matrix_count() + 1):

    # alg = MPP(matrix_num)

    # alg = Zeidel(matrix_num)

    # alg = SCR(matrix_num)

    # alg = GaussJordanoAlg(matrix_num)

    alg = NA(matrix_num)

    '''
    needed for some methods solve to n answer ignoring delta check
    '''
    # alg.set_solve_to_n_answer(True)
    filename = ''
    if matrix_num == 4:
        filename = f'Matrix_{matrix_num}_B_{alg.b0}_A_{alg.a0}_{alg.alg_type}_february.txt'
    elif matrix_num == 5:
        filename = f'Matrix_{matrix_num}_{alg.alg_type}_february.txt'
    else:
        filename = f'Matrix_{matrix_num}_B_{alg.b0}_{alg.alg_type}_february.txt'

    with open(filename, 'w') as output:

        Utils.print_matrix_type_and_number(alg, output)
        Utils.print_mat(alg.a, alg.f, 6, 8, output)

        if matrix_num == 3:
            todo = True

        Time_logger.get_instance().start_timer_for_event('algorithm_solve')
        alg.solve()
        # alg.solve_with_output(output) # GJ with steps
        Time_logger.get_instance().mark_timestamp_for_event('algorithm_solve')

        print()
        if alg.alg_type == Constants.ALG_TYPE_MPP or alg.alg_type == Constants.ALG_TYPE_MZ:
            Utils.print_answers(alg.xs, 'answers:', alg.steps, False, output)
            Utils.print_answers(alg.xs, 'answers:', alg.steps, True, output)
        elif alg.alg_type == Constants.ALG_TYPE_GJ:
            Utils.print_answers(alg.f_check, 'answers:',
                                alg.steps, False, output)
            Utils.print_answers(alg.f_check, 'answers:',
                                alg.steps, True, output)
        elif alg.alg_type == Constants.ALG_TYPE_SCR:
            Utils.print_answers(alg.x, 'answers:', alg.steps, False, output)
            Utils.print_answers(alg.x, 'answers:', alg.steps, True, output)
        elif alg.alg_type == Constants.ALG_TYPE_NA:
            Utils.print_answers(alg.f, 'answers:', -1, False, output)
            Utils.print_answers(alg.f, 'answers:', -1, True, output)

        Solve_builder.build_solution(alg, output)

        Time_logger.get_instance().print_events(False, output)
        Time_logger.get_instance().print_events(True, output)
