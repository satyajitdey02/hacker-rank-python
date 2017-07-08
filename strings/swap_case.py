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
    #v2: Using List comprehensions
    #return ''.join(c.lower() if c.isupper() else c.upper() for c in s)

    #v3: Using power of pythons utility functions
    #return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
