from commands import *
import numpy as np


def game_input(prompt, warning, isYN, isInt, isCommand):
    # game_input method streamlines user console input.
    # Three types of user input to return:
    #   Y/N input
    #   integer input
    #   command
    #   otherwise
    #
    #   input is received (using Python's builtin input function), game_exit (from commands file) is checked,
    #   and strings are reviewed depending on the arguments:
    #   
    #       prompt: input prompt from the program (ex. '> ')
    #       warning: repeated error string on improper user input (ex. 'not a number, input a number')
    #       isYN: boolean indicator as to whether the input requires a yes/no response or not.
    #       isInt: boolean indicator as to whether the input requires a number.
    #       isCommand: boolean indicator as to whether the input is a move/command.
    #   
    inp_string = input(prompt).strip() # receive input
    game_exit(inp_string) # check for exit command

    if isYN: # if yes/no response prompt
        while not (inp_string[:1].lower() == 'y' or inp_string[:1].lower() == 'n'): # looping, while the first, lowered character is not 'y' or 'n'
            print(warning) # warn user
            inp_string = input(prompt).strip() #receive input
            game_exit(inp_string) # check for exit command
        if inp_string[:1].lower() == 'y': # if first character lowered is 'y' 
            return True
        else: # else, first character must be 'n'
            return False
    elif isInt: # if integer response prompt
        castCheck = False # while loop exit boolean 
        while not castCheck:
            try:    # error check for if input is not number
                inp_int = int(inp_string) # cast to int
                castCheck = True # end while
            except ValueError: # if error from number
                print(warning) # warn user
                inp_string = input(prompt).strip() # receive input
                game_exit(inp_string) # check for exit command
        return inp_int # return integer
    elif isCommand:
        # commands_total is a dictionary of keys with multiple values per key.
        # to isolate just the values, commands_total.values() gives a 2D list (when cast to list) of grouped values.
        # numpy.darray will flatten it to 1D when the list is cast to a numpy array.
        commands_values_list = np.array(list(commands_total.values())).flatten()
        while not(inp_string in commands_values_list):
            print(warning) # warn user
            inp_string = input(prompt).strip() #receive input
            game_exit(inp_string) # check for exit command
        # after string is known to be in the values, it needs to be reassociated with its key, to return the key to the commands function.
        # the keys is cast to list, and so is the np.array (to get the index)
        # the index of the input string in the values list is an integer, going up each time the next value is found.
        # since there are two values per key, dividing by two and casting to int will ensure the correct key, which is returned at the end.
        return list(commands_total.keys())[int(list(commands_values_list).index(inp_string.lower()) / 2)]


    else: # if not a Yes/No prompt, not an int prompt and not a command prompt, is an otherwise prompt, 
        # and input string is returned without editing (ex. name input).
        return inp_string 