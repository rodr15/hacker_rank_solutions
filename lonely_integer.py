def lonelyinteger(a):
    # Write your code here
    result = 0
    for i in a:
        print('{0} XOR {1} = {2}'.format(i,result,result ^i))
        result = result ^ i
        
    return result



if __name__ == '__main__':
    a = [0 ,0 ,5 ,2 ,1,5,2]
    print(lonelyinteger(a))
    