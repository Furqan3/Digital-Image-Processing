def matrix_sum(myarray):
    grid_sums = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            grid_sum = sum(myarray[i][j:j+3]) + sum(myarray[i+1][j:j+3]) + sum(myarray[i+2][j:j+3])
            grid_sums.append(grid_sum)
    return grid_sums
mymatrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24, 25, 26, 27],
            [28, 29, 30, 31, 32, 33, 34, 35, 36],
            [37, 38, 39, 40, 41, 42, 43, 44, 45],
            [46, 47, 48, 49, 50, 51, 52, 53, 54],
            [55, 56, 57, 58, 59, 60, 61, 62, 63],
            [64, 65, 66, 67, 68, 69, 70, 71, 72],
            [73, 74, 75, 76, 77, 78, 79, 80, 81]]

result = matrix_sum(mymatrix)
print(result)