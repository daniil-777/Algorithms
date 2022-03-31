from caesar_cipher import caesar_encrypt


def test_example():
    input = 'This is stupid song stupid stupid stupid song'
    output = 'Drsc sc cdezsn cyxq cdezsn cdezsn cdezsn cyxq'
    assert caesar_encrypt(input, 10) == output


