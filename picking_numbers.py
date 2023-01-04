from collections import Counter


def pickingNumbers(a):
    # Write your code here
    arr = Counter(a)

    max_num = 0

    for i in range(100):
        max_num = max(max_num,arr[i] + arr [i + 1])

    return max_num
if __name__ == '__main__':
    # s = [1,1,1,1,2,2,4,4,5,5,5]
    s = [4,6,5,3,3,1]
    s = [1, 2, 2, 3, 1, 2]
    print(pickingNumbers(s))