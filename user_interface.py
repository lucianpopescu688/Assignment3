def print_menu():
    """
    Prints the menu
    """
    print("0 - Exit program")
    print("1 - Print menu")
    print("2 - Print the points in the repository")
    print("3 - Add a new point to the repository")
    print("4 - Get the point at a given index")
    print("5 - Get all the points which have a given color")
    print("6 - Get all the points which are inside a square")
    print("7 - Get the minimum distance between two points")
    print("8 - Update a point at a given index with new characteristics")
    print("9 - Delete a point at a given index")
    print("10 - Delete the points that are inside a given square")
    print("11 - Plot all points in a chart")


class UserInterface:
    def __init__(self, controller):
        self.__user_interface = controller

    def main_program(self):
        """
        Main program
        """
        print_menu()

        while True:
            command = get_command()
            if command == 0:
                break

            elif command == 1:
                print_menu()

            elif command == 2:
                print(self.__user_interface)

            elif command == 3:
                coordinate_x = get_coordinate()
                coordinate_y = get_coordinate()
                color = get_color()
                self.__user_interface.add_point([coordinate_x, coordinate_y, color])

            elif command == 4:
                index = get_index(self.__user_interface)
                print(self.__user_interface.get_point_by_index(index))
                
            elif command == 5:
                color = get_color()
                print(self.__user_interface.get_points_by_color(color))

            elif command == 6:
                x_square = get_coordinate()
                y_square = get_coordinate()
                length = get_length()
                print(self.__user_interface.get_points_inside_square(x_square, y_square, length))

            elif command == 7:
                print(round(self.__user_interface.get_minimum_distance_between_two_points(), 3))

            elif command == 8:
                index = get_index(self.__user_interface)
                coordinate_x = get_coordinate()
                coordinate_y = get_coordinate()
                color = get_color()
                self.__user_interface.update_a_point_by_index(index, coordinate_x, coordinate_y, color)

            elif command == 9:
                index = get_index(self.__user_interface)
                self.__user_interface.delete_a_point_by_index(index)

            elif command == 10:
                x_square = get_coordinate()
                y_square = get_coordinate()
                length = get_length()
                self.__user_interface.delete_points_inside_square(x_square, y_square, length)

            elif command == 11:
                self.__user_interface.plot_points()


def get_command():
    """
    Gets the command from the user. Print an error message if the command is not correct.
    :return: int, the command
    """
    while True:
        try:
            command = int(input("The command is: "))
            if command < 0 or command > 11:
                raise ValueError

            elif 0 <= command <= 11:
                return command

        except ValueError:
            print('\033[31m' + "Value need to be between 0 and 11. You will be asked to enter a new value:" + '\033[0m')


def get_index(self):
    """
    Gets the index from the user. Print an error message if the index is not correct.
    :return: int, the index
    """
    while True:
        try:
            index = int(input("The index is: "))
            if index < 0 or index > len(self) - 1:
                raise ValueError

            elif 0 <= index <= len(self) - 1:
                return index

        except ValueError:
            print('\033[31m' + f"Value need to be between 0 and {len(self) - 1}. You will be asked to enter a new "
                               f"value:" + '\033[0m')


def get_coordinate():
    """
    Gets the coordinate from the user. Print an error message if the coordinate is not correct.
    :return: float, the coordinate
    """
    while True:
        try:
            coordinate = float(input("The coordinate is: "))
            return coordinate

        except ValueError:
            print('\033[31m' + "Value need to be a float. You will be asked to enter a new value:" + '\033[0m')


def get_color():
    """
    Gets the color from the user. Print an error message if the color is not correct.
    :return: string, the color
    """
    while True:
        try:
            color = input("The color is: ")
            if color not in ["red", "green", "blue", "yellow", "magenta"]:
                raise ValueError

            elif color in ["red", "green", "blue", "yellow", "magenta"]:
                return color

        except ValueError:
            print('\033[31m' + "Color need to be red, green, blue, yellow or magenta. You will be asked to enter a new "
                               "value:" + '\033[0m')


def get_length():
    """
    Gets the length from the user. Print an error message if the length is not correct.
    :return: float, the length
    """
    while True:
        try:
            length = float(input("The length is: "))
            if length <= 0:
                raise ValueError

            return length

        except ValueError:
            print('\033[31m' + "Value need to be a float. You will be asked to enter a new value:" + '\033[0m')
