import io
import typing

from .strings import strings, strings_generator


def test_small_dump():
    file_path = 'resources/small_dump.bin'
    etalon = [
        'Hello scoring server!`',
        'Some noise 42232U55`',
        'Hello you too`',
        'What is Petr score?`',
        'Yet another noise 2342342D4e45',
        '.5`',
        '17`',
        'Thank you scoring server! Bye-bye!`',
        'Bye-bye!'
    ]
    strings_gen = strings(file_path=file_path, min_string_len=3)
    assert isinstance(strings_gen, typing.Generator)
    assert sorted(strings_gen) == sorted(etalon)


class CustomStream(io.BytesIO):
    """Class for counting number of calls of stream read"""
    def __init__(self, *args, **kwargs):
        super(CustomStream, self).__init__(*args, **kwargs)
        self.counter = 0

    def read(self, size=-1):
        self.counter += 1
        return super(CustomStream, self).read(size)


def test_that_stream_read_in_chunks_when_chunk_less_then_string():
    test_binary_stream = CustomStream(b'\x00He\x00llo \x00scor\x00ing server!`')
    strings_gen = strings_generator(test_binary_stream, 1, 1)
    assert next(strings_gen) == 'He'
    assert test_binary_stream.counter == 4
    assert next(strings_gen) == 'llo '
    assert test_binary_stream.counter == 9
