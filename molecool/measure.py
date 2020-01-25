import numpy as np

def calculate_distance(r_a, r_b):
    """
    Calculate the distance between two points.

    Parameters
    ----------
    r_a, r_b : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0,0,0])
    >>> r2 = np.array([1,0,0])
    >>> calculate_distance(r1, r2)
    1.0
    """
    # This function calculates the distance between two points given as numpy arrays.
    dist = np.linalg.norm(r_a - r_b)
    return dist

def calculate_angle(r_a, r_b, r_c, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    dist_ab = r_b - r_a
    dist_bc = r_b - r_c
    theta = np.arccos(np.dot(dist_ab, dist_bc) / (np.linalg.norm(dist_ab)*np.linalg.norm(dist_bc)))
    if degrees:
        theta = np.degrees(theta)
    return theta

