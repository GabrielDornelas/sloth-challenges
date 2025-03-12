def turnCalc(num):
    string = str(num).replace('.', '')
    string = reversed(string)
    ref = {
        '1': 'l',
        '2': 'Z',
        '3': 'E',
        '4': 'H',
        '5': 'S',
        '6': 'G',
        '7': 'L',
        '8': 'B',
        '9': '-',
        '0': 'O'
    }
    code = ''

    for n in string:
        code += ref[n]

    print(code)


if __name__ == '__main__':
    turnCalc(707)
    turnCalc(5508)
    turnCalc(3045)
    turnCalc('07734')
