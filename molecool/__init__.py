"""
molecool
A python package dor analyzing and visualizing xyz file. For MolSSI best practices workshop.
"""

# Add imports here
from .functions import *
from .molecule import *
from .atom_data import *
from .measure import *
from .visualize import *
from .io import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
