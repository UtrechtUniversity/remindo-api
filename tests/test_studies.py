# content of ./test_studies.py
from remindoapi import client
from remindoapi.study import RemindoStudy
from remindoapi.recipe import RemindoRecipe


def test_listOnlyStudies(rclient):
    study = rclient.list_studies(study_id=86)[0]
    assert isinstance(study, RemindoStudy)
    assert study.rid == 86
    assert study.name == "BETA project LearningLytics"
    assert study.code == "BETA-LL"
    assert study.descr == ""
    assert study.edition_descr == "De originele editie waar alles by default aan vast zit."
    assert study.edition_name == "Origineel"
    assert study.source_edition_id == 0
    assert study.source_study_id == 107

def test_listStudiesRecipes(rclient):
    study, recipes = rclient.list_studies(study_id=86, complete=True, since="2020-01-01")
    study = study[0]
    assert isinstance(study, RemindoStudy)
    assert study.rid == 86
    assert study.name == "BETA project LearningLytics"
    assert study.code == "BETA-LL"
    assert study.descr == ""
    assert study.edition_descr == "De originele editie waar alles by default aan vast zit."
    assert study.edition_name == "Origineel"
    assert study.source_edition_id == 0
    assert study.source_study_id == 107

    # test presence of recipes
    assert isinstance(recipes[0], RemindoRecipe)
    assert [2323 == r.rid for r in recipes]