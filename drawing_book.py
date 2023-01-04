

def pageCount(n, p):
    # Write your code here
    flipPagesForward = 0
    flipPagesBackward = 0
    
    if(n % 2 == 0): n += 1
    
    for page in range(0,n,2):
    
        if(page < p and page + 1 < p): flipPagesForward += 1
        if(n - page > p and n - page - 1 > p): flipPagesBackward += 1
    
    return min(flipPagesForward,flipPagesBackward)

if __name__ == '__main__':
    # n = 37455
    # p = 29835
    # n = 5
    # p = 4
    n = 6
    p = 5
    print(pageCount(n,p))