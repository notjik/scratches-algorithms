"""
The initializing module of the package.

-----

:authors: notjik
:license: MIT License
:copyright: (c) 2023 notjik
"""
from .algorithms import *
from .utils import *

__all__ = [*algorithms.__all__,
           *utils.__all__]

__version__ = '0.1.2'
