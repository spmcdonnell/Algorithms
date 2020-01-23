#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    total_possible = []

    for key in recipe:
        if ingredients.get(key) == None or ingredients[key] - recipe[key] < 0:
            return 0
        else:
            total_possible.append(ingredients[key] // recipe[key])

    return min(total_possible)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 400, 'butter': 199, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
