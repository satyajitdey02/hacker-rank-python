def print_formatted(number):
    width = len(str(bin(number))[2:])
    for n in range(number):
        print(str(n + 1).rjust(width), end=' ')
        print(str(oct(n + 1)[2:]).rjust(width), end=' ')
        print(str(hex(n + 1)[2:].upper()).rjust(width), end=' ')
        print(str(bin(n + 1)[2:]).rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
