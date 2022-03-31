import pytest
from setup import Input, Map, Graph

def test_empty_mapper():
    input_node = Input(input=[])
    mapper_node = Map(simple_mapper)(input_node)
    graph = Graph(input_node=input_node, output_node=mapper_node)
    res = graph.run()
    assert res == []

def simple_mapper(row):
    yield row

@pytest.fixture
def get_numbers():
    return [
    {"a": 1},
    {"a": 2},
    {"a": 3},
    {"a": 4},
    {"a": 5},
]

def linear_mapper(row):
    yield {'a': row['a']*3}


def test_square_mapper():
    input_node = Input(input=get_numbers())
    mapper_node = Map(linear_mapper)(input_node)
    graph = Graph(input_node=input_node, output_node=mapper_node)
    res = graph.run()

    answer = [{'a': i*3} for i in range(1, 6)]
    assert res == answer