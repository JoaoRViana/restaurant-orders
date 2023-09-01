from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():

    queijo_gorgonzola = Ingredient("queijo gorgonzola")
    farinha = Ingredient("farinha")
    assert queijo_gorgonzola.name == "queijo gorgonzola"
    assert queijo_gorgonzola.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert queijo_gorgonzola.__eq__(queijo_gorgonzola) is True
    assert queijo_gorgonzola.__eq__(farinha) != queijo_gorgonzola
    assert queijo_gorgonzola.__hash__() == hash(queijo_gorgonzola.name)
    assert farinha.__hash__() != hash(queijo_gorgonzola)
    assert queijo_gorgonzola.__repr__() == (
        f"Ingredient('{queijo_gorgonzola.name}')")
