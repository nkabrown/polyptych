# Notes

**powerset.py**

The Boolean operations on power sets include union, intersection, and complementation. The power set with these operations make up a Boolean algebra.

`chain.from_iterable` returns an `<itertools.chain object>`. Returning that would give me a little more flexibility in how to represent the power set.

Why `combinations()` and not `permutations()`?

Daily Coding Problem #37[Easy]

> This problem was asked by Google.
>
> The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
>
> For example, given the set `{1, 2, 3}`, it should return `{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}`.
>
> You may also use a list or array to represent a set.

Would like to demonstrate a solution using a generator to precisely "generate" a power set. But I suspect that using `itertools` would be lead to a more optimized solution.
