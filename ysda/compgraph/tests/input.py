import pytest
from setup import Input, Graph

def test_input_node_empty_run():
    input_node = Input(input=[])
    res = list(input_node.run())
    assert res == []

