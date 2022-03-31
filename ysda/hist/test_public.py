import subprocess


def test_sample():
    output = subprocess.check_output(
        ['python3', './hist.py'],
        input='Hello, world!',
        encoding='utf-8'
    )
    assert output == (
            '     #   \n'
            '     ##  \n'
            '#########\n'
            '!,Hdelorw\n'
            )
