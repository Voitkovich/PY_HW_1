from retangle import Rectangle
import pytest


@pytest.fixture
def square():
    return Rectangle(1)


@pytest.fixture
def squarev2():
    return Rectangle(1, 1)


def test_square_area(square, squarev2):
    assert square.ploshad() == squarev2.ploshad()


def test_get_perim_pytest(square: Rectangle, squarev2: Rectangle):
    assert square.perimetr() == squarev2.perimetr()


@pytest.fixture
def big_rect():
    return Rectangle(4, 6)


@pytest.fixture
def result_rect():
    return Rectangle(3, 5)


def test_sub_rects(square, big_rect, result_rect):
    assert big_rect - square == result_rect