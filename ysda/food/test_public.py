import subprocess


def test_sample():
    output = subprocess.check_output(
        ['python3', './food.py'],
        input=(
            '3 7\n'
            '#######\n'
            '#@...*#\n'
            '#######\n'
        ),
        encoding='utf-8'
    )
    assert output == '1'
