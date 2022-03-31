import subprocess


def check_output(input_text, expected_output):
    output = subprocess.check_output(
        ['python3', './counter_utils.py'],
        input=input_text,
        encoding='utf-8'
    )
    assert output.rstrip() == expected_output


def test_example1():
    check_output(
        '-m\n'
        '  there is one\n'
        '    more\n'
        'example for\n'
        ' problem\n',
        '45'
    )


def test_example2():
    check_output(
        '-l\n'
        '  there is one\n'
        '    more\n'
        'example for\n'
        ' problem\n',
        '4'
    )


def test_example3():
    check_output(
        '-L\n'
        '  there is one\n'
        '    more\n'
        'example for\n'
        ' problem\n',
        '14'
    )


def test_example4():
    check_output(
        '-w\n'
        '  there is one\n'
        '    more\n'
        'example for\n'
        ' problem\n',
        '7'
    )


def test_example5():
    check_output(
        '-m -l -L -w\n'
        '  there is one\n'
        '    more\n'
        'example for\n'
        ' problem\n',
        '4 7 45 14'
    )
