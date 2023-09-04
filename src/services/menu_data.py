import csv 
from src.models.dish import Dish
from src.models.ingredient import Ingredient

# Req 3


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set(self.get_dishes())
    
    def get_dishes(self):
        with open(self.source_path, 'r') as archive:
            list_dishes = csv.DictReader(archive)
            dishes = []

            for i in list_dishes:
                name = i['dish']
                price = float(i['price'])
                ingredient = i['ingredient']
                amount = int(i['recipe_amount'])
                for j in dishes:
                    ingredient_class = Ingredient(ingredient)
                    if j.name != name:
                        dish_class = Dish(name, price)
                        dish_class.add_ingredient_dependency(
                            ingredient_class, amount)
                        dishes.append(dish_class)
                    else:
                        j.add_ingredient_dependency(
                            ingredient_class, amount)
                if len(dishes) < 1:
                    ingredient_class = Ingredient(ingredient)
                    dish_class = Dish(name, price)
                    dish_class.add_ingredient_dependency(
                            ingredient_class, amount)
                    dishes.append(dish_class)
            return dishes
