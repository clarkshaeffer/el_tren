from conductor import Conductor
from city import *
# import city as cit
# import numpy.core.defchararray as numpy
from numpy.core.defchararray import *
import random
import time


def main():
    intro()

    player = Conductor(getAllCitiesList()[setHome()], 0)
    player.location.printCity()

    game_over = False
    while not game_over:
        dropped_off = False
        go_to_id = getRandomCity().city_id
        while go_to_id == player.location.city_id:
            go_to_id = getRandomCity().city_id
        original_id = player.location.city_id
        picked_up = False
        new_go_to = True
        # goTo(go_to_id, player, original_id, picked_up)
        while not dropped_off:

            if new_go_to:
                print(goTo(go_to_id, player, original_id, picked_up))
                new_go_to = False
            
            inputText = input('> ')
            try:
                if commands(inputText, player, go_to_id, original_id, picked_up) == 0:
                    player.location = eval(move(inputText, player.location.directions_possible, player.location.cities_possible))
                    player.location.printCity()
            except TypeError:
                print('Whoops! Try again. For help, type \'help\' or \'h\'.')

            
            if player.location.city_id == go_to_id and not picked_up:
                print(goTo(go_to_id, player, original_id, picked_up))
                picked_up = True
            elif player.location.city_id == original_id and picked_up:
                dropped_off = True
                player.points += 1
                print(goTo(go_to_id, player, original_id, picked_up))


def intro():
    inp = lower(input('Intro? (y/n) > '))
    game_exit(inp)
    if inp == 'y' or inp == 'yes':
        for i in range(len(intro_ascii_text)):
            print(intro_ascii_text[i], end='', flush = True)
            time.sleep(.005)
        print('\n\n\n')
        time.sleep(.75)


def setHome():
    print('\nWhere are you from? Choose a number:\n')
    time.sleep(.50)
    for i in range(len(getAllCitiesList())):
        print(getAllCitiesList()[i].city_id, getAllCitiesList()[i].name)
        time.sleep(.04)
    print()
    ready = False
    while not ready:
        inp_num = input('> ')
        game_exit(inp_num)

        try:
            if int(inp_num) > 0 and int(inp_num) <= len(getAllCitiesList()):
                print("You're from {}? (y/n)".format(getShortName(getAllCitiesList()[int(inp_num)])))
                inp_ready = lower(input('> '))
                game_exit(inp_ready)
                if inp_ready == 'y' or inp_ready == 'yes':
                    ready = True
                else:
                    print('Choose a number from the cities listed.')
        except ValueError:
            print('Choose a number from the cities listed.')
    return int(inp_num)


def goTo(go_to, conductor, original, pickup):
    go_to_name = ''.join(getShortName(getAllCitiesList()[go_to]))

    original_name = ''.join(getShortName(getAllCitiesList()[original]))

    if conductor.location.city_id != go_to and not pickup:
        return 'Go to {}.'.format(go_to_name)
    elif conductor.location.city_id != go_to and conductor.location.city_id != original and pickup:
        return 'Return to {}.'.format(original_name)
    elif conductor.location.city_id == go_to and not pickup:
        pickup = True
        return 'Cargo picked up. Now return to {}.'.format(original_name)
    elif conductor.location.city_id == go_to and pickup:
        return 'Return to {}.'.format(original_name)
    elif conductor.location.city_id == original and pickup:

        return 'Dropped off! Points: {}'.format(conductor.points)


def getRandomCity():
    x = random.randint(0,31)
    return getAllCitiesList()[x]


def commands(inp, conductor, go_to, original, picked_up):
    game_exit(inp)
    if inp == 'look' or inp == 'l':
        conductor.location.printCity()
        print(goTo(go_to, conductor, original, picked_up))
        return 1
    elif inp == 'points' or inp == 'p':
        print('Points:', conductor.points)
    elif inp == 'map' or inp == 'm':
        f = open('ascii-map-labeled.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
    elif inp == 'help' or inp == 'h':
        print(
'''Explore Mexico with your small start-up train!
To move from city to city, type in the cardinal direction indicated, not the desired city.
    Example:    "Southwest:    Morelia"
    To travel to Morelia, input 'Southwest' or 'southwest' or 'sw'.
Other commands:
    'exit' or 'quit' - exit the game
    'look' or 'l' - print the current city's name, quest, and available cities.
    'points' or 'p' - print your current score
    'map' or 'm' - print out a reference map of Mexico
        ''')
        return 1
    else:
        return 0


def move(inp, dir_list, city_list):
    move_index = inputDirection(inp, dir_list)
    # print(move_index)
    move_to = str(lower(city_list[move_index]))
    move_to_list = list(move_to)
    for i in range(len(move_to_list)):
        if move_to_list[i] == ' ':
            move_to_list[i] = '_'
    move_to = ''.join(move_to_list)
    return move_to


def inputDirection(inp, dir_list):
    fail = False
    for i in range(len(dir_list)):
        if (inp == 'nw' or inp == 'NW' or inp == 'northwest' or inp == 'Northwest') and dir_list[i] == nw:
            return i
        elif (inp == 'n' or inp == 'N' or inp == 'north' or inp == 'North') and dir_list[i] == n:
            return i
        elif (inp == 'ne' or inp == 'NE' or inp == 'northeast' or inp == 'Northeast') and dir_list[i] == ne:
            return i
        elif (inp == 'w' or inp == 'W' or inp == 'west' or inp == 'West') and dir_list[i] == w:
            return i
        elif (inp == 'e' or inp == 'E' or inp == 'east' or inp == 'East') and dir_list[i] == e:
            return i
        elif (inp == 'sw' or inp == 'SW' or inp == 'southwest' or inp == 'Southwest') and dir_list[i] == sw:
            return i
        elif (inp == 's' or inp == 'S' or inp == 'south' or inp == 'South') and dir_list[i] == s:
            return i
        elif (inp == 'se' or inp == 'SE' or inp == 'southeast' or inp == 'Southeast') and dir_list[i] == se:
            return i
        else:
            fail = True
    if fail:
        return 'fail'

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

def game_exit(inp):
    if lower(inp) == 'exit' or lower(inp) == 'quit':
        print('Adios!')
        exit()

main()