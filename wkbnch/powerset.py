"""Power set := the set of all subsets of a set."""

from itertools import chain, combinations

"""Return the list of all subsets as a list of tuples of an iterable."""
def powerset(iterable):
    S = list(iterable)
    # combinations: r-length tuples, in sorted order, no repeated elements
    return list(chain.from_iterable(combinations(S, r) for r in range(len(S) + 1)))
