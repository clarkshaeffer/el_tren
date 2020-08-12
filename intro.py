from commands import game_exit
import time
from city import *
from game_input import game_input

def intro():
    # print ASCII intro (at bottom of code) if response is a form of 'yes'.
    if (game_input('Intro? (y/n) > ', 'Intro? (y/n) > ', True, False, False)): # if input is 'y' from the prompt
        for i in range(len(intro_ascii_text)): # go through each intro character
            print(intro_ascii_text[i], end='', flush = True) # print the character with no newline and 
            # flush for console reinterpretation (animation)
            time.sleep(.005) # wait to print next character, to scroll output
        print('\n\n\n') # newline buffer
        time.sleep(.75) # wait before continuing, take a look at the intro (even if it is cheesy)


def setHome():
    # Player chooses home from number options
    print('\nWhere are you from? Choose a number:\n') #prompt
    time.sleep(.50) # wait for the user to read
    for i in range(len(getAllCitiesList())): # go through each city object in the cities list array
        print(getAllCitiesList()[i].city_id, getAllCitiesList()[i].name) #print the city number and name
        time.sleep(.04) # wait before printing the next to scroll through the options
    print() # newline buffer

    ready = False # for user double-checking
    while not ready: 
        inp_num = -1 # number check for in range of all cities
        while inp_num < 0 or inp_num > (len(getAllCitiesList()) - 1): # while not in range
            inp_num = game_input('> ', 'Choose a number from the cities listed.', False, True, False) # receive number input
        # user check string: the city_id chosen in inp_num retrieves the shortened name of the city in the cities list.
        double_check = "You're from {}? (y/n) > ".format(getShortName(getAllCitiesList()[inp_num]))
        if game_input(double_check, double_check, True, False, False): # if double checked
            ready = True
        else: # if double check fail (user is indecisive)
            print('Choose a number from the cities listed.')
    return inp_num # return home city_id



intro_ascii_text = '''
                    |_   _  |_   .  _       _       _
                \)/ | ) (_| |_   | _)   \/ (_) |_| |
                                        /


    __    ____   ______ ____          __  ___ ____  ______ ____ _    __ ______ ___
   / /   / __ \ / ____// __ \        /  |/  // __ \/_  __//  _/| |  / // ____//__ \ 
  / /   / / / // /    / / / /______ / /|_/ // / / / / /   / /  | | / // __/    / _/
 / /___/ /_/ // /___ / /_/ //_____// /  / // /_/ / / /  _/ /   | |/ // /___   /_/
/_____/\____/ \____/ \____/       /_/  /_/ \____/ /_/  /___/   |___//_____/  (_)

''' #Straight + Slant (fitted) from patorjk.com/software/taag/