"""Starter code for CSC108 Assignment 1 Winter 2018"""
# Game setting constants
SECTION_LENGTH = 3
ANSWER = 'CATDOGFOXEMU'
used_gamestates = []

# Move constants
SWAP = 'S'
ROTATE = 'R'
CHECK = 'C'

# Add any additional constants here

def get_section_start(section_num: int) -> int:
    """ Return the starting index of the section corresponding to section_num.
    
    >>> get_section_start(1)
    0
    >>> get_section_start(3)
    6
    """
    return (section_num - 1) * SECTION_LENGTH

def is_valid_move(char):
    """(str) -> bool

    Return True if and only if char represents one of the three move
    constants.

    >>> is_valid_move('S')
    True

    >>> is_valid_move('X')
    False
    """
    valid_moves = ['S','R','C']
    return char in valid_moves
       

def is_valid_section(section_num):
    """(int) -> bool

    Return True if and only if section_num is within the range of the answer
    string and section length

    >>> is_valid_section(3)
    True

    >>> is_valid_section(5)
    False
    """
    return get_section_start(section_num) <= (len(ANSWER) - SECTION_LENGTH)

def check_section(game_state, valid_section):
    """(str, int) -> bool

    Return True if and only if the game_state in valid_section matches
    the same section in the answer string. ie return True if the specified
    section is correctly unscrambled.

    >>> check_section('CATDOGFOXEMU', 1)
    True

    >>> check_section('ACTDOGFOXEMU', 1)
    False
    """
    ind = get_section_start(valid_section)
    return game_state[ind: ind + SECTION_LENGTH] == ANSWER[ind: ind + SECTION_LENGTH]
    
def change_state(game_state, section_num, move):
    """(str, int, str) -> str

    Return a new string that takes current game_state and applies the given move
    (either 'S' or 'R') to section section_num.

    >>> change_state('wrdokoclgmae', 2, 'S')
    'wrdolockgmae'

    >>> change_state('ACTGODOXFMUE', 2, 'R')
    'ACTDGOOXFMUE'
    """
    split_str = list(game_state)
    ind = get_section_start(section_num)
    end = split_str[ind + SECTION_LENGTH - 1]
    if move == 'S':
        temp = split_str[ind]
        split_str[ind] = end
        split_str[ind + SECTION_LENGTH - 1] = temp
        return ''.join(split_str)
 
    if move == 'R':
        split_str.insert(ind, end)
        del split_str[ind + SECTION_LENGTH]
        return ''.join(split_str)

def get_move_hint(game_state, section_number):
    """(str, int) -> str

    Return a hint that will help the user to unscramble the section of game_state
    indicated by section_number.

    >>> get_move_hint("CATGODFOXEMU", 2)
    'S'

    >>> get_move_hint("ATCDOGFOXEMU", 1)
    'S'
    """
    start_ind = get_section_start(section_number)
    hint_section = game_state[start_ind: start_ind + SECTION_LENGTH]
    comp_section = ANSWER[start_ind: start_ind + SECTION_LENGTH]
    
    if check_section(change_state(game_state, section_number, "S"), section_number):
        return "S"

    if check_section(change_state(game_state, section_number, "R"), section_number):
        return "R"

    if (change_state(game_state, section_number, "S") not in used_gamestates):
        used_gamestates.append(change_state(game_state, section_number, "S"))
        return "S"

    if (change_state(game_state, section_number, "R") not in used_gamestates):
        used_gamestates.append(change_state(game_state, section_number, "R"))
        return "R"
