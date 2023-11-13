from domain.my_point import MyPoint
from repository.my_point_repository import PointRepository
from controller.controller import PointController


def data_examples_for_first_iteration():
    """
    Data examples for first iteration
    """
    my_point_1 = MyPoint(40, 23, "red")
    my_point_2 = MyPoint(12, 43, "green")
    my_point_1.set_coordinate_x(15)
    my_point_2.set_coordinate_y(16)
    my_point_1.set_color("blue")
    my_point_2.get_coordinate_x()
    my_point_1.get_coordinate_y()
    my_point_2.get_color()
    my_point_1.__str__()
    my_point_2.set_color(my_point_1.get_color())


def data_examples_for_second_iteration_repository():
    """
    Data examples for second iteration - repository
    """
    repository = PointRepository([])
    repository.add_point([1, 2, "red"])
    repository.add_point([2, 3, "green"])
    repository.get_point_by_index(0)
    repository.get_point_by_index(1)
    repository.get_number_of_points()
    repository.get_points_by_color("red")
    repository.get_points_by_color("green")
    repository.get_points_inside_square(0, 0, 10)
    repository.get_minimum_distance_between_two_points()
    repository.update_a_point_by_index(0, 1, 2, "blue")
    repository.delete_a_point_by_index(0)
    repository.delete_points_inside_square(0, 0, 10)
    repository.plot_points()


def data_examples_for_second_iteration_controller():
    """
    Data examples for second iteration - controller
    """
    repository = PointRepository([])
    controller = PointController(repository)
    controller.add_point([2, 3, "blue"])
    controller.add_point([4, 1, "blue"])
    controller.get_point_by_index(1)
    controller.get_point_by_index(0)
    controller.get_points_by_color("blue")
    controller.get_points_inside_square(0, 0, 10)
    controller.get_minimum_distance_between_two_points()
    controller.update_a_point_by_index(0, 1, 2, "green")
    controller.delete_a_point_by_index(0)
    controller.delete_points_inside_square(0, 0, 10)
    controller.plot_points()
