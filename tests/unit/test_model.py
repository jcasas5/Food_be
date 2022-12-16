from recipe_api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, steps, rating and favorite fields are defined correctly
    """
    recipe = Recipe('cocido', 'eggs, flour, etc', 'step1, step2,step3', 5, True)
    assert recipe.name == 'cocido'
    assert recipe.ingredients == 'eggs, flour, etc'
    assert recipe.steps == 'step1, step2,step3'
    assert recipe.rating == 5
    assert recipe.favorite == True