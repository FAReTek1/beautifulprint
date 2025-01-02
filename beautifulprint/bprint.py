from .packing import bepr


def bprint(*args, theme=None, end: str = '\n', sep: str = '\n'):
    for i, arg in enumerate(args):
        if i == len(args) - 1:
            _bprint(arg, theme)
        else:
            _bprint(arg, theme, sep)

    print(end=end)


def _bprint(arg: object, theme=None, end: str = '\n'):
    print(bepr(arg), end=end)
