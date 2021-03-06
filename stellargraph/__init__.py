"""
Stellar Machine Learning Library

"""

__all__ = ["data", "layer", "mapper", "StellarDiGraph", "StellarGraph", "__version__"]

# Version
from .version import __version__

# Top-level imports
from stellargraph.core.graph import StellarGraph, StellarDiGraph
from stellargraph.core.schema import GraphSchema
