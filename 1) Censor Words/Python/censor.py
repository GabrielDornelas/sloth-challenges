import re

def censor(text, length=4):
    """
    Censors words longer than a specified length in the given text,
    while preserving punctuation and special characters.
    
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

    # Splitting words and punctuation while keeping spaces
    tokens = re.findall(r'\w+|[^\w\s]|\s+', text)
    censored_tokens = [
        token if not token.isalnum() else censor_word(token)
        for token in tokens
    ]
    # Joining tokens as they are, spaces are preserved
    return ''.join(censored_tokens)

if __name__ == '__main__':
    text = '''Hello! This is an example sentence, with various punctuation: commas, periods... and symbols like @, #, $, %, &, *, and others. 
Some numbers: 12345, and some mixed: abc123. Don't forget contractions like can't, won't, or they're! 
We also have parentheses (like this), brackets [like these], braces {curly ones}, and quotes: "double" and 'single'. 
Even slashes /, backslashes \\, and underscores _ are here. Ready to censor?
'''
    print("Original Text:")
    print(text)
    print("\nCensored Text:")
    print(censor(text))
