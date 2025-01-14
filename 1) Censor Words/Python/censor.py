import re

def censor(text, length=4):
    """
    Censors words longer than a specified length in the given text,
    while preserving punctuation.
    
    Args:
        text (str): The input text to censor.
        length (int): The minimum length of a word to be censored.
        
    Returns:
        str: The censored text.
    """
    def censor_word(word):
        if len(word) > length:
            return '*' * len(word)
        return word

    # Using re to split words and keep punctuation
    tokens = re.findall(r'\w+|\S', text)
    censored_tokens = [censor_word(token) if token.isalpha() else token for token in tokens]
    return ''.join(
        (token if token in '.,!?;:' else token + ' ') for token in censored_tokens
    ).strip()

if __name__ == '__main__':
    text = '''Each page turns into a new opportunity to learn something new.
    By organizing ideas, we find balance between practice and planning, turning goals into achievements!'''
    print("Original Text:")
    print(text)
    print("\nCensored Text:")
    print(censor(text))
