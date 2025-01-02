from .packing import bepr
from .theme import Theme
from .util import ContextManager


def bprint(*args, theme: Theme = None, end: str = '\n', sep: str = '\n---\n'):
    if not isinstance(theme, Theme):
        theme = ContextManager()

    with theme:
        for i, arg in enumerate(args):
            if i == len(args) - 1:
                # For the final element, end with the end string instead of the seperator
                _bprint(arg, end)
            else:
                # Only add separators between elements
                _bprint(arg, sep)


def _bprint(arg: object, end: str = '\n'):
    print(bepr(arg), end=end)
