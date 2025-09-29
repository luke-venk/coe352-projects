import numpy as np
from svd_calculator import svd


def test_hw2_q1_matrix():
    """ HW 2 Problem 1 """
    A = np.array([[3, 2, 2], [2, 3, -2]])
    U, S, VT, _, _ = svd(A)
    assert np.allclose(A, U @ S @ VT)
    
def test_hw2_q2_matrix():
    """ HW 2 Problem 2 """
    A = np.array([[-3, 1], [6, -2], [6, -2]])
    U, S, VT, _, _ = svd(A)
    assert np.allclose(A, U @ S @ VT)
    
def test_invertible_matrix():
    A = np.array(
        [[6, 8, 3, 5],
        [1, 2, 2, 8],
        [4, 6, 5, 7],
        [2, 4, 5, 4]]
    )
    my_U, my_S, my_VT, my_K, my_A_inv = svd(A)
    their_U, their_s, their_VT = np.linalg.svd(A)
    print(f'My U:\n{my_U}')
    print(f'Solver U:\n{their_U}')
    print(f'\nMy S:\n{my_S}')
    print(f'Solver S:\n{np.diag(their_s)}')
    print(f'\nMy VT:\n{my_VT}')
    print(f'Solver VT:\n{their_VT}')
    print(f'\nCondition number = {my_K}')
    print(f'\nInverse of A: \n{my_A_inv}')
    assert np.allclose(A, my_U @ my_S @ my_VT)
    """
    My answer is right, but Eigen/SVD solvers arbitrarily pick signs.
    Thus, both my answer and the Python solver are right, despite having
    different signs for some numbers. This is because, eigenvectors are
    only determined up to a sign.
    """
    

# test_hw2_q1_matrix()
# test_hw2_q2_matrix()
test_invertible_matrix()