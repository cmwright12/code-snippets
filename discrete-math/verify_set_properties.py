# -------------------------
# Helpers (CodeSkulptor3-safe)
# -------------------------

def _sorted_list(s):
    """Return a consistent order for readability across types."""
    return sorted(list(s), key=lambda x: (str(type(x)), str(x)))

def _set_str(s):
    """Human-readable set like {1, 2, 3} with stable order."""
    return "{" + ", ".join(map(str, _sorted_list(s))) + "}"

def _latex_escape(text):
    """Escape common LaTeX special characters."""
    s = str(text)
    repl = [
        ("\\", r"\textbackslash{}"),
        ("{", r"\{"), ("}", r"\}"),
        ("#", r"\#"), ("$", r"\$"), ("%", r"\%"),
        ("&", r"\&"), ("_", r"\_"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    ]
    for a, b in repl:
        s = s.replace(a, b)
    return s

def _set_latex(S):
    """Render a Python set as a LaTeX set: \{a, b, c\}."""
    items = [_latex_escape(x) for x in _sorted_list(S)]
    return r"\{" + ", ".join(items) + r"\}"

def complement(U, X):
    """Set complement relative to U."""
    return U - X


# -------------------------
# Laws to test
# -------------------------

def demorgan_union(U, X, Y):
    """
    De Morgan #1: U \ (X ∪ Y) == (U \ X) ∩ (U \ Y)
    """
    lhs = complement(U, X | Y)
    rhs = complement(U, X) & complement(U, Y)
    return {"law": "De Morgan (complement of union)", "lhs": lhs, "rhs": rhs, "holds": lhs == rhs, "X": X, "Y": Y}

def demorgan_intersection(U, X, Y):
    """
    De Morgan #2: U \ (X ∩ Y) == (U \ X) ∪ (U \ Y)
    """
    lhs = complement(U, X & Y)
    rhs = complement(U, X) | complement(U, Y)
    return {"law": "De Morgan (complement of intersection)", "lhs": lhs, "rhs": rhs, "holds": lhs == rhs, "X": X, "Y": Y}

def associativity_union(A, B, C):
    """(A ∪ B) ∪ C == A ∪ (B ∪ C)"""
    lhs = (A | B) | C
    rhs = A | (B | C)
    return {"law": "Associativity (union)", "lhs": lhs, "rhs": rhs, "holds": lhs == rhs}

def associativity_intersection(A, B, C):
    """(A ∩ B) ∩ C == A ∩ (B ∩ C)"""
    lhs = (A & B) & C
    rhs = A & (B & C)
    return {"law": "Associativity (intersection)", "lhs": lhs, "rhs": rhs, "holds": lhs == rhs}

# --- NEW: Distributive laws ---

def distributive_union_over_intersection(A, B, C):
    """A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)"""
    lhs = A | (B & C)
    rhs = (A | B) & (A | C)
    return {"law": "Distributive (union over intersection)", "lhs": lhs, "rhs": rhs, "holds": lhs == rhs}

def distributive_intersection_over_union(A, B, C):
    """A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)"""
    lhs = A & (B | C)
    rhs = (A & B) | (A & C)
    return {"law": "Distributive (intersection over union)", "lhs": lhs, "rhs": rhs, "holds": lhs == rhs}


# -------------------------
# Human-readable formatters
# -------------------------

def explain_human_demorgan(result, Xname="X", Yname="Y", ascii_only=False):
    lhs_s = _set_str(result["lhs"])
    rhs_s = _set_str(result["rhs"])

    if "union" in result["law"]:
        left_desc  = ("U \\ ({0} union {1})".format(Xname, Yname)) if ascii_only else (u"U \\ ({0} ∪ {1})".format(Xname, Yname))
        right_desc = ("(U \\ {0}) intersect (U \\ {1})".format(Xname, Yname)) if ascii_only else (u"(U \\ {0}) ∩ (U \\ {1})".format(Xname, Yname))
    else:
        left_desc  = ("U \\ ({0} intersect {1})".format(Xname, Yname)) if ascii_only else (u"U \\ ({0} ∩ {1})".format(Xname, Yname))
        right_desc = ("(U \\ {0}) union (U \\ {1})".format(Xname, Yname)) if ascii_only else (u"(U \\ {0}) ∪ (U \\ {1})".format(Xname, Yname))

    status = "HOLDS ✅" if result["holds"] else "DOES NOT HOLD ❌"
    out = []
    out.append("{0} for ({1}, {2}):".format(result["law"], Xname, Yname))
    out.append("  LHS = {0} = {1}".format(left_desc, lhs_s))
    out.append("  RHS = {0} = {1}".format(right_desc, rhs_s))
    out.append("  Result: {0}".format(status))
    return "\n".join(out)

def explain_human_assoc(result, op_symbol="∪", ascii_only=False):
    lhs_s = _set_str(result["lhs"])
    rhs_s = _set_str(result["rhs"])
    if ascii_only:
        op = "union" if "union" in result["law"].lower() else "intersect"
        lhs_desc = "(A {0} B) {0} C".format(op)
        rhs_desc = "A {0} (B {0} C)".format(op)
    else:
        op = op_symbol
        lhs_desc = "(A {0} B) {0} C".format(op)
        rhs_desc = "A {0} (B {0} C)".format(op)
    status = "HOLDS ✅" if result["holds"] else "DOES NOT HOLD ❌"
    out = []
    out.append("{0}:".format(result["law"]))
    out.append("  LHS = {0} = {1}".format(lhs_desc, lhs_s))
    out.append("  RHS = {0} = {1}".format(rhs_desc, rhs_s))
    out.append("  Result: {0}".format(status))
    return "\n".join(out)

def explain_human_distrib(result, outer_symbol, inner_symbol, ascii_only=False):
    """Readable explanation for distributive results."""
    lhs_s = _set_str(result["lhs"])
    rhs_s = _set_str(result["rhs"])
    if ascii_only:
        # ASCII words
        lhs_desc = "A {0} (B {1} C)".format("union" if outer_symbol=="∪" else "intersect",
                                            "union" if inner_symbol=="∪" else "intersect")
        rhs_desc = "(A {0} B) {1} (A {0} C)".format("union" if outer_symbol=="∪" else "intersect",
                                                    "union" if inner_symbol=="∪" else "intersect")
    else:
        lhs_desc = "A " + outer_symbol + " (B " + inner_symbol + " C)"
        rhs_desc = "(A " + outer_symbol + " B) " + inner_symbol + " (A " + outer_symbol + " C)"
    status = "HOLDS ✅" if result["holds"] else "DOES NOT HOLD ❌"
    out = []
    out.append("{0}:".format(result["law"]))
    out.append("  LHS = {0} = {1}".format(lhs_desc, lhs_s))
    out.append("  RHS = {0} = {1}".format(rhs_desc, rhs_s))
    out.append("  Result: {0}".format(status))
    return "\n".join(out)


# -------------------------
# LaTeX formatters (concise, “a couple steps”; built by concatenation)
# -------------------------

def latex_demorgan_union(U, X, Y, Xname="X", Yname="Y"):
    lhs = complement(U, X | Y)
    rhs = complement(U, X) & complement(U, Y)
    Xn = _latex_escape(Xname)
    Yn = _latex_escape(Yname)
    lhs_tex = _set_latex(lhs)
    rhs_tex = _set_latex(rhs)
    s  = ""
    s += "\\[\n"
    s += "\\begin{aligned}\n"
    s += "U \\setminus (" + Xn + " \\cup " + Yn + ")\n"
    s += "&= (U \\setminus " + Xn + ") \\cap (U \\setminus " + Yn + ") && \\text{by De Morgan}\\\\[2pt]\n"
    s += "&= " + lhs_tex + " \\quad\\text{and}\\quad " + rhs_tex + " && \\text{compute both sides}\\\\\n"
    s += "&\\text{so the sets are equal.}\n"
    s += "\\end{aligned}\n"
    s += "\\]\n"
    return s

def latex_demorgan_intersection(U, X, Y, Xname="X", Yname="Y"):
    lhs = complement(U, X & Y)
    rhs = complement(U, X) | complement(U, Y)
    Xn = _latex_escape(Xname)
    Yn = _latex_escape(Yname)
    lhs_tex = _set_latex(lhs)
    rhs_tex = _set_latex(rhs)
    s  = ""
    s += "\\[\n"
    s += "\\begin{aligned}\n"
    s += "U \\setminus (" + Xn + " \\cap " + Yn + ")\n"
    s += "&= (U \\setminus " + Xn + ") \\cup (U \\setminus " + Yn + ") && \\text{by De Morgan}\\\\[2pt]\n"
    s += "&= " + lhs_tex + " \\quad\\text{and}\\quad " + rhs_tex + " && \\text{compute both sides}\\\\\n"
    s += "&\\text{so the sets are equal.}\n"
    s += "\\end{aligned}\n"
    s += "\\]\n"
    return s

def latex_associativity_union(A, B, C):
    lhs = (A | B) | C
    rhs = A | (B | C)
    lhs_tex = _set_latex(lhs)
    rhs_tex = _set_latex(rhs)
    s  = ""
    s += "\\[\n"
    s += "\\begin{aligned}\n"
    s += "(A \\cup B) \\cup C &= A \\cup (B \\cup C) && \\text{associativity}\\\\[2pt]\n"
    s += "&= " + lhs_tex + " \\quad\\text{and}\\quad " + rhs_tex + " && \\text{compute both sides}\\\\\n"
    s += "&\\text{so the sets are equal.}\n"
    s += "\\end{aligned}\n"
    s += "\\]\n"
    return s

def latex_associativity_intersection(A, B, C):
    lhs = (A & B) & C
    rhs = A & (B & C)
    lhs_tex = _set_latex(lhs)
    rhs_tex = _set_latex(rhs)
    s  = ""
    s += "\\[\n"
    s += "\\begin{aligned}\n"
    s += "(A \\cap B) \\cap C &= A \\cap (B \\cap C) && \\text{associativity}\\\\[2pt]\n"
    s += "&= " + lhs_tex + " \\quad\\text{and}\\quad " + rhs_tex + " && \\text{compute both sides}\\\\\n"
    s += "&\\text{so the sets are equal.}\n"
    s += "\\end{aligned}\n"
    s += "\\]\n"
    return s

# --- NEW: LaTeX for distributive laws ---

def latex_distrib_union_over_intersection(A, B, C):
    lhs = A | (B & C)
    rhs = (A | B) & (A | C)
    lhs_tex = _set_latex(lhs)
    rhs_tex = _set_latex(rhs)
    s  = ""
    s += "\\[\n"
    s += "\\begin{aligned}\n"
    s += "A \\cup (B \\cap C)\n"
    s += "&= (A \\cup B) \\cap (A \\cup C) && \\text{distributive law}\\\\[2pt]\n"
    s += "&= " + lhs_tex + " \\quad\\text{and}\\quad " + rhs_tex + " && \\text{compute both sides}\\\\\n"
    s += "&\\text{so the sets are equal.}\n"
    s += "\\end{aligned}\n"
    s += "\\]\n"
    return s

def latex_distrib_intersection_over_union(A, B, C):
    lhs = A & (B | C)
    rhs = (A & B) | (A & C)
    lhs_tex = _set_latex(lhs)
    rhs_tex = _set_latex(rhs)
    s  = ""
    s += "\\[\n"
    s += "\\begin{aligned}\n"
    s += "A \\cap (B \\cup C)\n"
    s += "&= (A \\cap B) \\cup (A \\cap C) && \\text{distributive law}\\\\[2pt]\n"
    s += "&= " + lhs_tex + " \\quad\\text{and}\\quad " + rhs_tex + " && \\text{compute both sides}\\\\\n"
    s += "&\\text{so the sets are equal.}\n"
    s += "\\end{aligned}\n"
    s += "\\]\n"
    return s


# -------------------------
# Convenience runners (integrated)
# -------------------------

def test_all(U, A, B, C, ascii_only=False):
    """Print human-readable checks for De Morgan (pairs), associativity, and distributive laws."""
    # De Morgan on each pair (A,B), (A,C), (B,C)
    pairs = [(A, B, "A", "B"), (A, C, "A", "C"), (B, C, "B", "C")]
    for X, Y, Xn, Yn in pairs:
        print(explain_human_demorgan(demorgan_union(U, X, Y), Xn, Yn, ascii_only))
        print()
        print(explain_human_demorgan(demorgan_intersection(U, X, Y), Xn, Yn, ascii_only))
        print("\n" + "-" * 50 + "\n")

    # Associativity on A, B, C
    print(explain_human_assoc(associativity_union(A, B, C), "∪", ascii_only))
    print()
    print(explain_human_assoc(associativity_intersection(A, B, C), "∩", ascii_only))
    print("\n" + "-" * 50 + "\n")

    # Distributive laws
    print(explain_human_distrib(distributive_union_over_intersection(A, B, C), "∪", "∩", ascii_only))
    print()
    print(explain_human_distrib(distributive_intersection_over_union(A, B, C), "∩", "∪", ascii_only))

def latex_all(U, A, B, C):
    """Return a single LaTeX string with concise solutions for all requested laws."""
    pieces = []
    # De Morgan
    pieces.append(latex_demorgan_union(U, A, B, "A", "B"))
    pieces.append(latex_demorgan_intersection(U, A, B, "A", "B"))
    pieces.append(latex_demorgan_union(U, A, C, "A", "C"))
    pieces.append(latex_demorgan_intersection(U, A, C, "A", "C"))
    pieces.append(latex_demorgan_union(U, B, C, "B", "C"))
    pieces.append(latex_demorgan_intersection(U, B, C, "B", "C"))
    # Associativity
    pieces.append(latex_associativity_union(A, B, C))
    pieces.append(latex_associativity_intersection(A, B, C))
    # Distributive (NEW)
    pieces.append(latex_distrib_union_over_intersection(A, B, C))
    pieces.append(latex_distrib_intersection_over_union(A, B, C))
    return ("\n\n% ---\n\n").join(pieces)


# -------------------------
# Example usage (adjust or remove)
# -------------------------
if __name__ == "__main__":
    # Define your universe and subsets
    U = set(range(1, 13))
    A = {1, 2, 3, 6}
    B = {2, 4, 6, 8}
    C = {1, 5, 6, 9, 10}

    # Human-readable checks (set ascii_only=True if your console dislikes Unicode)
    test_all(U, A, B, C, ascii_only=False)

    # LaTeX blocks to paste into a solution key
    tex = latex_all(U, A, B, C)
    print("\n" + "=" * 60 + "\nLATEX OUTPUT:\n")
    print(tex)
