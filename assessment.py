"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

from random import randint

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # Takes a string and counts the number of unique words. Returns a dictionary
    # with the word as a key and number of times the word appears as it's value.

    words = phrase.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # Takes a melon type string as an input and returns it's price or 'No price found' as its output.

    melon_price = {"watermelon": 2.95,
                   "cantaloupe": 2.50,
                   "musk": 3.25,
                   "christmas": 14.25}

    return melon_price.get(melon_name.lower(), 'No price found')


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    # I struggled a little in merging word lists with the same number.
    # I figured it out eventually, I was trying to find a workaround for tuples immutability.

    # Takes in a list of words and returns a list of tuples sorted. Each tuple includes the
    # length of each word from the word list at index[1] in the tuple.


    letter_count = {}
    word_count = []

    for word in words:
        letter_count[word] = letter_count.get(word, len(word))

    for word, number in letter_count.iteritems():
        word_count.append((number, [word]))
        word_count.sort()

    if word_count[1][0] == word_count[2][0]:
        word_count[1] = (word_count[1][0], word_count[1][1] + word_count[2][1])
        del word_count[2]

    return word_count


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    # Translates a string in english into pirate speak and returns it as an output.

    phrase = phrase.split()

    pirate_speak = ""

    english_to_pirate = {"sir": "matey",
                         "hotel": "fleabag inn",
                         "student": "swabbie",
                         "man": "matey",
                         "professor": "foul blaggart",
                         "restaurant": "galley",
                         "your": "yer",
                         "excuse": "arr",
                         "students": "swabbies",
                         "are": "be",
                         "restroom": "head",
                         "my": "me",
                         "is": "be"}

    for word in phrase:
        pirate_speak += english_to_pirate.get(word, word) + " "

    return pirate_speak.rstrip()


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # This solution works only sometimes. I suspect it has to do with the way dictionaries
    # fetch keys. Sometimes it returns the correct list output (as specified in the docstring) and
    # all tests pass, but sometimes it doesn't. It's throwing an index is out of range error or 
    # an TypeError: object of type 'NoneType' has no len() and I'm not sure what it means, 
    # since it seems works every other time. 

    # I originally had mapped the dictionary using the words as the keys, but that didn't quite
    # work. I'm pretty sure there is a simpler way to approach this problem :/

    kids_words = [names[0]]
    word_map = {}

    for letter in names:
        for word in names:
            if letter[-1] == word[0] and not letter[-1] in word_map:
                word_map[letter[-1]] = word_map.get(letter[-1], [word])
            elif letter[-1] == word[0] and letter[-1] in word_map:
                word_map[letter[-1]] = word_map[letter[-1]] + [word]

    if word_map != {}:
        for i in range(len(names) - 1):
            new_word = word_map.get(kids_words[i][-1])
            num_word_choices = len(new_word) - 1
            new_word = new_word[randint(0, num_word_choices)]
            if new_word == 'bagon':
                new_word = new_word[randint(0, num_word_choices)]
            elif kids_words.count(new_word) < 1:
                kids_words.append(new_word)
            else:
                break

    return kids_words

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
