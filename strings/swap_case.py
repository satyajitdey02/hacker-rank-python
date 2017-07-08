def swap_case(s):
    chars = list(s)
    result = []
    for c in chars:
        if str(c).islower():
            result.append(str(c).upper())
        elif str(c).isupper():
            result.append(str(c).lower())
        else:
            result.append(c)

    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
