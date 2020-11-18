"""
>>> assert type(result) is str
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
Sentences: 7
Words: 71
Characters: 347
Letters: 283
Commas: 1
Adverbs: 0
"""

TEXT = """
    We choose to go to the Moon.
    We choose to go to the Moon in this decade and do the other things.
    Not because they are easy, but because they are hard.
    Because that goal will serve to organize and measure the best of our energies and skills.
    Because that challenge is one that we are willing to accept.
    One we are unwilling to postpone.
    And one we intend to win
"""

total_sentences = 0
total_words = 0
total_chars = 0
total_letters = 0
total_commas = 0
total_adverbs = 0


for sentence in TEXT.split('.'):

    sentence = sentence.strip()
    words = sentence.split()
    characters = sentence.replace(',', '')
    letters = characters.replace(' ', '')

    total_sentences += 1
    total_words += len(words)
    total_chars += len(characters)
    total_letters += len(letters)
    total_commas += sentence.count(',')

    for word in words:
        if word.endswith('ly'):
            total_adverbs += 1


result = f"""Sentences: {total_sentences}
Words: {total_words}
Characters: {total_chars}
Letters: {total_letters}
Commas: {total_commas}
Adverbs: {total_adverbs}"""
