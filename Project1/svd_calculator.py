import numpy as np

def svd(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, int, np.ndarray]:
    """
    Get the Singular Value Decomposition (SVD) of an input matrix A.
    
    For any matrix A in R(mxn), this function returns orthogonal matrices U
    in R(mxm) and V in R(nxn), as well as a non-negative diagonal matrix
    Sigma in R(mxn) such that:
        
        A = U @ S @ V^T.
    
    In addition to the SVD, this function also returns the condition number
    and inverse of matrix A.
    
        A^-1 = V S^{-1} U.T
        K = ||A|| ||A^-1||
    
    Parameters
    ----------
    A : np.ndarray
        Real 2D array of shape (m, n), representing the input matrix.

    Returns
    -------
    U : np.ndarray
        Orthogonal matrix of shape (m, m). Its columns are the singular left
        vectors of A.
    S : np.ndarray
        Non-negative, diagonal matrix of shape (m, n). Its diagonals are
        the singular values of A.
    VT : np.ndarray
        Orthogonal matrix of shape (n, n). We return it as the transpose for
        convenience. Its rows are the singular right vectors of A.
    K : Optional[int]
        The condition number of matrix A, if it exists.
    A_inv : Optional[np.ndarray]
        The inverse of matrix A, if it exists.
    """
    # Store dimensions of A, and compute A @ A.T, as well as A.T @ A.
    # Also, ensure float math
    A = np.asarray(A, dtype=float)
    m, n = A.shape
    AAT = A @ A.T
    ATA = A.T @ A
    
    # Eigenvectors of AAT are the left singular vectors -> columns of U
    eigenvalues_U, U = np.linalg.eigh(AAT)
    
    # Eigenvectors of ATA are the right singular vectors -> columns of V
    eigenvalues_V, V = np.linalg.eigh(ATA)
    
    # eigh() returns values in ascending order, but by convention in SVD,
    # these values should be in descending order. Rearrange the order of
    # the eigenvectors in the same way as well (reorder the columns).
    U_idx = np.argsort(eigenvalues_U)[::-1]
    eigenvalues_U = eigenvalues_U[U_idx]
    U = U[:, U_idx]
    
    V_idx = np.argsort(eigenvalues_V)[::-1]
    eigenvalues_V = eigenvalues_V[V_idx]
    V = V[:, V_idx]
    
    # The singular values are the square root of these eigenvalues.
    # These are equivalent to the diagonal entries of S.
    # Use clip() to make small negative numbers just 0
    sigmas = np.sqrt(np.clip(eigenvalues_U, 0.0, None))
    
    # Note that while S is a diagonal matrix, it must have the same
    # dimensions as A.
    k = min(m, n)
    S = np.zeros_like(A, dtype=float)
    S[:k, :k] = np.diag(sigmas[:k])
    
    # Eigen solvers don't guarantee consistent sign choices between U and V.
    # Align signs so that A @ v_i == sigma_i * u_i for i < k with sigma_i > 0
    for i in range(k):
        if sigmas[i] > 0:
            w = A @ V[:, i]               # should equal sigma_i * U[:, i] up to sign
            if np.dot(w, U[:, i]) < 0:    # opposite direction -> flip one side
                U[:, i] *= -1
                # (equivalently, you could do V[:, i] *= -1; flipping either is fine)
    
    # If any of the singular values are equal to 0, then the inverse doesn't exist
    # Also, if it is not a square matrix, it is not invertible.
    if m != n or np.any(sigmas[:n] <= 1e-5):
        print('The inverse of matrix A does not exist.')
        return U, S, V.T, None, None
    
    # At this point, can go ahead and compute the inverse of matrix A
    # A^{-1} = V S^{-1} U.T
    S_inv = np.diag(1.0 / sigmas[:n])
    A_inv = V[:, :n] @ S_inv @ U[:, :n].T
    
    # Compute the condition number
    K = np.linalg.norm(A) * np.linalg.norm(A_inv)
    
    return U, S, V.T, K, A_inv