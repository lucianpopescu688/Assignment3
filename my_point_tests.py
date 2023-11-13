from domain.my_point import *


def test_make_point_with_valid_data():
    """
    Test make_point function with valid data
    """
    my_point = MyPoint(40, 23, "red")
    assert my_point.get_coordinate_x() == 40
    assert my_point.get_coordinate_y() == 23
    assert my_point.get_color() == "red"


def test_make_point_with_invalid_x():
    """
    Test make_point function with invalid x
    """
    try:
        MyPoint("40", 23, "red")
        assert False
    except ValueError:
        assert True


def test_make_point_with_invalid_y():
    """
    Test make_point function with invalid y
    """
    try:
        MyPoint(40, "23", "red")
        assert False
    except ValueError:
        assert True


def test_make_point_with_invalid_color():
    """
    Test make_point function with invalid color
    """
    try:
        MyPoint(40, 23, "purple")
        assert False
    except ValueError:
        assert True


def test_get_coordinate_x():
    """
    Test get_coordinate_x function
    """
    my_point = MyPoint(40, 23, "red")
    assert my_point.get_coordinate_x() == 40


def test_get_coordinate_y():
    """
    Test get_coordinate_y function
    """
    my_point = MyPoint(40, 23, "red")
    assert my_point.get_coordinate_y() == 23


def test_get_color():
    """
    Test get_color function
    """
    my_point = MyPoint(40, 23, "red")
    assert my_point.get_color() == "red"


def test_set_coordinate_x():
    """
    Test set_coordinate_x function
    """
    my_point = MyPoint(40, 23, "red")
    my_point.set_coordinate_x(31)
    assert my_point.get_coordinate_x() == 31


def test_set_coordinate_x_error():
    """
    Test set_coordinate_x function raises ValueError
    """
    try:
        my_point = MyPoint(31, 23, "red")
        my_point.set_coordinate_x("31")
        assert False
    except ValueError:
        assert True


def test_set_coordinate_y():
    """
    Test set_coordinate_y function
    """
    my_point = MyPoint(40, 23, "red")
    my_point.set_coordinate_y(31)
    assert my_point.get_coordinate_y() == 31


def test_set_coordinate_y_error():
    """
    Test set_coordinate_y function raises ValueError
    """
    try:
        my_point = MyPoint(31, 23, "red")
        my_point.set_coordinate_y("31")
        assert False
    except ValueError:
        assert True


def test_set_color():
    """
    Test set_color function
    """
    my_point = MyPoint(40, 23, "red")
    my_point.set_color("blue")
    assert my_point.get_color() == "blue"


def test_set_color_error():
    """
    Test set_color function raises ValueError
    """
    try:
        my_point = MyPoint(31, 23, "red")
        my_point.set_color("purple")
        assert False
    except ValueError:
        assert True


def tests_my_point():
    """
    Test all my_point functions
    """
    test_make_point_with_valid_data()
    test_make_point_with_invalid_x()
    test_make_point_with_invalid_y()
    test_make_point_with_invalid_color()
    test_get_coordinate_x()
    test_get_coordinate_y()
    test_get_color()
    test_set_coordinate_x()
    test_set_coordinate_x_error()
    test_set_coordinate_y()
    test_set_coordinate_y_error()
    test_set_color()
    test_set_color_error()
    print("\u001B[92mAll my_point tests passed! \u001B[0m")
