# content of ./test_cluster.py
from remindo_api import client
from remindo_api.cluster import RemindoCluster


def test_listIdCluster(rclient):
    list_ids = list()
    response = rclient.list_clusters()
    assert isinstance(response[0], RemindoCluster)
    [list_ids.append(c.rid) for c in response]
    assert 2257 in list_ids

def test_listNameCluster(rclient):
    list_names = list()
    response = rclient.list_clusters()
    assert isinstance(response[0], RemindoCluster)
    [list_names.append(c.name) for c in response]
    assert "Accorderen Groep 1" in list_names

def test_listCluster(rclient):
    response = rclient.list_clusters()
    assert isinstance(response[0], RemindoCluster)
    assert 2257 == response[0].rid
    assert "Accorderen Groep 1" == response[0].name
    
