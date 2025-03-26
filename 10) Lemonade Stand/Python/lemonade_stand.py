def lemonade(bills):
    cashier = {'5': 0, '10': 0, '20': 0}
    for payment in bills:
        match payment:
            case 5:
                cashier['5'] += 1
            case 10:
                if cashier['5'] < 1:
                    return False
                cashier['5'] -= 1
                cashier['10'] += 1
            case 20:
                if cashier['10'] > 0 and cashier['5'] > 0:
                    cashier['10'] -= 1
                    cashier['5'] -= 1
                elif cashier['5'] >= 3:
                    cashier['5'] -= 3
                else:
                    return False
                cashier['20'] += 1
    return True

if __name__ == '__main__':
    print(lemonade([5, 5, 5, 10, 20]))
    print(lemonade([5, 5, 10, 10, 20]))
    print(lemonade([10, 10]))
    print(lemonade([5, 5, 10]))
