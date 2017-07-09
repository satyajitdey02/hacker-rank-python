import textwrap


def wrap(string, max_width):
    #textwrap.wrap(string, max_width) returns wrapping in a list
    #textwrap.fill(string, max_width) return the list as a single multiline string
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
