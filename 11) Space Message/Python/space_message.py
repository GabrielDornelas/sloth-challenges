def spaceMessage(message):
    decrypted = []
    index = 0
    size = len(message)

    while index < size:
        if message[index] == '[':
            index += 1

            num_str = ''
            while index < size and message[index].isdigit():
                num_str += message[index]
                index += 1

            num = int(num_str) if num_str else 0

            text = ''
            while index < size and message[index] != ']':
                text += message[index]
                index += 1

            index += 1

            if num > 0 and text:
                decrypted.append(text * num)
            elif text:
                decrypted.append(text)
        else:
            decrypted.append(message[index])
            index += 1
    
    return ''.join(decrypted)

if __name__ == '__main__':
    print(spaceMessage("ABCD"))
    print(spaceMessage("AB[3CD]"))
    print(spaceMessage("IF[2E]LG[5O]D"))
    print(spaceMessage("[3]AB"))
