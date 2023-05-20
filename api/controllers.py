import json

import random


def get_random_kanji(jplt, nombre):
    # Read the JSON file

    with open("json/jplt_" + str(jplt) + ".json", "r", encoding="utf-8") as file:
        data = json.load(file)

        # Get the keys of the JSON data (assuming it's a dictionary)
    keys = list(data.keys())

    # Get a list of random items from the keys
    random_keys = random.sample(keys, nombre)

    # Retrieve the corresponding values for the random keys
    random_items = [data[key] for key in random_keys]

    return random_items
