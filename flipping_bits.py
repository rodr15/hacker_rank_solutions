def flippingBits(numbers):
    # Write your code here
    minus = 2**32
    for index,num in enumerate(numbers):
        numbers[index] = (num + 1 - minus) * - 1
    
    return numbers

        

if __name__ == '__main__':
    print(flippingBits([2147483647,1,0]))