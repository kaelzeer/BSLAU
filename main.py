from algorithms.mpp import MPP
from algorithms.mz import Zeidel
from algorithms.gj import GaussJordanoAlg
from algorithms.scr import SCR

from time_logger import Time_logger
from utils import Utils, Constants

'''
Algorithm choice
'''
matrix_num = 3
alg = MPP(matrix_num)
# alg = Zeidel(matrix_num)
# alg = GaussJordanoAlg(matrix_num)
# alg = SCR(matrix_num)
if (matrix_num == 2 or matrix_num == 4) and (alg.alg_type == Constants.ALG_TYPE_MPP or alg.alg_type == Constants.ALG_TYPE_MZ or alg.alg_type == Constants.ALG_TYPE_SCR):
	alg.set_solve_to_n_answer(True)
'''
Solve with time logging
'''
Time_logger.get_instance().start_timer_for_event('algorithm_solve')
alg.solve()
Time_logger.get_instance().mark_timestamp_for_event('algorithm_solve')

'''
Answers print
'''
if alg.alg_type == Constants.ALG_TYPE_MPP or alg.alg_type == Constants.ALG_TYPE_MZ:
	Utils.print_answers(alg.xs, alg.steps)
elif alg.alg_type == Constants.ALG_TYPE_GJ:
	Utils.print_answers(alg.f_check, alg.steps)
elif alg.alg_type == alg.alg_type == Constants.ALG_TYPE_SCR:
	Utils.print_answers(alg.x, alg.steps)
'''
Time logger print
'''
Time_logger.get_instance().print_events()
