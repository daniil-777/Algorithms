from palindromes import addition_upto_palindrome


def test_example1():
    assert addition_upto_palindrome('abc') == 2


def test_example2():
    assert addition_upto_palindrome('aba') == 0
