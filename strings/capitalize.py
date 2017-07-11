def capitalize(string):
    words = string.split(' ')
    result = []
    for w in words:
        result.append(w.capitalize())

    return ' '.join(result)


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
