# How to connect to an API using Python

import requests

BASE_URL = "https://pokeapi.co/api/v2/"

POKEMON_NAME = "Squirtle"


def get_pokemon_info(name):

    url = f"{BASE_URL}/pokemon/{name}"

    response = requests.get(url)  # this method returns a Response object.

    # I think I'm using the __str()__ method of the response object:
    print(f"Response object: {response}")  # 200 means the response was "ok".

    if response.status_code == 200:
        print("Data retrieved!")

        # a Response is a JSON format. I can convert it to a Python dictionary
        pokemon_data = response.json()

        return pokemon_data

    else:
        print(f"Failed to retrieve data: {response.status_code}")

        return None


def main() -> None:

    pokemon_info = get_pokemon_info(POKEMON_NAME)

    if pokemon_info:
        print(f"\nPokemon's name: {pokemon_info['name'].capitalize()}")
        print(f"Pokemon's id: {pokemon_info['id']}")
        print(f"Pokemon's height: {pokemon_info['height']}")
        print(f"Pokemon's weight: {pokemon_info['weight']}")


if __name__ == '__main__':
    main()
