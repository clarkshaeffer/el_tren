from conductor import Conductor
from city import *
from numpy.core.defchararray import *
import random

def main():
    player = Conductor(getRandomCity(), 0)
    player.location.printCity()
    
    # print(directions_list)
    game_over = False
    while not game_over:
        directions_list = player.location.directions_possible
        cities_list = player.location.cities_possible
        inputText = input('> ')
        try:
            if commands(inputText, player) == 0:
                player.location = eval(move(inputText, directions_list, cities_list))
                player.location.printCity()
        except TypeError:
            print('Whoops! Try again. For help, type \'help\' or \'h\'.')
        
def getRandomCity():
    x = random.randint(0,31)
    for i in range(len(getAllCitiesList())):
        if x == getAllCitiesList()[i].city_id:
            return getAllCitiesList()[i]
        # print(getAllCitiesList()[i].directions_possible)

        
def commands(inp, conductor):
    if inp == 'exit' or inp == 'quit':
        print('Adios!')
        exit()
    elif inp == 'look' or inp == 'l':
        conductor.location.printCity()
        return 1
    elif inp == 'points' or inp == 'p':
        print('Points:', conductor.points)
    elif inp == 'help' or inp == 'h':
        print(
'''Explore Mexico with your small start-up train!
To move from city to city, type in the cardinal direction indicated, not the desired city.
    Example:    "Southwest:    Morelia"
    To travel to Morelia, input 'Southwest' or 'southwest' or 'sw'.
Other commands:
    'exit' or 'quit' - exit the game
    'look' or 'l' - print the current city's name and available cities.
    'points' or 'p' - print your current score
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

main()