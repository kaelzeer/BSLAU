

class Constants:
	'''
	Limits for matrixes
	'''
	BASE_MATRIX_LIMIT = 50
	FIRST_MATRIX_LIMIT = 800
	SECOND_MATRIX_LIMIT = 70
	THIRD_MATRIX_LIMIT = 800
	FOURTH_MATRIX_LIMIT = 70
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


class Utils:
	'''
	Project scoped utility methods
	'''
	__print_lim = 10
	NMAX = 5000

	@staticmethod
	def print_mat(a : list, f : list):
		'''
		Print matrix method. Project scoped
		'''
		for row in range(Utils.__print_lim):
			for col in range(Utils.__print_lim):
				print(f'{a[row][col]} ', end='')
			print(f'|{f[row]}\n\n', end='')


	@staticmethod
	def print_answers(x : list, ss : int):
		'''
		Print answers of system equation. Project scoped
		'''
		print(f's={ss}')
		for i in range(Utils.__print_lim):
			print(x[i], end=' ')
		print()


	@staticmethod
	def print_step(a : list, f : list, step_row : int, step_col : int, to_zero : bool):
		'''
		Print step of GJ alg. Project scoped
		'''
		if to_zero:
			print(f'\ncalc cell [{step_row},{step_col}] to zero:\n')
		else:
			print(f'\ncalc cell [{step_row},{step_col}] to one:\n')
		for row in range(Utils.__print_lim):
			for col in range(Utils.__print_lim):
				if row == step_row and col == step_col:
					print(f'[{a[row][col]}] ', end='')
				else:
					print(f' {a[row][col]}  ', end='')
			print(f'|{f[row]}\n\n', end='')


	@staticmethod
	def get_limit(algorithm) -> int:
		'''
		Get limit for specific algorithm and matrix. Project scoped
		'''
		if algorithm.matrix_num == 1:
			if algorithm.alg_type == Constants.ALG_TYPE_MPP:
				return Constants.FIRST_MATRIX_LIMIT
			elif algorithm.alg_type == Constants.ALG_TYPE_MZ:
				return Constants.FIRST_MATRIX_LIMIT
			elif algorithm.alg_type == Constants.ALG_TYPE_GJ:
				return Constants.FIRST_MATRIX_LIMIT * 2
			elif algorithm.alg_type == Constants.ALG_TYPE_SCR:
				return Constants.FIRST_MATRIX_LIMIT
		elif algorithm.matrix_num == 2:
			return Constants.SECOND_MATRIX_LIMIT
		elif algorithm.matrix_num == 3:
			return Constants.THIRD_MATRIX_LIMIT
		elif algorithm.matrix_num == 4:
			return Constants.FOURTH_MATRIX_LIMIT
		return Constants.BASE_MATRIX_LIMIT

	
	@staticmethod
	def get_first_d(algorithm) -> float:
		'''
		Get first delta for specific algorithm and matrix. Project scoped
		'''
		if algorithm.alg_type == Constants.ALG_TYPE_MPP:
			if algorithm.matrix_num == 1:
				return 0.000001
			elif algorithm.matrix_num == 2:
				return 0.000001
			elif algorithm.matrix_num == 3:
				return 0.000001
			elif algorithm.matrix_num == 4:
				return 0.0025
		elif algorithm.alg_type == Constants.ALG_TYPE_MZ:
			return 0.0000001
		elif algorithm.alg_type == Constants.ALG_TYPE_GJ:
			return 0.000001
		elif algorithm.alg_type == Constants.ALG_TYPE_SCR:
			return 0.0000001
		return 0.000001
		
	@staticmethod
	def get_second_d(algorithm) -> float:
		'''
		Get second delta for specific algorithm and matrix. Project scoped
		'''
		if algorithm.alg_type == Constants.ALG_TYPE_MPP:
			return 0.001
		elif algorithm.alg_type == Constants.ALG_TYPE_MZ:
			return 0.001
		elif algorithm.alg_type == Constants.ALG_TYPE_GJ:
			pass
		elif algorithm.alg_type == Constants.ALG_TYPE_SCR:
			0.001
		return 0.001