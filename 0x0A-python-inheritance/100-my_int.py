#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """this Inverts int operators == and !=."""

    def __eq__(self, value):
        """Overrides ==  with !=."""
        return self.real != value

    def __ne__(self, value):
        """Override !=  with == """
        return self.real == value
