from . import root
from forms.__ctx__ import Context

__forms__ = {"root": root}


def find(id: str):
    return __forms__.get(id)


__all__ = ["find", "Context"]
