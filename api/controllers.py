import json

import random


def get_random_kanji(jplt, nombre):
    # Read the JSON file

    with open("json/jplt_" + str(jplt) + ".json", "r", encoding="utf-8") as file:
        data = json.load(file)

        # Get the list of keys
        keys_list = list(data.keys())

        # Randomize the order of the keys
        randomized_keys = random.sample(keys_list, nombre)

        # Create a new dictionary with randomized order
        randomized_data = {key: data[key] for key in randomized_keys}

        return randomized_data
