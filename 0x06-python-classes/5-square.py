#!/usr/bin/python3
""" Define a class Square """


class Square:
    def __init__(self, size=0):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
            Getter property for the size of the square.
            Retrieve the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Setter property for the size of the square

            Args:
                value (int): New size value for the square

            Raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        """
        Returns the area of the square based on its size.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
            print in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
