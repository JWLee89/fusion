from typing import Any
from fusion.util.debug import _FuncDict
import pytest


@pytest.mark.parametrize(
    "key, value",
    [
        # Any dictionary with a value that is not a function
        ("a", 1),
        ("b", "string"),
        ("c", [1, 2, 3]),
        ("d", {"a": "string", "b": bool}),
    ],
)
def test_func_dict_failure(func_dict: _FuncDict, key: Any, value: Any):
    with pytest.raises(TypeError):
        func_dict[key] = value
