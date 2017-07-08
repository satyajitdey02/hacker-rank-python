def count_substring(string, sub_string):
    found = 0
    while True:
        pos = string.find(sub_string)
        if pos >= 0:
            found = found + 1
            string = string[:pos] + string[pos + 1:]
        else:
            break

    return found


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
