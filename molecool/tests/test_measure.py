from molecool.measure import (calculate_distance, calculate_angle, calculate_molecular_mass,
                              calculate_center_of_mass)
from molecool.atom_data import atomic_weights
import numpy as np
import pytest

def test_calculate_distance():
    r1 = np.array([0,0,0])
    r2 = np.array([1,0,0])
    assert calculate_distance(r1, r2) == 1

def test_calculate_distance_error():
    r1 = np.array([0,0,0])
    r2 = [1,0,0]
    with pytest.raises(TypeError):
        dist = calculate_distance(r1, r2)
    with pytest.raises(TypeError):
        dist = calculate_distance(r2, r1)

def test_calculate_angle():
    r1 = np.array([0,0,0])
    r2 = np.array([1,0,0])
    r3 = np.array([1,1,0])
    assert calculate_angle(r1, r2, r3, degrees=True) == 90
    assert calculate_angle(r1, r2, r3) == np.pi/2.
    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])
    assert calculate_angle(r1, r2, r3, degrees=True) == 90

@pytest.mark.parametrize("r1, r2, r3, theta",
                         [(np.array([0,0,0]), np.array([1,0,0]), np.array([1,1,0]), 90),
                          (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0,0,0]),
                           np.array([1,0,0]), 45),
                          (np.array([0,0,-1]), np.array([0,1,0]), np.array([1,0,0]), 60)])
def test_calculate_angle_many(r1, r2, r3, theta):
    assert pytest.approx(calculate_angle(r1, r2, r3, degrees=True)) == theta

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']
    calculated_mass = calculate_molecular_mass(symbols)
    actual_mass = atomic_weights['C'] + atomic_weights['H'] \
                  + atomic_weights['H'] + atomic_weights['H'] \
                  + atomic_weights['H']
    assert actual_mass == calculated_mass

def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])
    center_of_mass = calculate_center_of_mass(symbols, coordinates)
    expected_center = np.array([1,1,1])
    assert np.allclose(center_of_mass, expected_center)

