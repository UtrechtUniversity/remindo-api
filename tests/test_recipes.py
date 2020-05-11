# content of ./test_recips.py
from remindo_api.recipe import RemindoRecipe

# TODO: expand tests to "full = True"


def test_isInstanceRemindoRecipe(rclient):
    recipes = rclient.list_recipes(study_id=86)
    assert isinstance(recipes[0], RemindoRecipe)
    assert [2323 == r.rid for r in recipes]
    assert recipes[0].api_call_params_study_id == 86


def test_isRecipe(rclient):
    recipe = rclient.list_recipes(recipe_id=2323)[0]
    assert recipe.rid == 2323
    assert recipe.name == "[20200205] BMW11405 - Evolutiebiologie - FT1_BCI"
    assert recipe.code == ""
    assert recipe.study_id == 86
    assert recipe.category is None
    assert recipe.status == "active"
    assert recipe.type == "graded practice"
    assert recipe.api_call_params_recipe_id == 2323
