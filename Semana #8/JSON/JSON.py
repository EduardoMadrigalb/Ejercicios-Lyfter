import json

def read_pokemons(route):
    with open(route, "r", encoding="utf-8") as file:
        return json.load(file)


def write_pokemons(route, pokemons):
    with open(route, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, indent=4, ensure_ascii=False)

def main_pokemon():
    
    route = r"C:\Users\Usuario\Desktop\Python\Archivos Python\JSON\pokemon.json"


    pokemons= read_pokemons(route)


    new_pokemon = {}

   
    new_pokemon["name"] = {}
    new_pokemon["name"]["english"] = input("Enter the name of the Pokémon")

  
    new_pokemon ["type_of_power"] = {}
    new_pokemon ["type_of_power"] = input("Enter the type of power: ")
    

   
    new_pokemon["base"] = {}
    new_pokemon["base"]["HP"] = int(input("Enter HP: "))
    new_pokemon["base"]["Attack"] = int(input("Enter Attack: "))
    new_pokemon["base"]["Defense"] = int(input("Enter Defense: "))
    new_pokemon["base"]["Sp. Attack"] = int(input("Enter Sp. Attack: "))
    new_pokemon["base"]["Sp. Defense"] = int(input("Enter Sp. Defense: "))
    new_pokemon["base"]["Speed"] = int(input("Enter Speed: "))

    pokemons.append(new_pokemon)

    write_pokemons(route, pokemons)

    print(new_pokemon)

   
main_pokemon()    

    

