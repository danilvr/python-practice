import deal

from pow_two import pow2

@deal.cases(pow2)
def test_div(case: deal.TestCase) -> None:
    case()
