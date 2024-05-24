# exercise Abdellah Merri 
import csv
def charger_pokemons_csv(filename):
    pokemons = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            stats = list(map(int, row[1:]))
            pokemons[name] = stats
    return pokemons
pkmn = charger_pokemons_csv(pokemon.csv)
for nom, stats in pkmn.items():
    print(f{nom}: {stats})
print(isinstance(pkmn, dict))
print(isinstance(pkmn[Pikachu], list))
print(isinstance(pkmn[Pikachu][0], int))

