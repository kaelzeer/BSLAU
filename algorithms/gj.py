from utils import Utils, Constants
from algorithms.base_alg import Algorithm

import numpy as np


class GaussJordanoAlg(Algorithm):

	def __init__(self, matrix_num : int = 1) -> None:

		super().__init__(matrix_num)
		self.alg_type = Constants.ALG_TYPE_GJ
		super().post_init()

		# self.answers_length = 2
		self.f_check = np.zeros(self.limit)
		self.prev_f = np.zeros(self.limit)
		self.changed_cols = np.zeros(self.limit)
		self.current_mat_size = 2


	def make_cell_one(self, cell_row : int, cell_col : int):

		divider = self.a[cell_row][cell_col]
		if cell_row != cell_col or divider == 1:
			return
		
		last_col = self.limit if cell_col < Utils.NMAX else Utils.NMAX
		if divider == 0:
			non_zero_element_index = self.get_first_non_zero_col(cell_row, cell_col + 1)
			self.a[cell_row], self.a[non_zero_element_index] = self.a[non_zero_element_index], self.a[cell_row]
			divider = self.a[cell_row][cell_col]
		
		if divider != 1:
			for col in range (cell_col, last_col):
				self.a[cell_row][col] /= divider
			self.f[cell_row] /= divider
		# Utils.print_step(self.a, self.f, cell_row, cell_col, False)
			
	
	def calculate_cell(self, cell_row : int, cell_col : int):

		if cell_row == cell_col or self.a[cell_col][cell_col] != 1.0:
			self.make_cell_one(cell_col, cell_col)

		last_col = self.limit if cell_col < Utils.NMAX else Utils.NMAX
		if self.a[cell_row][cell_col] != 0:
			divider = -self.a[cell_row][cell_col]
			for col in range(cell_col,last_col):
				self.a[cell_row][col] += self.a[cell_col][col] * divider
			self.f[cell_row] += self.f[cell_col] * divider
		# Utils.print_step(self.a, self.f, cell_row, cell_col, True)


	def get_first_non_zero_col(self, row : int, first_col : int)->int:
		
		last_col = self.limit
		for col in range(first_col, last_col):
			if self.a[row][col] != 0:
				return col
		return -1
	

	def solve(self):

		d = 0.0
		cur_row = 0
		cur_col = 0

		while True:
			prev_f_row = 0.0
			cur_f_row = self.f[cur_row]
			self.steps += 1
			self.prev_f = np.array(self.f_check)

			while True:
				last_row = self.current_mat_size - 1
				last_col = self.current_mat_size - 1

				for col in range(last_col):
					self.calculate_cell(last_row, col)

				if not cur_row:
					cur_col = last_col # first row only
				else:
					cur_col = self.get_first_non_zero_col(cur_row, cur_row + 1) # other rows starts from main diag
				# print(f'cur_row : {cur_row}, cur_col : {cur_col}')
				self.calculate_cell(cur_row, cur_col)
				self.changed_cols[cur_row] = cur_col
				prev_f_row = cur_f_row
				cur_f_row = self.f[cur_row]
				d = abs(cur_f_row - prev_f_row)
				self.f_check = self.f
				# print(f'row check:\n row: {cur_row}, col: {cur_col}, matrix size: {self.current_mat_size}, prev: {prev_f_row}, cur: {cur_f_row} d: {d}\n')
				if cur_col >= last_col and self.current_mat_size < self.limit:
					self.current_mat_size += 1
				
				if d < 0.0001:
					print(f'row check:\n row: {cur_row}, col: {cur_col}, matrix size: {self.current_mat_size}, prev: {prev_f_row}, cur: {cur_f_row} d: {d}\n')
				
				# do-while-emu exit condition
				if d < Utils.get_first_d(self):
					break

			cur_row += 1
			cur_col = cur_row + 1

			# do-while-emu exit condition
			if cur_row > self.answers_length: # or d < 0.001:
				print(f'end')
				break

'''
	def repeatedSolve(self):
		cur_row = 0
		cur_col = 0

		while True:
			additional_count = 0
			while True:
				last_row = self.current_mat_size - 1
				last_col = self.current_mat_size - 1

				for col in range(last_col):
					self.calculate_cell(last_row, col)

				if not cur_row:
					cur_col = last_col # first row only
				else:
					cur_col = self.get_first_non_zero_col(cur_row, cur_row + 1) # other rows starts from main diag
				# print(f'cur_row : {cur_row}, cur_col : {cur_col}')
				self.calculate_cell(cur_row, cur_col)
				self.changed_cols[cur_row] = cur_col
				additional_count += 1

				if cur_col >= last_col and self.current_mat_size < self.limit:
					self.current_mat_size += 1

				# if additional_count >= 5:
				if Matrix_builder.check_second_mat(cur_row, self.answers_length, self.f, self.f_orig, self.a_orig) or additional_count >= 5:
					break
			
			cur_row += 1
			cur_col = cur_row + 1
			# print(f'answers check:\n matrix size: {self.current_mat_size}, d: {d}\n')

			# do-while-emu exit condition
			if cur_row > self.answers_length:
				print(f'end')
				break
'''

# while True:
# 	hasFalse = False
# 	checked = Matrix_builder.check_second_mat_arr(alg.answers_length, alg.f, alg.f_orig, alg.a_orig)
# 	false_count = 0
# 	true_count = 0
# 	for member in checked:
# 		if not member:
# 			false_count += 1
# 		else:
# 			true_count += 1

# 	if false_count > true_count:
# 		alg.repeatedSolve()
# 	else:
# 		break

# Utils.print_answers(alg.f_check, alg.steps)
# delta, checked = Matrix_builder.check_second_mat(alg.b, alg.answers_length, alg.f_check, True)