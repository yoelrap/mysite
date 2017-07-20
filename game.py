import os
import random

WORD_FILE = os.path.abspath(os.path.join(os.path.split(__file__)[0], "words.txt"))
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
MAX_ERRORS = 6

def choose_word():
    words = open(WORD_FILE).readlines()

    # in case we have empty lines, we'll keep looping until
    # we get a word that has some letters in it
    word = ''
    while len(word) == 0:
        word = random.choice(words).strip().lower()
    return word

def reset_state(word):
    """return an empty game state"""

    return {
        'errors': 0,
        'word': word,
        'guessed': ['_'] * len(word),
        'chosen': [],
        'message': None,
    }

def turn(state, letter):
    """
    Pass in the current state and a letter choice.

    Update the state and return an updated state. If there is anything to
    be displayed, it will be stored in state['message']
    """
    letter = letter.lower()
    state['message'] = None

    # check to see if the letter passed is valid other
    # set the error
    if len(letter) != 1 or letter.lower() not in LETTERS:
        state['message']  = "Bad letter %s" % letter
        return state

    # Is the letter is not in the letters list, we must have already
    # chosen it the show a letter.
    if letter in state['chosen']:
        state['message'] = "ERROR: Repeated letter"
        return state

    # delete the letter from the letters list so that we cannot choose it again
    state['chosen'].append(letter)

    if letter not in state['word']:
        state['errors'] += 1
    else:
        guessed = state['guessed']
        for pos, let in enumerate(list(state['word'])):
            if letter == let:
                guessed[pos] = letter
        state['guessed'] = guessed

    # if we have 6 errors then it is game over
    if state['errors'] == MAX_ERRORS:
        state['message'] = "You LOOSE, word was '%s'" % state['word']
        state['chosen'] = LETTERS

    # if there are no more blank characters in guessed then we have won
    if '_' not in state['guessed']:
        state['message'] = "You win, word was '%s'. You had %d turns left" % (
            state['word'], MAX_ERRORS - state['errors'])
        state['chosen'] = LETTERS

    return state
