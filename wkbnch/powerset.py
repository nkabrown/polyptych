"""Power set is the set of all subsets of a set.

S = {x, y, z}

P(S) = {{}, {x}, {y}, {z}, {x, y}, {x, z}, {y, z}, {x, y, z}}
"""
from itertools import chain, combinations


def powerset(iterable):
   """Return the list of all subsets as a list of tuples of an iterable."""
    S = list(iterable)
    # combinations: r-length tuples, in sorted order, no repeated elements
    return list(chain.from_iterable(combinations(S, r) for r in range(len(S) + 1)))
