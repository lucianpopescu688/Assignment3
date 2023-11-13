class PointController:
    def __init__(self, repository):
        self.__repository = repository

    def __len__(self):
        return len(self.__repository)

    def __str__(self):
        """
        Converting a PointController object into a string.
        :param self: PointController object
        :return: string containing all the points in the repository
        """
        return str(self.__repository)

    def get_number_of_points(self):
        """
        Get the number of points in the repository
        :return:
        """
        return self.__repository.get_number_of_points()

    def list_to_string(self):
        """
        Convert the content of the list of integers into string
        Return the string representation
        :return:
        """
        return [str(element) for element in self.__repository]

    def add_point(self, new_entry: list):
        """
        Add a new point to the repository
        :param self: PointController object
        :param new_entry: list containing the abscissa, ordinate and color
        :raises IndexError if point already exists in the repository
        :raises ValueError if the color does not match one of the required colors
        """
        self.__repository.add_point(new_entry)

    def get_point_by_index(self, index):
        """
        Get the point at a given index
        :param self: PointController object
        :param index: index of the point
        :return: instance which is at the given index in the repository
        :raises IndexError if index is out of bound
        """
        return self.__repository.get_point_by_index(index)

    def get_points_by_color(self, color):
        """
        Get all the points which have a given color
        :param self: PointController object
        :param color: the color of the point
        :return: list containing all the points which have the given color
        """
        return self.__repository.get_points_by_color(color)

    def get_points_inside_square(self, x_coordinate, y_coordinate, length):
        """
        Get all the points which are inside a square
        :param self: PointController object
        :param x_coordinate: the square up-left corner abscissa
        :param y_coordinate: the square up-left corner ordinate
        :param length: length of the square
        :return: list containing all the points which are inside the square
        """
        return self.__repository.get_points_inside_square(x_coordinate, y_coordinate, length)

    def get_minimum_distance_between_two_points(self):
        """
        Get the minimum distance between two points
        :return: the minimum distance between two points
        """
        return self.__repository.get_minimum_distance_between_two_points()

    def update_a_point_by_index(self, the_index, the_x, the_y, the_color):
        """
        Update a point with new characteristics
        :param self: PointRepository object
        :param the_index: the index of the point that will be updated
        :param the_x: the new abscissa of the point
        :param the_y: the new ordinate of the point
        :param the_color: the new color of the point
        :return: the new point after the changes
        """
        return self.__repository.update_a_point_by_index(the_index, the_x, the_y, the_color)

    def delete_a_point_by_index(self, the_index):
        """
        Delete a point at a given index
        :param self: PointRepository object
        :param the_index: the index of the point to be deleted
        """
        self.__repository.delete_a_point_by_index(the_index)

    def delete_points_inside_square(self, x_coordinate, y_coordinate, length):
        """
        Delete the points that are inside a given square
        :param x_coordinate: up-left corner abscissa
        :param y_coordinate: square up-left corner ordinate
        :param length: the square side length
        :return: points left after deletion
        """
        return self.__repository.delete_points_inside_square(x_coordinate, y_coordinate, length)

    def plot_points(self):
        """
        Plot all the points in the repository
        """
        self.__repository.plot_points()
