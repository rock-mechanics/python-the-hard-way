def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words"""
    return sorted(words)

def print_first_word(words):
    """print the first word after poping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """print the last word after poping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """take in a full sentence and return sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the first and last word of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sort the words and then print the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# help(module-name) will show all the comments after function in the python intepreter

# from .. import .., import the function, but the function can access its neighbouring functions in the same module.
