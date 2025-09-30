list_of_keys = ['Heredia','Guanacaste']

Provinces_and_capitals = {
    'San Jose' : 'San Jose',
    'Alajuela': 'Alajuela',
    'Heredia': 'Heredia',
    'Cartago' : 'Cartago',
    'Guanacaste' : 'Nicoya',
    'Puntarenas' : 'Puntarenas',
    'Limon' : 'Limon'
}

for i in list_of_keys:
    Provinces_and_capitals.pop(i,None)

print(Provinces_and_capitals)