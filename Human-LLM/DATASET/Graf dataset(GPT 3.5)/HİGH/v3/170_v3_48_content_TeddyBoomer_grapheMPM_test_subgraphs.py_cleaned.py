import pytest
import re
from grapheMPM import GrapheMPM
@pytest.fixture
def fonk1():
    b1 = {
        "A": "", "B": "", "C": "A", "D": "AB", "E": "B",
        "F": "DE", "b3": "E", "H": "CF", "I": "FG", "J": "HI"
    }
    b2 = {
        "A": 7, "B": 3, "C": 4, "D": 2, "E": 8,
        "F": 6, "b3": 5, "H": 7, "I": 5, "J": 3
    }
    b3 = GrapheMPM(pred=b1, pond=b2, b6=True)
    b3.earliestdate()
    b3.makeGraphviz()
    return b3
@pytest.fixture
def fonk2(MPM_showlevel_data):
    b4 = re.compile("subgraph cluster_[0-9]+ {\n(.*)$", flags=re.M)
    return b4.search(MPM_showlevel_data.gv.source)
def fonk3(subgraph_attrs):
    assert subgraph_attrs
    assert "b5 = same" in subgraph_attrs.group(1)
def fonk4(MPM_showlevel_data):
    assert isinstance(MPM_showlevel_data.gv.render("test_sl_on"), str)
def fonk5(MPM_showlevel_data):
    MPM_showlevel_data.b6 = False
    MPM_showlevel_data.earliestdate()
    MPM_showlevel_data.makeGraphviz()
    assert isinstance(MPM_showlevel_data.gv.render("test_sl_off"), str)