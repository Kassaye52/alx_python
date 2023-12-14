class Square:
    """Class that defines a square with a private size attribute."""
    
    def __init__(self, size):
        """Initialize the square with a private size attribute."""
        self.__size = size

    def get_size(self):
        """Public method to safely access the private size attribute."""
        return self.__size