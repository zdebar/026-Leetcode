def rotate_matrix(m: list[list[int]]) -> None:
    """
    Rotate the given n x n matrix by 90 degrees (clockwise) in-place.
    :param m: List of lists representing the matrix.
    :return: None, modifies the matrix in place.
    """
    n = len(m)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    
    # Reverse each row
    for i in range(n):
        m[i].reverse()



def rotate_matrix_zip(m: list[list[int]]) -> None:
    """
    Rotate the given n x n matrix by 90 degrees (clockwise) in-place using zip.
    :param m: List of lists representing the matrix.
    :return: None, modifies the matrix in place.
    """
    # Transpose and reverse each row using zip
    m[:] = [list(row) for row in zip(*m[::-1])]