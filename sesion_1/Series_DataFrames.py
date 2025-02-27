# Importamos la biblioteca pandas y la llamamos pd 
import pandas as pd 
# Creamos una Serie de pandas que es como una lista con etiquetas 
# Los valores son nombres de jugadores de PSG
# El índice especifica los números de camisetas de esos jugadores
psg_players = pd.Series (
    ['Navas', 'Mbappe', 'Neymar', 'Messi']#, # Lista de jugadores
#    index = [1, 7, 10, 30] # Lista de Camisetas
)
# Creamos un diccionario que asocia números de camisetas con nombres de jugadores
psg_dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}
# Creamos una Serie de Pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)
# Imprimimos la serie creada a partir del diccionario
print(psg_players_dict)
# Imprimimos el valor en la posición (indice) 7 de la Serie creada a partir del diccionario
print(psg_players_dict[7])
# Diccionario con datos de jugadores
dict = { 'Jugador' : ['Navas', 'Mbappe', 'Neymar', 'Messi'],
        'Altura': [183.0, 170.0, 170.0, 165.0],
        'Goles' : [2, 200, 150, 200]}