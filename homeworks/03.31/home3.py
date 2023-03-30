def read_recipes(file_name):
    with open(file_name, 'r') as file:
        recipes = [line.strip().split(',') for line in file.readlines()]
    return recipes


def find_strawberry_sugar(recipes):
    found_recipes = []
    for recipe in recipes:
        if 'strawberries' in recipe and 'sugar' in recipe:
            found_recipes.append(', '.join(recipe))
    return found_recipes

recipes = read_recipes('recipes.txt')
found_recipes = find_strawberry_sugar(recipes)

print("Recipes that require strawberries and sugar:")
for recipe in found_recipes:
    print(recipe)
