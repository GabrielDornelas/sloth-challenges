def bridgeShuffle(array1, array2):
    final = []
    array1_size = len(array1)
    array2_size = len(array2)
    size = max(array1_size, array2_size)
    for index in range(size):
        if index < array1_size:
            final.append(array1[index])
        if index < array2_size:
            final.append(array2[index])
    return final

if __name__ == '__main__':
    print(bridgeShuffle(["A", "A", "A"], ["B", "B", "B"]))
    print(bridgeShuffle(["C", "C", "C", "C"], ["D"]))
    print(bridgeShuffle([1, 3, 5, 7], [2, 4, 6]))
