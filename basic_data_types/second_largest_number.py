if __name__ == '__main__':
    n = int(input())
    numbers = sorted(list({int(i) for i in input().split()}))
    print(numbers[-2])