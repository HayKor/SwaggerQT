import sys


def except_hook(cls, exception, traceback) -> None:
    sys.__excepthook__(cls, exception, traceback)
