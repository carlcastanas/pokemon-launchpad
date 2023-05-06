class Pokemon:
    def __init__(self, name, species, level):
        self.name = name
        self.species = species
        self.level = level

class MacBookLaunchpad:
    def __init__(self):
        self.pokemon_list = []

    def add_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)

    def display_launchpad(self):
        print("MacBook Launchpad:")
        print("------------------")
        if len(self.pokemon_list) == 0:
            print("No Pokemon found.")
        else:
            for index, pokemon in enumerate(self.pokemon_list, 1):
                print(f"{index}. {pokemon.name} ({pokemon.species}), Level {pokemon.level}")

# Create a MacBook Launchpad instance
launchpad = MacBookLaunchpad()

# Add some pet Pokemon
pokemon1 = Pokemon("Pikachu", "Electric", 10)
pokemon2 = Pokemon("Bulbasaur", "Grass/Poison", 8)
pokemon3 = Pokemon("Charmander", "Fire", 12)

launchpad.add_pokemon(pokemon1)
launchpad.add_pokemon(pokemon2)
launchpad.add_pokemon(pokemon3)

# Display the MacBook Launchpad with pet Pokemon
launchpad.display_launchpad()
