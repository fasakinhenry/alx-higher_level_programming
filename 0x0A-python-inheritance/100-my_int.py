#!/usr/bin/python3
"""A class that inherits from int constructor"""


class MyInt(int):
    """A rebel class that inherits from int."""

    def __eq__(self, other):
        """check for === and negiate the result."""
        return (not super().__eq__(other))

    def __ne__(self, other):
        """check for != and negiate the result."""
        return (not super().__ne__(other))
