def rotate(mat):
    """
    Rotate a matrix 90 degrees clockwise in-place.
    """
    n = len(mat)

    # Transpose
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    '''
    (0,1), (1,0) -> (1,0), (0,1)
    (0,2), (2,0) -> (2,0), (0,2)
    (1,2), (2,1) -> (2,1), (1,2)
    '''

    # Horizontal Reflection
    for i in range(n):
        for j in range(n//2): 
            mat[i][j], mat[i][n-j-1] = mat[i][n-j-1], mat[i][j]
    '''
    (0,0), (0,2) -> (0,2), (0,0)
    (0,1), (0,1) -> (0,1), (0,1)
    (1,0), (1,2) -> (1,2), (1,0)
    (1,1), (1,1) -> (1,1), (1,1)
    (2,0), (2,2) -> (2,2), (2,0)
    '''


mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(mat1)
print(mat1)

mat2 = [
    [1, 2],
    [3, 4]
]

rotate(mat2)
print(mat2)

mat3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rotate(mat3)
print(mat3)