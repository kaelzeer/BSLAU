import numpy as np

from helpers.matrix_builder import Matrix_builder
from helpers.matrix_builder_new import NMatrix_builder
from utils import Utils, Constants


class Algorithm:

    def __init__(self, matrix_num: int) -> None:

        self.alg_type = Constants.ALG_TYPE_BASE
        self.answers_length = 10
        self.steps = 0
        self.a0 = 0
        self.b0 = Constants.B0
        if matrix_num == 4:
            self.a0 = Constants.A0_FM2
            self.b0 = Constants.B0_FM2
        self.matrix_num = matrix_num
        self.first_index = 0
        self.limit = Constants.BASE_MATRIX_LIMIT

    def post_init(self):

        self.limit = Utils.get_limit(self.matrix_num)
        # self.a = np.zeros((self.limit,self.limit))
        # self.f = np.zeros(self.limit)
        self.answers = np.zeros(self.limit)

        self.solve_to_n_answer = False
        self.build_matrix()

    def build_matrix(self) -> None:

        NMatrix_builder.build_matrix(self)

    def presolve(self) -> None:

        pass

    def solve(self) -> None:

        pass

    def set_solve_to_n_answer(self, value: bool) -> None:

        self.solve_to_n_answer = value
