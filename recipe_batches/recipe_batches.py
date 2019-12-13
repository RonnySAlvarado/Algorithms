#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    recipeKeys = list(recipe.keys())
    ingredientsKeys = list(ingredients.keys())
    smallest = ingredients[ingredientsKeys[0]] // recipe[recipeKeys[0]]
    if(len(recipeKeys) != len(ingredientsKeys)):
        return 0

    for key in ingredients:
        if math.floor(ingredients[key] // recipe[key]) < smallest:
            smallest = math.floor(ingredients[key] // recipe[key])

    if smallest <= 0:
        return 0
    else:
        return smallest


print(recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
    'milk': 1288, 'flour': 9, 'sugar': 95}))

print(recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10}, {
    'milk': 1000, 'flour': 12, 'sugar': 100}))

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
