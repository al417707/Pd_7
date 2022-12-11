import pytest
import tempfile
import os
import filecmp

from homework import take_from_list
from homework import calculate

def test_take_empty():
    assert take_from_list([],[]) == []

def test_take_except():
    with pytest.raises(TypeError):
        take_from_list(1,1)
    with pytest.raises(IndexError):
        take_from_list([1,2,3],6)

def test_calculate():
    out_dirpath = os.path.join(tempfile.mkdtemp(), 'wyn.json')
    calculate('input.json', out_dirpath)
    assert filecmp.cmp(out_dirpath,'output.json')
    os.remove(out_dirpath)


