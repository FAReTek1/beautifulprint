from .packing import bepr


def bprint(*args, theme=None, end: str = '\n', sep: str = '\n---\n'):
    for i, arg in enumerate(args):
        if i == len(args) - 1:
            # For the final element, end with the end string instead of the seperator
            _bprint(arg, theme, end)
        else:
            # Only add separators between elements
            _bprint(arg, theme, sep)


def _bprint(arg: object, theme=None, end: str = '\n'):
    print(bepr(arg), end=end)
