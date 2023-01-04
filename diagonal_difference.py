from turtle import right


def diagonalDifference(arr):
    # Write your code here
    right_diagonal = 0
    left_diagonal = 0
    for index in range(len(arr)):
        right_diagonal += arr[index][index]
        left_diagonal += arr[len(arr) - 1 - index][index]

    return abs(right_diagonal - left_diagonal)
  

if __name__ == '__main__':
    matrix = [[1, 2, 3],[4, 5, 6],[9, 8 ,9]]
    print(diagonalDifference(matrix))