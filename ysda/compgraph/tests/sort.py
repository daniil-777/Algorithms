import pytest
from setup import Input, Sort, Graph


@pytest.fixture
def get_numbers():
    return [
    {"a": 1},
    {"a": 2},
    {"a": 3},
    {"a": 4},
    {"a": 5},
]


@pytest.fixture
def get_advanced_persons():
    return [
    {"name": "Andrey", "id": 1, "age": 38},
    {"name": "Leonid", "id": 2, "age": 20},
    {"name": "Sergey", "id": 1, "age": 25},
    {"name": "Daniil", "id": 4, "age": 60},
    {"name": "Misha", "id": 1, "age": 5},
    {"name": "Roma", "id": 1, "age": 10},
    {"name": "Rishat", "id": 2, "age": 17},
    {"name": "Maxim", "id": 5, "age": 28},
    {"name": "Tanya", "id": 10, "age": 14},
]


def test_simple_sort():
    input_node = Input(input=get_numbers()[::-1])
    sort_node = Sort(by='a')(input_node)

    graph = Graph(input_node=input_node, output_node=sort_node)
    res = graph.run()
    assert res == get_numbers()


def test_sort_name():
    input_node = Input(input=get_advanced_persons())
    sort_node = Sort(by='name')(input_node)
    graph = Graph(input_node=input_node, output_node=sort_node)
    res = graph.run()
    print("***** RESULT *****")
    for value in res:
        print(value)

    print()
    print("******************")

    assert res == [
        {'name': 'Andrey', 'id': 1, 'age': 38},
        {'name': 'Daniil', 'id': 4, 'age': 60},
        {'name': 'Leonid', 'id': 2, 'age': 20},
        {'name': 'Maxim', 'id': 5, 'age': 28},
        {'name': 'Misha', 'id': 1, 'age': 5},
        {'name': 'Rishat', 'id': 2, 'age': 17},
        {'name': 'Roma', 'id': 1, 'age': 10},
        {'name': 'Sergey', 'id': 1, 'age': 25},
        {'name': 'Tanya', 'id': 10, 'age': 14},
    ]