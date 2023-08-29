#!/usr/bin/python3
""" Define a class Square """


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
            intialize the square
            Args:
                size (int): The size of the square
        """
        self.__size = size
        self.__position = position

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
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """
            Getter property for the position of the square.
            Retrieve the position
        """
        return self._position

    @position.setter
    def position(self, value):
        """
            Setter property for the position of the square

            Args:
                value (int): New position value for the square

            Raises:
                TypeError: if value is not integer or
                is not tuple or sits length is not 2
                ValueError: if any value in the tuple is less than 0
        """
        msgError = TypeError("position must be a tuple of 2 positive integers")

        if type(value) is not tuple or len(value) != 2:
            raise msgError
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise msgError
        elif value[0] < 0 or value[1] < 0:
            raise msgError

        self.__position = value

    def area(self):
        """
            Return the area of the square based on its size.
        """
        return self.__size ** 2

    def my_print(self):
        """
            print in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
