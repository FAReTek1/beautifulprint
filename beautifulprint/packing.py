from types import FunctionType

from .kvstorage import KVStorage

packers = KVStorage()


def packer(cls: type):
    def decorator(func: FunctionType):
        # print(f"Registering {cls} packer with {func}")
        packers[cls] = func

        return func

    return decorator


def bepr(obj: object, *, default: FunctionType = repr) -> str:
    """
    Like repr, but better; beautiful repr! Uses pepr internally.
    """
    ret = pepr(obj, default=default)

    # Remove the starting newline
    ret = ret[1:]

    # Unindent by 1
    split = ret.splitlines()
    ret = ''
    for i, line in enumerate(split):
        ret += line[1:]

        # Don't add trailing newline
        if i < len(split) - 1:
            ret += '\n'

    return ret


def pepr(obj: object, *, default: FunctionType = repr, strip: bool = False) -> str:
    """
    Inner bepr function used for packer functions. Calls the packer function of the object's type on the object.
    "It needs more pepr, Mason."
    """
    if type(obj) in packers:
        data: str = packers[type(obj)](obj)
    else:
        data: str = default(obj)
    # You have to add a blank item at the start so all lines are indented uniformly
    lines = [''] + data.splitlines()

    ret = ''
    for i, line in enumerate(lines):
        if i > 0:
            ret += '\t'

        ret += line

        if i < len(lines) - 1:
            ret += '\n'
    if strip:
        ret = ret.strip()

    return ret


@packer(cls=dict)
def _pack_dict(_value: dict):
    ret = '{'

    for i, (k, v) in enumerate(_value.items()):
        ret += f"{pepr(k)}: {pepr(v, strip=True)}"

        if i < len(_value) - 1:
            ret += ', '
        else:
            # This way we only add a newline before the final bracket if there are items
            ret += '\n'

    ret += '}'
    return ret


@packer(cls=list)
def _pack_list(_value: list):
    ret = '['

    for i, v in enumerate(_value):
        ret += f"{pepr(v)}"

        if i < len(_value) - 1:
            ret += ', '
        else:
            # This way we only add a newline before the final bracket if there are items
            ret += '\n'

    ret += ']'

    return ret


@packer(cls=tuple)
def _pack_tuple(_value: tuple):
    if len(_value) == 1:
        return repr(_value)

    ret = '('

    for i, v in enumerate(_value):
        ret += f"{pepr(v)}"

        if i < len(_value) - 1:
            ret += ', '
        else:
            # This way we only add a newline before the final bracket if there are items
            ret += '\n'

    ret += ')'

    return ret
