from algorithms.mpp import MPP
from algorithms.mz import Zeidel
from algorithms.gj import GaussJordanoAlg
from algorithms.scr import SCR

from time_logger import Time_logger
from utils import Utils, Constants
'''
Solve new matrixes
'''


with open('solver.txt', 'w') as output:

	matrix_num = 1
	print(f'Matrix: {matrix_num}')
	print(f'Matrix: {matrix_num}', file=output)

	alg = MPP(matrix_num)
	
	Time_logger.get_instance().start_timer_for_event('algorithm_solve')
	alg.solve()
	Time_logger.get_instance().mark_timestamp_for_event('algorithm_solve')

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