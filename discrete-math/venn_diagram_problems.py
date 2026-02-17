def venn_regions(A, B, C, U):
    """Return dict of the 8 regions of a 3‑set Venn diagram."""
    return {
        "onlyA":  A - B - C,
        "onlyB":  B - A - C,
        "onlyC":  C - A - B,
        "onlyAB": (A & B) - C,
        "onlyAC": (A & C) - B,
        "onlyBC": (B & C) - A,
        "ABC":    A & B & C,
        "notABC": U - (A | B | C)
    }


def _brace(s):
    """Format set as {1, 2, 3} with elements sorted."""
    return "{" + ", ".join(map(str, sorted(s))) + "}"


def print_human(regions):
    print("Only A:      ", _brace(regions["onlyA"]))
    print("Only B:      ", _brace(regions["onlyB"]))
    print("Only C:      ", _brace(regions["onlyC"]))
    print("A ∩ B only:  ", _brace(regions["onlyAB"]))
    print("A ∩ C only:  ", _brace(regions["onlyAC"]))
    print("B ∩ C only:  ", _brace(regions["onlyBC"]))
    print("A ∩ B ∩ C:   ", _brace(regions["ABC"]))
    print("Outside ABC: ", _brace(regions["notABC"]))


def print_form(regions):
    print(f"form[labelOnlyA={_brace(regions['onlyA'])},")
    print(f"     labelOnlyB={_brace(regions['onlyB'])},")
    print(f"     labelOnlyC={_brace(regions['onlyC'])},")
    print(f"     labelOnlyAB={_brace(regions['onlyAB'])},")
    print(f"     labelOnlyAC={_brace(regions['onlyAC'])},")
    print(f"     labelOnlyBC={_brace(regions['onlyBC'])},")
    print(f"     labelABC={_brace(regions['ABC'])},")
    print(f"     labelNotABC={_brace(regions['notABC'])}]")
    

U = set(range(1, 10))
A = {2,3,4}
B = {2,3,4,8}
C = {1,8}


regions = venn_regions(A, B, C, U)

print_human(regions)
print()
print_form(regions)

