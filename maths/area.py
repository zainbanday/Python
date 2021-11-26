"""
Find the area of various geometric shapes
"""
from math import pi, sqrt


def surface_area_cube(side_length: float) -> float:
    """
    Calculate the Surface Area of a Cube.

    >>> surface_area_cube(1)
    6
    >>> surface_area_cube(3)
    54
    >>> surface_area_cube(-1)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cube() only accepts non-negative values
    """
    if side_length < 0:
        raise ValueError("surface_area_cube() only accepts non-negative values")
    return 6 * side_length ** 2




    doctest.testmod(verbose=True)  # verbose so we can see methods missing tests
 
    print("\nSurface Areas of Cube is: \n")
    print(f"Cube: {surface_area_cube(20) = }")
    
