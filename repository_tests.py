from repository.my_point_repository import *


def test_add_point():
    """
    Test add_point function
    """
    my_point_repository = PointRepository()
    my_point_repository.add_point([1, 2, "red"])
    assert my_point_repository.get_point_by_index(0).get_coordinate_x() == 1
    assert my_point_repository.get_point_by_index(0).get_coordinate_y() == 2
    assert my_point_repository.get_point_by_index(0).get_color() == "red"


def test_add_point_value_error():
    """
    Test add_point function raises ValueError
    """
    try:
        my_point_repository = PointRepository()
        my_point_repository.add_point([1, 2, "red"])
        my_point_repository.add_point([1, 2, "red"])

    except ValueError:
        assert True


def test_get_point_by_index():
    """
    Test get_point_by_index function
    """
    my_point_repository = PointRepository()
    my_point_repository.add_point([1, 2, "red"])
    assert my_point_repository.get_point_by_index(0).get_coordinate_x() == 1
    assert my_point_repository.get_point_by_index(0).get_coordinate_y() == 2
    assert my_point_repository.get_point_by_index(0).get_color() == "red"


def test_get_point_by_index_index_error():
    """
    Test get_point_by_index function raises IndexError
    """
    try:
        my_point_repository = PointRepository()
        my_point_repository.add_point([1, 2, "red"])
        my_point_repository.get_point_by_index(1)

    except IndexError:
        assert True


def test_get_points_by_color():
    """
    Test get_points_by_color function
    """
    my_point_repository = PointRepository()
    my_point_repository.add_point([1, 2, "red"])
    my_point_repository.add_point([3, 4, "blue"])
    my_point_repository.add_point([5, 6, "red"])
    my_point_repository.add_point([7, 8, "blue"])
    assert len(my_point_repository.get_points_by_color("red")) == 2
    assert len(my_point_repository.get_points_by_color("blue")) == 2


def test_get_points_by_color_value_error():
    """
    Test get_points_by_color function raises ValueError
    """
    try:
        my_point_repository = PointRepository()
        my_point_repository.add_point([1, 2, "red"])
        my_point_repository.get_points_by_color("pink")

    except ValueError:
        assert True


def test_get_points_inside_square():
    """
    Test get_points_inside_square function
    """
    my_point_repository = PointRepository()
    my_point_repository.add_point([1, 2, "red"])
    my_point_repository.add_point([3, 4, "blue"])
    my_point_repository.add_point([5, 6, "red"])
    my_point_repository.add_point([7, 8, "blue"])
    assert len(my_point_repository.get_points_inside_square(0, 10, 10)) == 4
    assert len(my_point_repository.get_points_inside_square(0, 5, 5)) == 2


def test_get_points_inside_square_value_error():
    """
    Test get_points_inside_square function raises ValueError
    """
    try:
        my_point_repository = PointRepository()
        my_point_repository.add_point([1, 2, "red"])
        my_point_repository.get_points_inside_square(0, 0, -1)

    except ValueError:
        assert True


def test_get_minimum_distance_between_two_points():
    """
    Test get_minimum_distance_between_two_points function
    """
    my_point_repository = PointRepository()
    my_point_repository.add_point([1, 2, "red"])
    my_point_repository.add_point([3, 4, "blue"])
    my_point_repository.add_point([5, 6, "red"])
    my_point_repository.add_point([7, 8, "blue"])
    assert my_point_repository.get_minimum_distance_between_two_points() == 2.8284271247461903


def test_update_point_by_index():
    """
    Test update_point_by_index function
    """
    my_point_repository = PointRepository()
    my_point_repository.add_point([1, 2, "red"])
    my_point_repository.update_a_point_by_index(0, 3, 4, "blue")
    assert my_point_repository.get_point_by_index(0).get_coordinate_x() == 3
    assert my_point_repository.get_point_by_index(0).get_coordinate_y() == 4
    assert my_point_repository.get_point_by_index(0).get_color() == "blue"


def test_update_point_by_index_value_error():
    """
    Test update_point_by_index function raises ValueError
    """
    try:
        my_point_repository = PointRepository()
        my_point_repository.add_point([1, 2, "red"])
        my_point_repository.update_a_point_by_index(0, 3, 4, "blue")
        my_point_repository.update_a_point_by_index(0, 3, 4, "blue")

    except ValueError:
        assert True


def test_update_point_by_index_index_error():
    """
    Test update_point_by_index function raises IndexError
    """
    try:
        my_point_repository = PointRepository()
        my_point_repository.add_point([1, 2, "red"])
        my_point_repository.update_a_point_by_index(1, 3, 4, "blue")

    except IndexError:
        assert True


def test_delete_point_by_index():
    """
    Test delete_point_by_index function
    """
    my_point_repository = PointRepository()
    my_point_repository.add_point([1, 2, "red"])
    my_point_repository.delete_a_point_by_index(0)
    assert my_point_repository.get_number_of_points() == 0


def test_delete_point_by_index_index_error():
    """
    Test delete_point_by_index function raises IndexError
    """
    try:
        my_point_repository = PointRepository()
        my_point_repository.add_point([1, 2, "red"])
        my_point_repository.delete_a_point_by_index(1)

    except IndexError:
        assert True


def test_delete_points_inside_square():
    """
    Test delete_points_inside_square function
    """
    my_point_repository = PointRepository()
    my_point_repository.add_point([1, 2, "red"])
    my_point_repository.add_point([3, 4, "blue"])
    my_point_repository.add_point([5, 6, "red"])
    my_point_repository.add_point([7, 8, "blue"])
    my_point_repository.delete_points_inside_square(0, 10, 10)
    assert my_point_repository.get_number_of_points() == 0


def test_delete_points_inside_square_value_error():
    """
    Test delete_points_inside_square function raises ValueError
    """
    try:
        my_point_repository = PointRepository()
        my_point_repository.add_point([1, 2, "red"])
        my_point_repository.delete_points_inside_square(0, 0, -1)

    except ValueError:
        assert True


def tests_my_point_repository():
    """
    Test all my_point_repository functions
    """
    test_add_point()
    test_add_point_value_error()
    test_get_point_by_index()
    test_get_point_by_index_index_error()
    test_update_point_by_index()
    test_update_point_by_index_value_error()
    test_update_point_by_index_index_error()
    test_delete_point_by_index()
    test_delete_point_by_index_index_error()
    test_get_points_by_color()
    test_get_points_by_color_value_error()
    test_get_points_inside_square()
    test_get_points_inside_square_value_error()
    test_delete_points_inside_square()
    test_delete_points_inside_square_value_error()
    test_get_minimum_distance_between_two_points()
    print("\u001B[92mAll my_point_repository tests passed! \u001B[0m")
