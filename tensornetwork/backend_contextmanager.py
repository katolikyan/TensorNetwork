from typing import Text
from contextlib import contextmanager

class DefaultBackend():

    with_statement = False
    backend = None

    def __init__(self, backend_name: Text):
        DefaultBackend.backend = backend_name

    def __enter__(self):
        DefaultBackend.with_statement = True

    def __exit__(self, exc_type, exc_value, traceback):
        DefaultBackend.with_statement = False
        DefaultBackend.backend = None
