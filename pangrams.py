def pangrams(s):
    # Write your code here
    unique_letters = set(s.lower())
    print(len(unique_letters))
    if(len(unique_letters) <= 26): return 'not pangram'
    else: return 'pangram'


if __name__ == '__main__':
    x = 'We promptly judged antique ivory buckles for the prize    '
    print(pangrams(x))