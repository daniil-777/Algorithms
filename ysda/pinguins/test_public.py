import subprocess


def test_example():
    output = subprocess.check_output(
        ['python3', './pinguins.py'],
        input='1',
        encoding='utf-8'
    )
    expected_output = (
        '   _~_    \n'
        '  (o o)   \n'
        ' /  V  \\  \n'
        '/(  _  )\\ \n'
        '  ^^ ^^'
    )
    assert output.rstrip() == expected_output
