from src.models.dish import Dish, Recipe  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    JaoFood = Dish("JaoFood", 12.27)
    notJaoFood = Dish("notJaoFood", 0.27)
    farinha = Ingredient('farinha')
    assert JaoFood.name == "JaoFood"
    assert JaoFood.price == 12.27
    assert JaoFood.__eq__(JaoFood) is True
    assert notJaoFood.__eq__(notJaoFood) != JaoFood
    assert JaoFood.__hash__() == hash(JaoFood)
    assert notJaoFood.__hash__() != hash(JaoFood)
    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish('invalidFood', 0)
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('invalidFood', "10")
    assert JaoFood.__repr__() == (f"Dish('{JaoFood.name}', R${JaoFood.price})")
    JaoFood.add_ingredient_dependency(farinha, 1)
    assert JaoFood.recipe == {farinha: 1}
    assert JaoFood.get_ingredients() == {farinha}
    assert JaoFood.get_restrictions() == farinha.restrictions
