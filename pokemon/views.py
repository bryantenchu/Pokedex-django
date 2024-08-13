from django.shortcuts import render
import requests

def index(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
    data = response.json()
    pokemons = data['results']

    # Extract IDs and add to the pokemon dictionary
    for pokemon in pokemons:
        pokemon_id = pokemon['url'].split('/')[-2]
        pokemon['id'] = pokemon_id

    return render(request, 'index.html', {'pokemons': pokemons})

def detail(request, id):
    pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    species_response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{id}')
    
    if pokemon_response.status_code != 200 or species_response.status_code != 200:
        return render(request, '404.html')  # Create a 404.html template

    pokemon = pokemon_response.json()
    species = species_response.json()

    context = {
        'pokemon': pokemon,
        'species': species,
        'description': next((entry['flavor_text'] for entry in species['flavor_text_entries'] if entry['language']['name'] == 'en'), 'No description available.'),
    }
    return render(request, 'detail.html', context)
