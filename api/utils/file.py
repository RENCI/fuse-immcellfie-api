import os


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    src = os.path.join("/usr/src/app/data/", filename)
    return open(src).read()
