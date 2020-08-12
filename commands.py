# commands_total = [
#     'look',
#     'l',
#     'points',
#     'p',
#     'map',
#     'm',
#     'help',
#     'h',
#     'exit',
#     'quit'
# ]
commands_total = {
    'look': ['look', 'l'],
    'points': ['points', 'p'],
    'map': ['map', 'm'],
    'help': ['help', 'h'],
    'exit': ['exit', 'quit'],
    'northwest': ['northwest', 'nw'],
    'north': ['north', 'n'],
    'northeast': ['northeast', 'ne'],
    'west': ['west', 'w'],
    'east': ['east', 'e'],
    'southwest': ['southwest', 'sw'],
    'south': ['south', 's'],
    'southeast': ['southeast', 'se']
}

def commands(inp, conductor, go_to, original, picked_up):
    # print the outcome of external commands from user input.
    #   
    # Arguments:
    #   
    #   inp: user input string
    #   conductor: player object
    #   go_to: quest destination city_id
    #   original: home city_id
    #   picked_up: current cargo hold boolean
    #   
    #   
    #   
    #   
    #   
    game_exit(inp)

    if inp == 'look':
        look()
        return 1
    elif inp == 'points':
        points()
    elif inp == 'map':
        map()
    elif inp == 'help':
        return 1
    else:
        return 0


def game_exit(inp):
    # kill the program when the input is 'exit' or 'quit'
    if inp.lower() == 'exit':
    # if inp == 'exit' or inp == 'quit':
        print('Adios!')
        exit()

def look():
    conductor.location.printCity()
    print(goTo(go_to, conductor, original, picked_up))

def points():
        print('Points:', conductor.points)

def map():
    f = open('ascii-map-labeled.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

# def help:



help_text = ''' 
Explore Mexico with your small start-up train!
To move from city to city, type in the cardinal direction indicated, not the desired city.
    Example:    "Southwest:    Morelia"
    To travel to Morelia, input 'Southwest' or 'southwest' or 'sw'.
Other commands:
    'exit' or 'quit' - exit the game
    'look' or 'l' - print the current city's name, quest, and available cities.
    'points' or 'p' - print your current score
    'map' or 'm' - print out a reference map of Mexico
'''