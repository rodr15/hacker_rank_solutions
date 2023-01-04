def sockMerchant(n, ar):
    unique = set(ar)
    pairs = 0
    
    for sock in unique:
        pairs += ar.count(sock) // 2 

    
    return pairs

    
if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    print(sockMerchant(n,ar))