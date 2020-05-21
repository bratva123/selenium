import pytest
@pytest.yield_fixture()
def setUp():
    print("run before every method")
    yield
    print("once after every method")

def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")