# (generated with --quick)

import remindo_api.recipe
import remindo_api.study
from typing import Type

RemindoRecipe: Type[remindo_api.recipe.RemindoRecipe]
RemindoStudy: Type[remindo_api.study.RemindoStudy]

def test_listOnlyStudies(rclient) -> None: ...
def test_listStudiesRecipes(rclient) -> None: ...
