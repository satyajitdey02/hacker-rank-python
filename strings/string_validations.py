if __name__ == '__main__':
    s = input()

    '''print True if any(k in "0123456789" or k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in S) else False
    print True if any(k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in S) else False
    print True if any(k in "0123456789" for k in S) else False
    print True if any(k in "abcdefghijklmnopqrstuvwxyz" for k in S) else False
    print True if any(k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for k in S) else False'''

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
