from utils import as_dict


def test_as_dict():
    assert as_dict([{"id": 1, "value": "test1"}, {"id": 2, "value": "test2"}]) == {1: "test1", 2: "test2"}
