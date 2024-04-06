from fusion.util.debug import _FuncDict
import pytest


@pytest.fixture
def func_dict():
    return _FuncDict()
