from conductor import Conductor
from city import *
from numpy.core.defchararray import *
# la_paz.printCity()
# mexicali.printCity()

def main():
    
    player = Conductor(queretaro, 0)
    player.location.printCity()
    
    # print(directions_list)
    dead = False
    while not dead:
        directions_list = player.location.getDirectionsPossible()
        cities_list = player.location.getCitiesPossible()
        inputText = input('> ')
        try:
            commands(inputText)
            player.location = eval(move(inputText, directions_list, cities_list))
            player.location.printCity()
        except TypeError:
            print('Whoops! Try again.')
        
        
def commands(inp):
    if inp == 'exit' or inp == 'quit':
        print('Adios!')
        exit()

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