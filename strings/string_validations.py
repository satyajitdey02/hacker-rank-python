if __name__ == '__main__':
    s = input()

    isalnum = False
    for c in s:
        if c.isalnum():
            isalnum = True
            break

    isalpha = False
    for c in s:
        if c.isalpha():
            isalpha = True
            break

    isdigit = False
    for c in s:
        if c.isdigit():
            isdigit = True
            break

    islower = False
    for c in s:
        if c.islower():
            islower = True
            break

    isupper = False
    for c in s:
        if c.isupper():
            isupper = True
            break

    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)
