from os import stat
from re import S
from xml.dom.minidom import Element


def rotateLeft(d, arr):
    # Write your code here
    
    return  arr[d:] + arr[:d] 

if __name__ == '__main__':
    # d = 4
    # arr = [1, 2, 3, 4, 5]
    d = 2
    arr = [1, 2, 3, 4, 5]
    print(rotateLeft(d,arr))