import pytest
@pytest.yield_fixture()
def setUp():
    print("run before every method")
    yield
    print("once after every method")

def test_case_demo2MethodA(setUp):
    print("Running demo2 method A")

def test_case_demo2MethodB(setUp):
    print("Running demo2 method B")

def test_case_demo1methodA(setUp):
    print("Running method A")

def test_case_demo1methodB(setUp):
    print("Running method B")