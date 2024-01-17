from algorithms.mpp import MPP
from algorithms.mz import Zeidel
from algorithms.gj import GaussJordanoAlg
from algorithms.scr import SCR
from algorithms.lu_gj import LUGJ
from algorithms.lu_gj_fixed import LUGJF
from algorithms.lu_gj_podstanovka import LUGJP

from time_logger import Time_logger
from utils import Utils, Constants


'''
Solve new matrixes
'''

matrix_num = 5  # plastinka

# alg = Zeidel(matrix_num)
# alg = SCR(matrix_num)
alg = GaussJordanoAlg(matrix_num)
# alg = LUGJ(matrix_num)
# alg = LUGJF(matrix_num)

filename = 'some_alg_plast.txt'

if alg.alg_type == Constants.ALG_TYPE_MPP:
    filename = 'MPP_plast.txt'
elif alg.alg_type == Constants.ALG_TYPE_MZ:
    filename = 'MZ_plast.txt'
elif alg.alg_type == Constants.ALG_TYPE_GJ:
    filename = 'GJ_plast.txt'
elif alg.alg_type == Constants.ALG_TYPE_SCR:
    filename = 'SCR_plast.txt'
elif alg.alg_type == Constants.ALG_TYPE_LUGJ:
    filename = 'LUGJ_plast.txt'
elif alg.alg_type == Constants.ALG_TYPE_LUGJF:
    filename = 'LUGJF_plast.txt'

with open(filename, 'w') as output:

    print(f'Matrix: {matrix_num}')
    print(f'Matrix: {matrix_num}', file=output)

    Utils.print_mat_to_file(alg.a, alg.f, output)

    Time_logger.get_instance().start_timer_for_event('algorithm_solve')
    alg.solve()
    # alg.solve_with_output(output) # GJ with steps
    Time_logger.get_instance().mark_timestamp_for_event('algorithm_solve')

    if alg.alg_type == Constants.ALG_TYPE_MPP or alg.alg_type == Constants.ALG_TYPE_MZ:
        Utils.print_answers(alg.xs, alg.steps, False, output)
        Utils.print_answers(alg.xs, alg.steps, True, output)
    elif alg.alg_type == Constants.ALG_TYPE_GJ:
        Utils.print_answers(alg.f_check, alg.steps, False, output)
        Utils.print_answers(alg.f_check, alg.steps, True, output)
    elif alg.alg_type == Constants.ALG_TYPE_SCR:
        Utils.print_answers(alg.x, alg.steps, False, output)
        Utils.print_answers(alg.x, alg.steps, True, output)
    elif alg.alg_type == Constants.ALG_TYPE_LUGJ:
        Utils.print_answers(alg.f, -1, False, output)
        Utils.print_answers(alg.f, -1, True, output)
    elif alg.alg_type == Constants.ALG_TYPE_LUGJF:
        Utils.print_answers(alg.y, -1, False, output)
        Utils.print_answers(alg.y, -1, True, output)

    Time_logger.get_instance().print_events(False, output)
    Time_logger.get_instance().print_events(True, output)
