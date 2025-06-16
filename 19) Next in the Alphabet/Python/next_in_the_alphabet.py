def nextLetters(letters: str) -> str:
    '''
    This function returns the next letters alphabetically in a given string. If the last letter is a "Z", change the rest of the letters accordingly.

    Examples
    nextLetters("A")
    output = "B"
    'A' becomes 'B' – simple increment.

    nextLetters("ABC")
    output = "ABD"
    'C' becomes 'D' – last character changes without carry.

    nextLetters("Z")
    output = "AA"
    'Z' rolls over to 'A', and since there's no previous letter, we add a new 'A'.
    Think of it like 9 + 1 = 10, here Z + 1 = AA.

    nextLetters("CAZ")
    output = "CBA"
    'Z' → 'A' (carry), 'A' → 'B' (no carry), so "CAZ" becomes "CBA".
    Like incrementing 129 → 130 but in letters.

    nextLetters("")
    output = "A"
    Empty input is treated as 0 → return 'A'.
    Notes
    Tests will all be in CAPITALS.

    Empty inputs should return a capital "A" (as if it were in letter position 0!).

    Think about the letter "Z" like the number 9 and how it carries over to increment the next letter/digit over.

    Args:
        letters: The input string of letters.

    Returns:
        str: Next letters.
    '''
    if not letters:
        return "A"
    next_letters = ''
    carry = True
    for letter in reversed(letters):
        if carry:
            if letter == 'Z':
                next_letters = 'A' + next_letters
            else:
                next_letters = chr(ord(letter) + 1) + next_letters
                carry = False
        else:
            next_letters = letter + next_letters
    if carry:
        next_letters = 'A' + next_letters
    
    return next_letters

if __name__ == '__main__':
    func = nextLetters
    inputs = [
        "A",
        "ABC",
        "Z",
        "CAZ",
        "",
        "ZZZ",
        "AAZ",
        "XYZ",
        "ZZZZZ",
        "AAB",
        "BAZ"
    ]
    for item in inputs:
        print(f"{item}: {func(item)}")
