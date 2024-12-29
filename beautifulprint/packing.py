from types import FunctionType
from .kvstorage import KVStorage

packers = KVStorage()


def packer(cls: type):
    def decorator(func: FunctionType):
        print(f"Registering {cls} packer with {func}")
        packers[cls] = func

        return func

    return decorator


# Example usage
@packer(cls=dict)
def _pack_dict(_value: dict):
    return repr(_value)
