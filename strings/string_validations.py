if __name__ == '__main__':
    s = input()

    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False

    for c in s:
        if c.islower():
            isalnum = True
            isalpha = True
            islower = True
        elif c.isupper():
            isalnum = True
            isalpha = True
            isupper = True
        elif c.isdigit():
            isdigit = True
            isalnum = True

    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)
