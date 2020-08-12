# Loco-Motive by Clark Shaeffer         https://github.com/clarkshaeffer/el_tren
# 
# TO DO:
#   Code organization:
#       Fix commands mess (not directions + other, but all one)
#       User input fix across game
#       Ciudad de Mexico short name has 2 periods.
#       Finish documentation on current edition
#       More files for more functions. Keep it clean in the main. 
#       
#
#   Separate quests:
#       Home - goto - home
#       goto - destination
#
#   City-specific events
#
#   A city's main exports
#
#
#
#
#

#     Functions:
#           main
#           intro
#           setHome
#           goTo
#           getRandomCity
#           commands
#           move
#           inputDirection
#           game_exit
#       Objects:
#            City
#            Conductor

import os
from conductor import Conductor
from city import *
# import city as cit
# import numpy.core.defchararray as np
# from numpy.core.defchararray import *
# import random
from quest import Quest
from intro import *
from commands import *
from game_input import game_input





def main():
    #clear terminal window before starting game
    os.system('clear') 
    # Prompt to show intro
    intro() 
    # Set player's home point using setHome; access from getAllCitiesList
    player = Conductor(getAllCitiesList()[setHome()], 0)
    #First city_print (method from City object - print current city, state, options, and possibly destination.)
    player.location.printCity() 


    # Game really starts. Overarching while loop begins.
    game_over = False
    while not game_over:
        # New cargo  
        dropped_off = False
        # get random new destination city
        go_to_id = getRandomCity().city_id
        while go_to_id == player.location.city_id: # if the destination is the player's location
            go_to_id = getRandomCity().city_id
        #return city is current location, a.k.a. home from setHome().
        original_id = player.location.city_id
        picked_up = False
        # First time with a new destination - quest printed in printCity()
        new_go_to = True
        # goTo(go_to_id, player, original_id, picked_up)
        while not dropped_off:

            # if first time with new pickup quest, print in printCity() and don't do it again
            if new_go_to:
                print(goTo(go_to_id, player, original_id, picked_up))
                new_go_to = False
            
            # receive move input
            

            inputText = game_input('> ', 'Whoops! Try again. For help, type \'help\' or \'h\'.', False, False, True)
            try:
                # If input is not an alternate command (look, map, etc). a.k.a. if input is a cardinal direction:
                if commands(inputText, player, go_to_id, original_id, picked_up) == 0:
                    # move to input direction (1) if in directions possible (2) and set location to associated city (3)
                    player.location = eval(move(inputText, player.location.directions_possible, player.location.cities_possible))
                    # print new city
                    player.location.printCity()
            except TypeError:
                # 
                print('Whoops! Try again. For help, type \'help\' or \'h\'.')

            
            if player.location.city_id == go_to_id and not picked_up:
                print(goTo(go_to_id, player, original_id, picked_up))
                picked_up = True
            elif player.location.city_id == original_id and picked_up:
                dropped_off = True
                player.points += 1
                print(goTo(go_to_id, player, original_id, picked_up))






def goTo(go_to, conductor, original, pickup):
    # return string of current cargo quest fulfillment.
    # 
    # Arguments:
    # 
    # go_to: city_id of quest city
    # conductor: player object
    # original: city_id of home
    # pickup: boolean of if cargo is picked up. Determines direction: going to quest city or returning.

    go_to_name = ''.join(getShortName(getAllCitiesList()[go_to])) # name is shortened name of go_to city (function in city.py)

    original_name = ''.join(getShortName(getAllCitiesList()[original])) # shortened name of home city

    if conductor.location.city_id != go_to and not pickup: # if going to pick up
        return 'Go to {}.'.format(go_to_name)
    elif conductor.location.city_id != go_to and conductor.location.city_id != original and pickup: # if returning
        return 'Return to {}.'.format(original_name)
    elif conductor.location.city_id == go_to and not pickup: # if at pickup location, now picked up
        pickup = True
        return 'Cargo picked up. Now return to {}.'.format(original_name)
    # elif conductor.location.city_id == go_to and pickup: # if at pickup location, and already picked up
    #     return 'Return to {}.'.format(original_name)
    elif conductor.location.city_id == original and pickup: # if returned with cargo
        return 'Dropped off! Points: {}'.format(conductor.points)






def move(inp, dir_list, city_list):
    move_index = inputDirection(inp, dir_list)
    move_to = str(city_list[move_index].lower())
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


main()