from algorithms.mpp import MPP
from algorithms.mz import Zeidel
from algorithms.gj import GaussJordanoAlg
from algorithms.scr import SCR
from algorithms.lu_gj import LUGJ

from time_logger import Time_logger
from utils import Utils, Constants


'''
Solve new matrixes
'''
with open('solver.txt', 'w') as output:

    matrix_num = 5
    print(f'Matrix: {matrix_num}')
    print(f'Matrix: {matrix_num}', file=output)

    alg = LUGJ(matrix_num)
    # alg = SCR(matrix_num)

    # SCR matrix 8
    # alg.set_solve_to_n_answer(True)

    Utils.print_mat_to_file(alg.a, alg.f, output)

    # Time_logger.get_instance().start_timer_for_event('algorithm_solve')
    alg.solve()
    # alg.solve_with_output(output) # GJ with steps
    # Time_logger.get_instance().mark_timestamp_for_event('algorithm_solve')

    # if alg.alg_type == Constants.ALG_TYPE_MPP or alg.alg_type == Constants.ALG_TYPE_MZ:
    #     Utils.print_answers(alg.xs, alg.steps, False, output)
    #     Utils.print_answers(alg.xs, alg.steps, True, output)
    # elif alg.alg_type == Constants.ALG_TYPE_GJ:
    #     Utils.print_answers(alg.f_check, alg.steps, False, output)
    #     Utils.print_answers(alg.f_check, alg.steps, True, output)
    # elif alg.alg_type == alg.alg_type == Constants.ALG_TYPE_SCR:
    #     Utils.print_answers(alg.x, alg.steps, False, output)
    #     Utils.print_answers(alg.x, alg.steps, True, output)

    # Time_logger.get_instance().print_events(False, output)
    # Time_logger.get_instance().print_events(True, output)
