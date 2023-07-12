#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, int_val):
        """Initialisation method"""
        super().__init__()

    def __eq__(self, other_int):
        """Test for equality"""
        return not super().__eq__(other_int)

    def __ne__(self, other_int):
        """Test for not equal to"""
        return not super().__ne__(other_int)
