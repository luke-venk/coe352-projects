import numpy as np
import argparse
from svd_calculator import svd

def solve_spring_mass_system(springs: np.ndarray, masses: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    For a spring-mass system, find the following:
        (1) The equilibrium displacements of the masses
        (2) The internal stresses of the springs
        (3) The elongations of the springs
    
    Parameters
    ----------
    springs : np.ndarray
        Array of spring constants (N/m).
    masses : np.ndarray
        Array of mass masses (kg).
    
    Returns
    -------
    u : np.ndarray
        The displacements of the masses.
    w : np.ndarray
        The internal stresses of the springs.
    e : np.ndarray
        The elongations of the springs.
    """
    # First, construct difference matrix A
    m, n = len(springs), len(masses)
    A = np.zeros((m, n))
    
    # If the springs outnumber the masses by 1, it is a fixed-fixed system
    if m == n + 1:
        for i in range(n):
            A[i][i] = 1
            A[i + 1][i] = -1
    # If there are the same number of springs as masses, it is a fixed-free system
    elif m == n:
        for i in range(n - 1):
            A[i][i] = 1
            A[i + 1][i] = -1
        A[-1][-1] = 1
    # Otherwise, the system is not solvable
    else:
        raise ValueError('It is not possible to solve a system where the masses outnumber the springs.')
    
    # Construct constituent law matrix C from the spring constants
    C = np.diag(springs)
    
    # Construct stiffness matrix
    K = A.T @ C @ A

    # Use function to solve for the singular value decomposition
    # Also yields condition number and the inverse of K
    _, _, _, cond, K_inv = svd(K)
    print(f'The condition number of K = {cond:.4f}')
    
    # Construct the force vector
    g = 9.81
    f = masses * g
    
    # Solve for the displacements using f = K @ u
    u = K_inv @ f
    
    # Solve for the elongation with e = A @ u
    e = A @ u
    
    # Solve for the internal stress with w = C @ e
    w = C @ e
    
    return u, w, e

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to solve spring-mass systems.')
    parser.add_argument('--type', '-t', type=str, default='custom', help='The type of problem to solve (e.g. fixed-fixed, fixed-free, custom)')
    args = parser.parse_args()
    
    # Use the correct input file based on the command line arguments
    input = None
    if args.type == 'fixed-fixed' or args.type == 'fixed_fixed':
        input = 'fixed_fixed'
    elif args.type == 'fixed-free' or args.type == 'fixed_free':
        input = 'fixed_free'
    input_dir = f'{input}_inputs' if input else 'inputs'
    
    # Read spring inputs
    spring_txt = np.loadtxt(f'{input_dir}/springs.txt', dtype=float)
    num_springs = int(spring_txt[0])
    springs = spring_txt[1:]
    
    # Read mass inputs
    mass_txt = np.loadtxt(f'{input_dir}/masses.txt', dtype=float)
    num_masses = int(mass_txt[0])
    masses = mass_txt[1:]
    
    if num_springs != len(springs) or num_masses != len(masses):
        raise ValueError('The number of inputs in the input file does not match the first line of the file!')
    
    u, w, e = solve_spring_mass_system(springs, masses)
    print(f'Displacements: {u}')
    print(f'Internal Stresses: {w}')
    print(f'Elongations: {e}')