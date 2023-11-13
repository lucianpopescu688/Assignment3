from tests.my_point_tests import tests_my_point
from tests.repository_tests import tests_my_point_repository


def all_tests():
    """
    Test all functions
    """
    tests_my_point()
    tests_my_point_repository()
    print("\u001B[92mAll tests passed! \u001B[0m")
