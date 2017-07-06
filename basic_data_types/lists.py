if __name__ == '__main__':
    a_list = []
    command = None
    index = None
    value = None
    N = int(input())

    for i in range(N):
        inputs = str(input())
        input_arr = inputs.split(' ')
        if len(input_arr) == 1:
            command = inputs
        elif len(input_arr) == 2:
            command = input_arr[0]
            value = int(input_arr[1])
        elif len(input_arr) == 3:
            command = input_arr[0]
            index = int(input_arr[1])
            value = int(input_arr[2])

        if command == 'insert':
            a_list.insert(index, value)
        elif command == 'remove':
            a_list.remove(value)
        elif command == 'append':
            a_list.append(value)
        elif command == 'sort':
            a_list.sort()
        elif command == 'pop':
            a_list.pop()
        elif command == 'reverse':
            a_list.reverse()
        elif command == 'print':
            print(a_list)
