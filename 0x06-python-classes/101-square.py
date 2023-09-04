class Square:
    """
    Represents a square object.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): Size of the square. Defaults to 0.
            position (tuple): Position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position
            is not a tuple of 2 positive integers.
            ValueError: If size is less than 0
            or any value in the position tuple is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        errMsg = TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not tuple or len(value) != 2:
            raise errMsg
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise errMsg
        elif value[0] < 0 or value[1] < 0:
            raise errMsg
        self.__position = value

    def area(self):
        return self.__size ** self.__size

    def my_print(self):
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
