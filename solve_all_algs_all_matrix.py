from algorithms.mpp import MPP
from algorithms.mz import Zeidel
from algorithms.gj import GaussJordanoAlg
from algorithms.scr import SCR

from time_logger import Time_logger
from utils import Utils, Constants


with open('solve_all_algs_answers.txt', 'w') as output:

	matrix_num = 6
	print(f'Matrix: {matrix_num}')
	print(f'Matrix: {matrix_num}', file=output)
	alg = GaussJordanoAlg(matrix_num)

	Time_logger.get_instance().start_timer_for_event('algorithm_solve')
	alg.solve()
	Time_logger.get_instance().mark_timestamp_for_event('algorithm_solve')

	if alg.alg_type == Constants.ALG_TYPE_MPP or alg.alg_type == Constants.ALG_TYPE_MZ:
		Utils.print_answers(alg.xs, alg.steps, False, output)
		Utils.print_answers(alg.xs, alg.steps, True, output)
	elif alg.alg_type == Constants.ALG_TYPE_GJ:
		Utils.print_answers(alg.f_check, alg.steps, False, output)
		Utils.print_answers(alg.f_check, alg.steps, True, output)
	elif alg.alg_type == alg.alg_type == Constants.ALG_TYPE_SCR:
		Utils.print_answers(alg.x, alg.steps, False, output)
		Utils.print_answers(alg.x, alg.steps, True, output)

	Time_logger.get_instance().print_events(False, output)
	Time_logger.get_instance().print_events(True, output)


	# matrix_num = 7
	# print(f'\n\nMatrix: {matrix_num}')
	# print(f'\n\nMatrix: {matrix_num}', file=output)
	# alg = GaussJordanoAlg(matrix_num)

	# alg.set_solve_to_n_answer(True)

	# Time_logger.get_instance().start_timer_for_event('algorithm_solve')
	# alg.solve()
	# Time_logger.get_instance().mark_timestamp_for_event('algorithm_solve')

	# if alg.alg_type == Constants.ALG_TYPE_MPP or alg.alg_type == Constants.ALG_TYPE_MZ:
	# 	Utils.print_answers(alg.xs, alg.steps, False, output)
	# 	Utils.print_answers(alg.xs, alg.steps, True, output)
	# elif alg.alg_type == Constants.ALG_TYPE_GJ:
	# 	Utils.print_answers(alg.f_check, alg.steps, False, output)
	# 	Utils.print_answers(alg.f_check, alg.steps, True, output)
	# elif alg.alg_type == alg.alg_type == Constants.ALG_TYPE_SCR:
	# 	Utils.print_answers(alg.x, alg.steps, False, output)
	# 	Utils.print_answers(alg.x, alg.steps, True, output)

	# Time_logger.get_instance().print_events(False, output)
	# Time_logger.get_instance().print_events(True, output)

	# matrix_num = 8
	# print(f'\n\nMatrix: {matrix_num}')
	# print(f'\n\nMatrix: {matrix_num}', file=output)
	# alg = GaussJordanoAlg(matrix_num)

	# alg.set_solve_to_n_answer(True)

	# Time_logger.get_instance().start_timer_for_event('algorithm_solve')
	# alg.solve()
	# Time_logger.get_instance().mark_timestamp_for_event('algorithm_solve')

	# if alg.alg_type == Constants.ALG_TYPE_MPP or alg.alg_type == Constants.ALG_TYPE_MZ:
	# 	Utils.print_answers(alg.xs, alg.steps, True, output)
	# 	Utils.print_answers(alg.xs, alg.steps, False, output)
	# elif alg.alg_type == Constants.ALG_TYPE_GJ:
	# 	Utils.print_answers(alg.f_check, alg.steps, True, output)
	# 	Utils.print_answers(alg.f_check, alg.steps, False, output)
	# elif alg.alg_type == alg.alg_type == Constants.ALG_TYPE_SCR:
	# 	Utils.print_answers(alg.x, alg.steps, True, output)
	# 	Utils.print_answers(alg.x, alg.steps, False, output)

	# Time_logger.get_instance().print_events(True, output)
