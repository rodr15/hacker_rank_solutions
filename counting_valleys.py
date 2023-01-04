
def countingValleys(steps, path):
    # Write your code here
    level = 0
    valley = 0
    
    d = {'U' : 1 , 'D': -1}

    for step in path:
        level += d[step]
        if level == 0 and step == 'U':
            valley += 1

    return valley

    
if __name__ == '__main__':
    steps = 8
    path = 'UDDDUDUU'
    print(countingValleys(steps,path))