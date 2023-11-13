class MyPoint:
    def __init__(self, x, y, color):
        if not isinstance(x, int) and not isinstance(x, float):
            raise ValueError(f"The abscissa you entered is invalid. It should be an integer or a float.")

        elif not isinstance(y, int) and not isinstance(y, float):
            raise ValueError(f"The abscissa you entered is invalid. It should be an integer or a float.")

        elif not(color == "red" or color == "green" or color == "blue" or color == "yellow" or color == "magenta"):
            raise ValueError(f"The color you entered is invalid. Choose one of blue, red, green, yellow, magenta.")

        self.__coordinate_x = x
        self.__coordinate_y = y
        self.__color = color

    def get_coordinate_x(self):
        """
        Get the abscissa of the point
        :return: abscissa of the point
        """
        return self.__coordinate_x

    def get_coordinate_y(self):
        """
        Get the ordinate of the point
        :return: ordinate of the point
        """
        return self.__coordinate_y

    def get_color(self):
        """
        Get the color of the point
        :return: color
        """
        return self.__color

    def set_coordinate_x(self, x):
        """
        Set a new abscissa to the point
        :param x: new abscissa of the point
        :raises ValueError: if the abscissa is not an integer or a float
        """
        if not isinstance(x, int) and not isinstance(x, float):
            raise ValueError(f"The abscissa you entered is invalid. It should be an integer or a float.")

        self.__coordinate_x = x

    def set_coordinate_y(self, y):
        """
        Set new ordinate to the point
        :param y: new ordinate of the point
        :raises ValueError: if the ordinate is not an integer or a float
        """
        if not isinstance(y, int) and not isinstance(y, float):
            raise ValueError(f"The abscissa you entered is invalid. It should be an integer or a float.")

        self.__coordinate_y = y

    def set_color(self, color):
        """
        Set a new color to the point
        :param color: new color of the point
        :raises ValueError: if the color is not one of blue, red, green, yellow, magenta
        """
        if not(color == "red" or color == "green" or color == "blue" or color == "yellow" or color == "magenta"):
            raise ValueError(f"The color you entered is invalid. Choose one of blue, red, green, yellow, magenta.")

        self.__color = color

    def __str__(self):
        """
        Converting a MyPoint object into a string
        :return: string of the MyPoint object
        """
        return f"Point({self.__coordinate_x}, {self.__coordinate_y}) of color {self.__color}"
