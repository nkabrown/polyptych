from wkbnch import powerset

def test_powerset():
    """If set A has n elements than P(A) has 2ⁿ elements."""
    A = 'abc'
    assert len(powerset.powerset(A)) == 2**len(A)
    B = [1, 2, 3, 4, 5]
    assert len(powerset.powerset(B)) == 2**len(B)
    C = []
    assert len(powerset.powerset(C)) == 2**len(C)
