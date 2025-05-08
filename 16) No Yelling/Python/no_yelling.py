def noYelling(phrase: str) -> str:
    '''Transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one.
    Without changing punctuation in the middle of the sentences.

    Args:
        phrase: The input string with ! or ? at the end.

    Returns:
        str: Same phrase with just one ! or ? at the end of it.
    '''
    punctuation = phrase[-1]
    if punctuation not in '?!':
        return phrase
    array = phrase.split()
    last = array.pop()
    last = last.replace('!', '').replace('?', '')
    last += punctuation
    array.append(last)
    return ' '.join(array)
    

if __name__ == '__main__':
    inputs = [
        "What went wrong?????????",
        "Oh my goodness!!!",
        "I just!!! can!!! not!!! believe!!! it!!!",
        "Oh my goodness!"
    ]
    func = noYelling
    for item in inputs:
        print(func(item))
