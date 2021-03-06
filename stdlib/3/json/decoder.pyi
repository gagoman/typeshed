import sys
from typing import Any, Callable, Dict, List, Tuple

if sys.version_info >= (3, 5):
    class JSONDecodeError(ValueError):
        msg: str
        doc: str
        pos: int
        lineno: int
        colno: int
        def __init__(self, msg: str, doc: str, pos: int) -> None: ...

class JSONDecoder:
    object_hook = None  # type: Callable[[Dict[str, Any]], Any]
    parse_float = ...  # Callable[[str], Any]
    parse_int = ...  # Callable[[str], Any]
    parse_constant = ...  # Callable[[str], Any]
    strict = ...  # type: bool
    object_pairs_hook = None  # type: Callable[[List[Tuple[str, Any]]], Any]

    def __init__(self, object_hook: Callable[[Dict[str, Any]], Any]=None,
            parse_float: Callable[[str], Any]=None,
            parse_int: Callable[[str], Any]=None,
            parse_constant: Callable[[str], Any]=None,
            strict: bool=True,
            object_pairs_hook: Callable[[List[Tuple[str, Any]]], Any]=None) -> None: ...
    def decode(self, s: str) -> Any: ...
    def raw_decode(self, s: str, idx: int=...) -> Tuple[Any, int]: ...
