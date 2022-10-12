from _typeshed import Incomplete
from collections.abc import Generator

basestring: Incomplete
unicode = str
xrange: Incomplete

def is_iterable(obj): ...
def is_scalar(obj): ...
def is_collection(obj): ...
def split(src, sep: Incomplete | None = ..., maxsplit: Incomplete | None = ...): ...
def split_iter(
    src, sep: Incomplete | None = ..., maxsplit: Incomplete | None = ...
) -> Generator[Incomplete, None, Incomplete]: ...
def lstrip(iterable, strip_value: Incomplete | None = ...): ...
def lstrip_iter(iterable, strip_value: Incomplete | None = ...) -> Generator[Incomplete, None, None]: ...
def rstrip(iterable, strip_value: Incomplete | None = ...): ...
def rstrip_iter(iterable, strip_value: Incomplete | None = ...) -> Generator[Incomplete, None, None]: ...
def strip(iterable, strip_value: Incomplete | None = ...): ...
def strip_iter(iterable, strip_value: Incomplete | None = ...): ...
def chunked(src, size, count: Incomplete | None = ..., **kw): ...
def chunked_iter(src, size, **kw) -> Generator[Incomplete, None, Incomplete]: ...
def pairwise(src): ...
def pairwise_iter(src): ...
def windowed(src, size): ...
def windowed_iter(src, size): ...
def xfrange(stop, start: Incomplete | None = ..., step: float = ...) -> Generator[Incomplete, None, None]: ...
def frange(stop, start: Incomplete | None = ..., step: float = ...): ...
def backoff(start, stop, count: Incomplete | None = ..., factor: float = ..., jitter: bool = ...): ...
def backoff_iter(
    start, stop, count: Incomplete | None = ..., factor: float = ..., jitter: bool = ...
) -> Generator[Incomplete, None, None]: ...
def bucketize(src, key=..., value_transform: Incomplete | None = ..., key_filter: Incomplete | None = ...): ...
def partition(src, key=...): ...
def unique(src, key: Incomplete | None = ...): ...
def unique_iter(src, key: Incomplete | None = ...) -> Generator[Incomplete, None, Incomplete]: ...
def redundant(src, key: Incomplete | None = ..., groups: bool = ...): ...
def one(src, default: Incomplete | None = ..., key: Incomplete | None = ...): ...
def first(iterable, default: Incomplete | None = ..., key: Incomplete | None = ...): ...
def flatten_iter(iterable) -> Generator[Incomplete, None, None]: ...
def flatten(iterable): ...
def same(iterable, ref=...): ...
def default_visit(path, key, value): ...
def default_enter(path, key, value): ...
def default_exit(path, key, old_parent, new_parent, new_items): ...
def remap(root, visit=..., enter=..., exit=..., **kwargs): ...

class PathAccessError(KeyError, IndexError, TypeError):
    exc: Incomplete
    seg: Incomplete
    path: Incomplete
    def __init__(self, exc, seg, path) -> None: ...

def get_path(root, path, default=...): ...
def research(root, query=..., reraise: bool = ...): ...

class GUIDerator:
    size: Incomplete
    count: Incomplete
    def __init__(self, size: int = ...) -> None: ...
    pid: Incomplete
    salt: Incomplete
    def reseed(self) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def __next__(self): ...
    next: Incomplete

class SequentialGUIDerator(GUIDerator):
    start: Incomplete
    def reseed(self) -> None: ...
    def reseed(self) -> None: ...
    def __next__(self): ...
    next: Incomplete

guid_iter: Incomplete
seq_guid_iter: Incomplete

def soft_sorted(
    iterable, first: Incomplete | None = ..., last: Incomplete | None = ..., key: Incomplete | None = ..., reverse: bool = ...
): ...
def untyped_sorted(iterable, key: Incomplete | None = ..., reverse: bool = ...): ...
