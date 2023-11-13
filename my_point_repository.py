from domain.my_point import MyPoint
import matplotlib.pyplot as plt
import math


def is_valid_color(color):
    """
    Verify if the color is valid
    :param color: the color to be verified
    :return: True if the color is valid, False otherwise
    """
    if color == "red" or color == "green" or color == "blue" or color == "yellow" or color == "magenta":
        return True
    return False


class PointRepository:
    def __init__(self, points_list=None):
        if points_list is None:
            points_list = []
        self.__points = points_list.copy()

    def __len__(self):
        return len(self.__points)

    def __str__(self):
        """
        Converting a PointRepository object into a string.
        :param self: PointRepository object
        :return: string containing all the points in the repository
        """
        string = ""
        for element in self.__points:
            string += str(element) + "\n"
        string = string.strip()
        return string.strip()

    def get_number_of_points(self):
        """
        Get the number of points in the repository
        :return:
        """
        return len(self.__points)

    def add_point(self, new_entry: list):
        """
        Add a new point to the repository
        :param self: PointRepository object
        :param new_entry: list containing the abscissa, ordinate and color
        :raises IndexError if point already exists in the repository
        :raises ValueError if the color does not match one of the required colors
        """
        if self.point_exists(new_entry[0], new_entry[1], new_entry[2]):
            raise ValueError("Point already exists in the repository")
        self.__points.append(MyPoint(new_entry[0], new_entry[1], new_entry[2]))

    def get_point_by_index(self, index):
        """
        Get the point at a given index
        :param self: PointRepository object
        :param index: index of the point
        :return: instance which is at the given index in the repository
        :raises IndexError if index is out of bound
        """
        if self.is_valid_index(index):
            return self.__points[index]
        else:
            raise IndexError(f"Index should be between 0 and {len(self.__points) - 1}")

    def get_points_by_color(self, color_check):
        """
        Get points that have a certain color
        :param color_check: the color that the points must have
        :return: new PointRepository containing points that have the given color
        :raises ValueError if the color does not comply with the imposed conditions
        """

        if is_valid_color(color_check):
            color_list = []
            for element in self.__points:
                if element.get_color() == color_check:
                    color_list.append(element)
            return PointRepository(color_list)
        else:
            raise ValueError("The color you entered is invalid. Choose one of blue, red, green, yellow, magenta.")

    def get_points_inside_square(self, x_coordinate, y_coordinate, length):
        """
        Get points that are inside a given square
        :param x_coordinate: the square up-left corner abscissa
        :param y_coordinate: the square up-left corner ordinate
        :param length: square side length
        :return: new PointRepository containing points that are inside a given square
        :raises ValueError if the length of the square is a negative number or 0
        """
        square_list = []
        left_up_x = x_coordinate
        left_up_y = y_coordinate
        left_down_y = y_coordinate - length
        right_up_x = x_coordinate + length

        for element in self.__points:
            if (left_up_x < element.get_coordinate_x() < right_up_x and
                    left_down_y < element.get_coordinate_y() < left_up_y):

                square_list.append(element)

        return PointRepository(square_list)

    def get_minimum_distance_between_two_points(self):
        """
        Get the minimum distance between two points
        :return: the minimum distance between two points
        """
        minimum_distance = math.inf
        for first in self.__points:
            for second in self.__points:
                distance = math.sqrt((first.get_coordinate_x() - second.get_coordinate_x()) ** 2 +
                                     (first.get_coordinate_y() - second.get_coordinate_y()) ** 2)

                if distance < minimum_distance and distance != 0:
                    minimum_distance = distance

        return minimum_distance

    def update_a_point_by_index(self, the_index, the_x, the_y, the_color):
        """
        Update a point with new characteristics
        :param self: PointRepository object
        :param the_index: the index of the point that will be updated
        :param the_x: the new abscissa of the point
        :param the_y: the new ordinate of the point
        :param the_color: the new color of the point
        :return: the new point after the changes
        :raises ValueError if the point already exists in the repository
        :raises IndexError if the index or color does not meet the required parameters
        """
        if self.point_exists(the_x, the_y, the_color):
            raise ValueError("Point already exists in the repository")

        elif self.is_valid_index(the_index) and is_valid_color(the_color):

            self.set_properties_of_point(the_index, the_x, the_y, the_color)
            return self.__points[the_index]

        else:
            raise IndexError(f"Index should be between 0 and {len(self.__points) - 1} or "
                             f"the color does not meet the required conditions")

    def delete_a_point_by_index(self, the_index):
        """
        Delete a point at a given index
        :param self: PointRepository object
        :param the_index: the index of the point to be deleted
        :raises IndexError if the index is out of bound
        """
        if self.is_valid_index(the_index):
            del self.__points[the_index]
        else:
            raise IndexError(f"Index should be between 0 and {len(self.__points) - 1}")

    def delete_points_inside_square(self, x_coordinate, y_coordinate, length):
        """
        Delete the points that are inside a given square
        :param x_coordinate:  up-left corner abscissa
        :param y_coordinate: square up-left corner ordinate
        :param length: the square side length
        :return: points left after deletion
        """
        left_up_x = x_coordinate
        left_up_y = y_coordinate
        left_down_y = y_coordinate - length
        right_up_x = x_coordinate + length
        length = len(self.__points)
        element = 0
        while element < length:
            if left_up_x <= self.__points[element].get_coordinate_x() <= right_up_x:
                if left_down_y <= self.__points[element].get_coordinate_y() <= left_up_y:
                    del self.__points[element]
                    element -= 1
                    length -= 1
            element += 1

    def plot_points(self):
        """
        Plot all the points in the repository
        :return:
        """
        x = [point.get_coordinate_x() for point in self.__points]
        y = [point.get_coordinate_y() for point in self.__points]
        color = [point.get_color() for point in self.__points]
        plt.scatter(x, y, c=color)
        plt.show()

    def is_valid_index(self, index):
        """
        Verify if the index is valid
        :param index: the index to be verified
        :return: True if the index is valid, False otherwise
        """
        if 0 <= index < len(self.__points):
            return True
        return False

    def set_properties_of_point(self, the_index, the_x, the_y, the_color):
        """
        Set new properties to a point
        :param self: PointRepository object
        :param the_index: the index of the point to be modified
        :param the_x: the new abscissa of the point
        :param the_y: the new ordinate of the point
        :param the_color: the new color of the point
        """
        self.__points[the_index].set_coordinate_x(the_x)
        self.__points[the_index].set_coordinate_y(the_y)
        self.__points[the_index].set_color(the_color)

    def point_exists(self, point_x, point_y, point_color):
        """
        Verify if a point is already in the list
        :param self: PointRepository object
        :param point_x: the abscissa of the point
        :param point_y: the ordinate of the point
        :param point_color: the color of the point
        :return:
        """
        for i in range(len(self.__points)):
            if self.__points[i].get_coordinate_x() == point_x and self.__points[i].get_coordinate_y() == point_y:
                if self.__points[i].get_color() == point_color:
                    return True
        return False
