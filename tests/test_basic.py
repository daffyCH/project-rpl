import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import add

def test_add():
    assert add(1, 2) == 3
