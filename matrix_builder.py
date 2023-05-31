from utils import Utils
import math
from time_logger import Time_logger
import numpy as np


class Matrix_builder:

	@staticmethod
	def build_matrix(algorithm) -> None:
		
		Time_logger.get_instance().start_timer_for_event("matrix_creation")

		if algorithm.matrix_num == 1:
			Matrix_builder.build_first_matrix(algorithm)
		elif algorithm.matrix_num == 2:
			Matrix_builder.build_second_matrix(algorithm)
		elif algorithm.matrix_num == 3:
			Matrix_builder.build_third_matrix(algorithm)
		elif algorithm.matrix_num == 4:
			Matrix_builder.build_fourth_matrix(algorithm)

		Time_logger.get_instance().mark_timestamp_for_event("matrix_creation")
    
	@staticmethod
	def build_first_matrix(algorithm) -> None:

		algorithm.f = np.zeros(algorithm.limit)
		algorithm.a = np.zeros((algorithm.limit,algorithm.limit),np.double)

		for i in range(algorithm.limit):
			for j in range(algorithm.limit):
				if i == j:
					algorithm.a[i][j] = -1
				else:
					algorithm.a[i][j] =  1.0 / (( 2 * (i + 1) + 1 - 2 * (j + 1)) * (2 * (i + 1) - 1 - 2 * (j + 1)) )
					
		algorithm.f[0] = -1

		print('Original matrix:')
		Utils.print_mat(algorithm.a, algorithm.f)
	

	@staticmethod
	def build_second_matrix(algorithm, matmul : bool = True) -> None:

		algorithm.f = np.zeros(algorithm.limit)
		algorithm.a = np.zeros((algorithm.limit,algorithm.limit),np.double)


		for j in range(algorithm.limit):
			for p in range(algorithm.limit - j):
				n = 2 * j + 2 * p + 1
				k = 2 * j
				sss = math.perm(n, k)
				algorithm.a[j,j+p] = sss
			algorithm.f[j] = algorithm.b0 ** j
			if j != 0:
				algorithm.f[j] += algorithm.f[j - 1]

		print('Original matrix:')
		Utils.print_mat(algorithm.a, algorithm.f)
		if matmul:
			lower_triangle_mat = np.zeros((algorithm.limit,algorithm.limit))

			for i in range(algorithm.limit):
				for j in range(algorithm.limit):
					if i >= j:
						lower_triangle_mat[i,j] = 1

			print('lower triangle matrix:')
			Utils.print_mat(lower_triangle_mat, algorithm.f)
			algorithm.a = np.matmul(lower_triangle_mat,algorithm.a)

		print('lower_triangle * matrix:')
		Utils.print_mat(algorithm.a, algorithm.f)
	

	@staticmethod
	def build_third_matrix(algorithm) -> None:

		algorithm.f = np.zeros(algorithm.limit)
		algorithm.a = np.zeros((algorithm.limit,algorithm.limit),np.double)
		lower_triangle_mat = np.zeros((algorithm.limit,algorithm.limit),np.double)

		for i in range(algorithm.limit):
			for j in range(algorithm.limit):
				if i >= j:
					lower_triangle_mat[i][j] = 1
				else:
					lower_triangle_mat[i][j] = 0
				first = (2 * (i + 1) + 1 - 2 * (j + 1))
				second = (2 * (i + 1) - 1 - 2 * (j + 1))
				algorithm.a[i][j] = 1.0 / (first * second)
			algorithm.f[i] = -1.0 / (4 * (i + 1) - 2)

		print('Original matrix:')
		Utils.print_mat(algorithm.a, algorithm.f)


	@staticmethod
	def build_fourth_matrix(algorithm, matmul : bool = True) -> None:

		algorithm.f = np.zeros(algorithm.limit)
		algorithm.a = np.zeros((algorithm.limit,algorithm.limit),np.double)


		for j in range(algorithm.limit):
			for p in range(algorithm.limit - j):
				n = 2 * j + 2 * p
				k = 2 * j
				sss = math.perm(n, k)
				algorithm.a[j,j+p] = sss
			algorithm.f[j] = algorithm.b0 ** j
			if j != 0:
				algorithm.f[j] += algorithm.f[j - 1]

		print('Original matrix:')
		Utils.print_mat(algorithm.a, algorithm.f)
		if matmul:
			lower_triangle_mat = np.zeros((algorithm.limit,algorithm.limit))

			for i in range(algorithm.limit):
				for j in range(algorithm.limit):
					if i >= j:
						lower_triangle_mat[i,j] = 1

			print('lower triangle matrix:')
			Utils.print_mat(lower_triangle_mat, algorithm.f)
			algorithm.a = np.matmul(lower_triangle_mat,algorithm.a)

		print('lower_triangle * matrix:')
		Utils.print_mat(algorithm.a, algorithm.f)

	@staticmethod
	def build_fifth_matrix(algorithm) -> None:
		
		algorithm.f = np.zeros(algorithm.limit)
		algorithm.a = np.zeros((algorithm.limit,algorithm.limit),np.double)

		n = 1 # temp
		phi = 1 # algorithm.b5 / algorithm.a5
		n_pi_phi = n * math.pi # * phi
		alpha_n = (n * math.pi / 16) * (n_pi_phi + math.sinh(n_pi_phi)) / pow(math.cosh(n_pi_phi / 2), 2)
		# alpha_n =  pow(phi, -5) * (n * math.pi / 16) * (n_pi_phi + math.sinh(n_pi_phi)) / pow(math.cosh(n_pi_phi / 2), 2)
		alpha_after_10 = n * math.pi / 8

		for p in range(1,algorithm.limit,2):
			for n in range(1,algorithm.limit,2):
				if n < 10:
					alpha_n = (n * math.pi / 16) * (n_pi_phi + math.sinh(n_pi_phi)) / pow(math.cosh(n_pi_phi / 2), 2)
				else:
					alpha_n = n * math.pi / 8
				algorithm.a[p,n] = alpha_n


