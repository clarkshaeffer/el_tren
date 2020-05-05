mexicali_t = 'Mexicali'
la_paz_t = 'La Paz'
hermosillo_t = 'Hermosillo'
culiacan_t = 'Culiacan'
chihuahua_t = 'Chihuahua'
durango_t = 'Durango'
saltillo_t = 'Saltillo'
monterrey_t = 'Monterrey'
ciudad_victoria_t = 'Ciudad Victoria'
zacatecas_t = 'Zacatecas'
san_luis_potosi_t = 'San Luis Potosi'
aguascalientes_t = 'Aguascalientes'
guanajuato_t = 'Guanajuato'
queretaro_t = 'Queretaro'
tepic_t = 'Tepic'
guadalajara_t = 'Guadalajara'
morelia_t = 'Morelia'
colima_t = 'Colima'
pachuca_t = 'Pachuca'
tlaxcala_t = 'Tlaxcala'
ciudad_de_mexico_t = 'Ciudad de Mexico'
toluca_t = 'Toluca'
cuernavaca_t = 'Cuernavaca'
puebla_t = 'Puebla'
xalapa_t = 'Xalapa'
chilpancingo_t = 'Chilpancingo'
oaxaca_t = 'Oaxaca'
tuxtla_gutierrez_t = 'Tuxtla Gutierrez'
villahermosa_t = 'Villahermosa'
campeche_t = 'Campeche'
merida_t = 'Merida'
chetumal_t = 'Chetumal'

nw =    'Northwest'
n =     'North'
ne =    'Northeast'
w =     'West'
e =     'East'
sw =    'Southwest'
s =     'South'
se =    'Southeast'
shortTab =      ':    '
northSouthTab = ':        '
westEastTab =   ':         '

class City():
    def __init__(self, name, directions_possible, cities_possible, city_id):
        self.name = name
        # self.description = description
        self.directions_possible = directions_possible
        self.cities_possible = cities_possible
        self.city_id = city_id
    
    def printCity(self):
        print(self.name)
        print('-------')
        for i in range(len(self.directions_possible)):
            print(self.directions_possible[i], end = '')
            print(self.tab(self.directions_possible[i]), end = '')
            print(self.cities_possible[i])
        print()
    
    # def getDirectionsPossible(self):
    #     return self.directions_possible

    # def getCitiesPossible(self):
    #     return self.cities_possible
    
    def tab(self, direction):
        if direction == nw:
            return shortTab
        elif direction == n:
            return northSouthTab
        elif direction == ne:
            return shortTab
        elif direction == w:
            return westEastTab
        elif direction == e:
            return westEastTab
        elif direction == sw:
            return shortTab
        elif direction == s:
            return northSouthTab
        elif direction == se:
            return shortTab



# North = 6
# Northeast = 3
# Central = 5
# West = 4
# Capital = 6
# Coast = 5
# Peninsula = 3

all_cities_list = []
#NORTH
mexicali = City('Mexicali, Baja California.',
[s, se],
[la_paz_t, hermosillo_t],
0)
all_cities_list.append(mexicali)

la_paz = City('La Paz, Baja California Sur.',
[n],
[mexicali_t],
1)
all_cities_list.append(la_paz)

hermosillo = City('Hermosillo, Sonora.', 
[nw, e, se],
[mexicali_t, chihuahua_t, culiacan_t],
2)
all_cities_list.append(hermosillo)

culiacan = City('Culiacan, Sinaloa.',
[nw, ne, e, se],
[hermosillo_t, chihuahua_t, durango_t, tepic_t],
3)
all_cities_list.append(culiacan)

chihuahua = City('Chihuahua, Chihuahua.',
[w, sw, s, se],
[hermosillo_t, culiacan_t, durango_t, saltillo_t],
4)
all_cities_list.append(chihuahua)

durango = City('Durango, Durango.',
[n, w, e, s, se],
[chihuahua_t, culiacan_t, saltillo_t, tepic_t, zacatecas_t],
5)
all_cities_list.append(durango)

#NORTHEAST
saltillo = City('Saltillo, Coahuila.',
[nw, w, e, sw],
[chihuahua_t, durango_t, monterrey_t, zacatecas_t],
6)
all_cities_list.append(saltillo)

monterrey = City('Monterrey, Nuevo Leon.',
[w, s, se],
[saltillo_t, san_luis_potosi_t, ciudad_victoria_t],
7)
all_cities_list.append(monterrey)

ciudad_victoria = City('Ciudad Victoria, Tamaulipas.',
[nw, sw],#se
[monterrey_t, san_luis_potosi_t],#xalapa_t
8)
all_cities_list.append(ciudad_victoria)

#CENTRAL
zacatecas = City('Zacatecas, Zacatecas.',
[nw, ne, s, se],
[durango_t, saltillo_t, aguascalientes_t, san_luis_potosi_t],
9)
all_cities_list.append(zacatecas)

san_luis_potosi = City('San Luis Potosi, San Luis Potosi.',
[nw, n, ne, w, s],
[zacatecas_t, monterrey_t, ciudad_victoria_t, aguascalientes_t, guanajuato_t],
10)
all_cities_list.append(san_luis_potosi)

aguascalientes = City('Aguascalientes, Aguascalientes.',
[n, e, sw, se],
[zacatecas_t, san_luis_potosi_t, guadalajara_t, guanajuato_t],
11)
all_cities_list.append(aguascalientes)

guanajuato = City('Guanajuato, Guanajuato.',
[nw, n, w, s, se],
[aguascalientes_t, san_luis_potosi_t, guadalajara_t, morelia_t, queretaro_t],
12)
all_cities_list.append(guanajuato)

queretaro = City('Queretaro, Queretaro.',
[nw, e, sw, s, se],
[guanajuato_t, pachuca_t, morelia_t, toluca_t, ciudad_de_mexico_t],
13)
all_cities_list.append(queretaro)

# WEST
tepic = City('Tepic, Nayarit.',
[n, ne, se],
[durango_t, zacatecas_t, guadalajara_t],
14)
all_cities_list.append(tepic)

guadalajara = City('Guadalajara, Jalisco.',
[nw, ne, e, s, se],
[tepic_t, aguascalientes_t, guanajuato_t, colima_t, morelia_t],
15)
all_cities_list.append(guadalajara)

morelia = City('Morelia, Michoacan.',
[nw, n, ne, w, e],
[guadalajara_t, guanajuato_t, queretaro_t, colima_t, toluca_t],
16)
all_cities_list.append(morelia)

colima = City('Colima, Colima.',
[n, e],
[guadalajara_t, morelia_t],
17)
all_cities_list.append(colima)

#CAPITAL

pachuca = City('Pachuca, Hidalgo.',
[w, s], #se
[queretaro_t, ciudad_de_mexico_t], #tlaxcala
18)
all_cities_list.append(pachuca)

tlaxcala = City('Tlaxcala, Tlaxcala.',
[e, s], #nw, w
[xalapa_t, puebla_t], #pachuca_t, ciudad_de_mexico_t
19)
all_cities_list.append(tlaxcala)

ciudad_de_mexico = City('La Ciudad de Mexico.',
[nw, n, w, s, se],
[queretaro_t, pachuca_t, toluca_t, cuernavaca_t, puebla_t],
20)
all_cities_list.append(ciudad_de_mexico)

toluca = City('Toluca, Estado de Mexico.',
[n,w,e], #se
[queretaro_t, morelia_t, ciudad_de_mexico_t], #cuernavaca_t
21)
all_cities_list.append(toluca)

cuernavaca = City('Cuernavaca, Morelos.',
[n,e,s], #nw
[ciudad_de_mexico_t, puebla_t, chilpancingo_t], #toluca_t
22)
all_cities_list.append(cuernavaca)

puebla = City('Puebla, Puebla.',
[nw, n, w, se], #ne, sw
[ciudad_de_mexico_t, tlaxcala_t, cuernavaca_t, oaxaca_t], #xalapa_t, chilpancingo_t
23)
all_cities_list.append(puebla)

#COAST
xalapa = City('Xalapa, Veracruz.',
[w, se], #sw
[tlaxcala_t, villahermosa_t], #puebla_t
24)
all_cities_list.append(xalapa)

chilpancingo = City('Chilpancingo, Guerrero.',
[n, e], #ne
[cuernavaca_t, oaxaca_t], #puebla
25)
all_cities_list.append(chilpancingo)

oaxaca = City('Oaxaca, Oaxaca.',
[nw, w, e],
[puebla_t, chilpancingo_t, tuxtla_gutierrez_t],
26)
all_cities_list.append(oaxaca)

tuxtla_gutierrez = City('Tuxtla Gutierrez, Chiapas.',
[n, w],
[villahermosa_t, oaxaca_t],
27)
all_cities_list.append(tuxtla_gutierrez)

villahermosa = City('Villahermosa, Tabasco.',
[nw, ne, s],
[xalapa_t, campeche_t, tuxtla_gutierrez_t],
28)
all_cities_list.append(villahermosa)

#PENINSULA
campeche = City('Campeche, Campeche.',
[n, e, sw],
[merida_t, chetumal_t, villahermosa_t],
29)
all_cities_list.append(campeche)

merida = City('Merida, Yucatan.',
[s, se],
[campeche_t, chetumal_t],
30)
all_cities_list.append(merida)

chetumal = City('Chetumal, Quintana Roo.',
[nw, w],
[merida_t, campeche_t],
31)
all_cities_list.append(chetumal)


def getAllCitiesList():
    return all_cities_list

def getShortName(self):
    ##### Make a shortened name for a city
    name_list = []
    for i in range(len(self.name)):
        if self.name[i] != ',':# or self.name[i] != '.':
            name_list.append(self.name[i])
        else:
            break
    return ''.join(name_list)
    ####



# def direction_full(self, inputText):
    #     if inputText == nw:
    #         print('Northwest', end = '')
    #     elif inputText == 'n':
    #         print('North', end = '')
    #     elif inputText == 'ne':
    #         print('Northeast', end = '')
    #     elif inputText == 'w':
    #         print('West', end = '')
    #     elif inputText == 'e':
    #         print('East', end = '')
    #     elif inputText == 'sw':
    #         print('Southwest', end = '')
    #     elif inputText == 's':
    #         print('South', end = '')
    #     elif inputText == 'se':
    #         print('Southeast', end = '')
    #     else:
    #         print('nothing', end = '')