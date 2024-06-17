from . import root

__forms__ = {"root": root}


def find(id: str):
    return __forms__.get(id)
