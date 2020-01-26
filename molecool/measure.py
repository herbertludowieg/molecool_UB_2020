import numpy as np
from molecool.atom_data import atomic_weights

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
    if not isinstance(r_a, np.ndarray):
        raise TypeError("r_a parameter needs to be a numpy array")
    if not isinstance(r_b, np.ndarray):
        raise TypeError("r_b parameter needs to be a numpy array")
    # This function calculates the distance between two points given as numpy arrays.
    dist = np.linalg.norm(r_a - r_b)
    return dist

def calculate_angle(r_a, r_b, r_c, degrees=False):
    """
    Calculate the angle between three points.

    Parameters
    ----------
    r_a, r_b, r_c : np.ndarray
        Coordinates of each point
    degrees : bool, Optional, default=False
        Return the angle in degrees

    Returns
    -------
    theta : float
        Angle between the three points

    Examples
    --------
    >>> r1 = np.array([0,0,-1])
    >>> r2 = np.array([0,0,0])
    >>> r3 = np.array([1,0,0])
    >>> calculate_angle(r1, r2, r3, degrees=True)
    90.0
    """
    # Calculate the angle between three points. Answer is given in radians by default, 
    # but can be given in degrees
    # by setting degrees=True
    dist_ab = r_b - r_a
    dist_bc = r_b - r_c
    theta = np.arccos(np.dot(dist_ab, dist_bc) / (np.linalg.norm(dist_ab)*np.linalg.norm(dist_bc)))
    if degrees:
        theta = np.degrees(theta)
    return theta

def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
    
    Parameters
    ----------
    symbols : list
        A list of elements.
    
    Returns
    -------
    mass : float
        The mass of the molecule
    """
    masses = list(map(lambda x: atomic_weights[x], symbols))
    mol_mass = np.sum(masses)
    return mol_mass

def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.
    
    The center of mass is weighted by each atom's weight.
    
    Parameters
    ----------
    symbols : list
        A list of elements for the molecule
    coordinates : np.ndarray, or list-like
        The coordinates of the molecule.
    
    Returns
    -------
    center_of_mass: np.ndarray
        The center of mass of the molecule.
    Notes
    -----
    The center of mass is calculated with the formula
    
    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
    
    """
    mol_mass = calculate_molecular_mass(symbols)
    masses = list(map(lambda x: atomic_weights[x], symbols))
    center = np.zeros(3)
    for mass, coord in zip(masses, coordinates):
        center += list(map(lambda x: mass*x, coord))
    center /= mol_mass
    return center

