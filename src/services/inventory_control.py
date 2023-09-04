from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_inventory(self, recipe_name):
        ingredientes = self.inventory.keys()
        ingredient_names = []
        for i in ingredientes:
            ingredient_names.append(i.name)
        return (recipe_name in ingredient_names)

    def check_recipe_availability(self, recipe: Recipe) -> bool:
        avalaible = []
        for i in recipe:
            if ((self.check_inventory(i.name)) and
               (self.inventory[i] >= recipe[i])):
                avalaible.append(True)
            else:
                avalaible.append(False)
        return False not in avalaible

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        avalaible_recipe = self.check_recipe_availability(recipe)
        if avalaible_recipe:
            for i in recipe:
                self.inventory[i] -= recipe[i]
            return None
        else:
            raise ValueError('went bad')
