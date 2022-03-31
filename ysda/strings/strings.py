import typing
import string


def strings_generator(stream: typing.BinaryIO,
                      min_string_len: int = 5,
                      chunk_size: int = 10 * 1024 * 1024) -> typing.Generator:
    """
    Generates printable strings from binary stream
    :param stream: some binary stream
    :param min_string_len: minimal size printable characters in a row to be detected as string
    :param chunk_size: size of chunk to parse stream in bytes
    :return extract printable string for each call
    """
    printable = set(string.printable)

    acc = []
    while True:
        chunk = stream.read(chunk_size)
        if not len(chunk):
            break

        for ch in chunk:
            if chr(ch) in printable:
                acc.append(chr(ch))
                continue
            if len(acc) >= min_string_len:
                yield ''.join(acc)
            acc = []
    if len(acc) >= min_string_len:
        yield ''.join(acc)


def strings(file_path: str, min_string_len: int = 4,
            chunk_size: int = 10 * 1024 * 1024) -> typing.Generator:
    """
    Generates printable strings from file with given path
    :param file_path: path to file
    :param min_string_len: minimal size printable characters in a row to be detected as string
    :param chunk_size: size of chunk to parse file in bytes
    :return extract printable string for each call
    """
    with open(file_path, 'rb') as f:
        yield from strings_generator(f, min_string_len, chunk_size)
