from tests.all_tests import all_tests
from controller.controller import PointController
from user_interface.user_interface import UserInterface
from repository.my_point_repository import PointRepository
from domain.my_point import MyPoint

all_tests()
try:
    repository = PointRepository([
        MyPoint(1.0, 1.0, "blue"),
        MyPoint(2.0, 2.0, "magenta"),
        MyPoint(4.0, 4.0, "yellow"),
        MyPoint(6.0, 6.0, "red"),
        MyPoint(8.0, 8.0, "green"),
        MyPoint(10.0, 10.0, "blue"),
        MyPoint(12.0, 12.0, "green"),
        MyPoint(-2.0, -2.0, "red"),
        MyPoint(-1.0, -1.0, "green"),
        MyPoint(14.0, 14.0, "blue")
    ])
    controller = PointController(repository)
    UserInterface(controller).main_program()
except ValueError as ve:
    print(ve)
    print("Check the input data from repository")
