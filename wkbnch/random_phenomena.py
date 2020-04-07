"""Simple example of random phenomena.

Example from "Intoduction to Probability Theory" Hoel, Port, Stone

A box has s balls, labeled 1,2,...,s but otherwise identical. Consider the following experiment.
The balls are mixed up well in the box and a person reaches into the box and draws a ball. The
number of the ball is noted and the ball is returned to the box. The outcome of the experiment
is the number on the ball selected. About this experiment we can make no nontrivial prediction.

  Suppose we repeat the above experiment n times. Let Nⁿ(k) denote the number of times the ball
labeled k was drawn during these n trials of the experiment. Assume that we had, say, s = 3 balls
and n = 20 trials. The outcomes of these 20 trials could be described by listing the numbers which
appeared in the order they were observed. A typical result might be
      1, 1 ,3, 2, 1, 2, 2, 3, 2, 3, 3, 2, 1, 2, 3, 3, 1, 3, 2, 2,
in which case
     N₂₀(1) = 5,   N₂₀(2) = 8, and N₂₀(3) = 7.
The relative frequencies (i.e., proportion of times) of the outcomes 1, 2, and 3 are then
    N₂₀(1) / 20 = .25,  N₂₀(2) / 20 = .40, and N₂₀(3) / 20 = .35.

  As the number of trials gets large we would expect the relative frequncies Nⁿ(1)/n,...,Nⁿ(s)/n
to settle down to some fixed numbers p₁,p₂,...,ps (which according to our intuition in this case
should be 1/s).
"""
import random
from itertools import chain, combinations

def trial(n, s):
    """Number of experiments to run of selecting one number from a squence."""
    # draw number for each trial
    trial_list = []
    random.seed(a=None, version=2)
    for t in range(n):
        pick = random.randrange(1, s + 1)
        trial_list.append(pick)
    print(f'Result of selecting one number from a sequence of {s} numbers {n} times {trial_list}')
    # count number of draws for element k
    counts_list = []
    for num in range(1, s + 1):
        draws = count(n, num, trial_list)
        counts_list.append((num, draws))
    print(f'Counts of number of draws for each number {counts_list}')
    probability_space(s)
    # calculate relative frequencies

def count(n, k, l):
    """Number of times the element labeled k was drawn during n trials of the experiment."""
    # slice of results from 0 to n
    result_list = l[0:n] 
    return result_list.count(k)

def probability_space(s):
    """Generate a probability space for finite set of s points (Ω, Α, Ρ)."""
    Ω = range(1, s + 1)
    print(list(Ω))
    Α = powerset(Ω)
    print(Α)
    Ρ = probability_measure
    measure = Ρ(Α[7], s)
    print(measure)

def powerset(iterable):
    """Return the list of all subsets as a list of tuples of an iterable."""
    S = list(iterable)
    # combinations: r-length tuples, in sorted order, no repeated elements
    return list(chain.from_iterable(combinations(S, r) for r in range(len(S) + 1)))

def probability_measure(A, s):
    """Probability measure on a σ-field of subsets Α of a set Ω."""
    # size of subset of events / size of set of all events
    probability = len(A) / s
    return probability

if __name__ == "__main__":
    trial(20, 3)
