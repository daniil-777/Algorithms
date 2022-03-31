import subprocess


def check_output(input_text, expected_output):
    output = subprocess.check_output(
        ['python3', './git_log.py'],
        input=input_text,
        encoding='utf-8'
    )
    assert output == expected_output


def test_example1():
    check_output(
        # stdin
        '0cd8619f18d8ecad1e5d2303f95ed206c2d6f92b\t'
        'Fri Sep 23 10:59:32 2016 -0700\t'
        'Brett Cannon\t'
        'brettcannon@users.noreply.github.com\t'
        'Update PEP 512 (#107)\n'

        '94dbee096b92f10ab83bbcf88102c6acdc3d76d1\t'
        'Thu Sep 22 12:39:58 2016 +0100\t'
        'Thomas Kluyver\t'
        'takowl@gmail.com\t'
        'Update PEP 517 to use pyproject.toml from PEP 518 (#51)',

        # stdout
        '0cd8619....................................................Update PEP 512 (#107)\n'
        '94dbee0..................Update PEP 517 to use pyproject.toml from PEP 518 (#51)\n'
    )
