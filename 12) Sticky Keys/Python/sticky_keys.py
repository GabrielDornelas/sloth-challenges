def isLongPressed(original, typed):
    original_len = len(original)
    typed_len = len(typed)
    i = j = 0

    while j < typed_len:
        if i < original_len and original[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False
    return i == original_len
    

if __name__ == '__main__':
    print(isLongPressed("alex", "aaleex"))
    print(isLongPressed("saeed", "ssaaedd"))
    print(isLongPressed("leelee", "lleeelee"))
    print(isLongPressed("Tokyo", "TTokkyoh"))
    print(isLongPressed("laiden", "laiden"))
