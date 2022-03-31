import sys
import contextlib

from context_manager import supresser, retyper, dumper
from io import StringIO


def test_retyper():
    try:
        with retyper(ValueError, TypeError):
            raise ValueError('penguin')
    except ValueError:
        assert False, 'source error was raised'
    except TypeError as e:
        assert 'penguin' in e.args, 'attribute args lost'
    except Exception as e:
        assert False, 'totally wrong exception type {}'.format(e)


def test_supresser():
    try:
        with supresser(ValueError, TypeError,):
            raise ValueError('message')
    except Exception as e:
        assert False, 'supressed exception raised {}'.format(e)
    else:
        assert True


def test_dumped():
    stream = StringIO()
    msg = 'message to log'
    try:
        with dumper(stream):
            raise ValueError(msg)
    except ValueError:
        assert msg in stream.getvalue()
    except Exception:
        assert False, "wrong exception"
