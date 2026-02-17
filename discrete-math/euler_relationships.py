def analyze_euler_relationships(U, A, B, C):
    sets = {'A': A, 'B': B, 'C': C}
    names = list(sets.keys())
    
    print("--- Euler Diagram Relationship Analysis ---")
    
    # 1. Check for Universal Set Integrity
    for name, s in sets.items():
        if not s.issubset(U):
            print(f"Warning: Set {name} contains elements not in Universal set U!")

    # 2. Pairwise Comparisons
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            name1, name2 = names[i], names[j]
            s1, s2 = sets[name1], sets[name2]
            
            print(f"\nRelationship between {name1} and {name2}:")
            
            if s1 == s2:
                print(f"  - {name1} and {name2} are EQUAL.")
            elif s1.issubset(s2):
                print(f"  - {name1} is a PROPER SUBSET of {name2}.")
            elif s2.issubset(s1):
                print(f"  - {name2} is a PROPER SUBSET of {name1}.")
            elif s1.isdisjoint(s2):
                print(f"  - {name1} and {name2} are DISJOINT (no common elements).")
            else:
                intersection = s1.intersection(s2)
                print(f"  - {name1} and {name2} OVERLAP (Intersection: {intersection}).")

    # 3. Triple Intersection
    triple_int = A.intersection(B).intersection(C)
    if triple_int:
        print(f"\nTriple Intersection (A ∩ B ∩ C): {triple_int}")
    else:
        print("\nThere is NO common intersection between all three sets.")

def get_latex_summary(U, A, B, C):
    """Generates a LaTeX bulleted list of set relationships."""
    sets = {'A': A, 'B': B, 'C': C}
    names = ['A', 'B', 'C']
    lines = [r"\begin{itemize}"]

    # 1. Pairwise Comparisons
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            n1, n2 = names[i], names[j]
            s1, s2 = sets[n1], sets[n2]
            
            if s1 == s2:
                rel = f"is equal to ${n2}$"
            elif s1.issubset(s2):
                rel = f"is a proper subset of ${n2}$ ($ {n1} \\subset {n2} $)"
            elif s2.issubset(s1):
                rel = f"is a superset of ${n2}$ ($ {n1} \\supset {n2} $)"
            elif s1.isdisjoint(s2):
                rel = f"is disjoint from ${n2}$ ($ {n1} \\cap {n2} = \\emptyset $)"
            else:
                rel = f"overlaps with ${n2}$ ($ {n1} \\cap {n2} \\neq \\emptyset $)"
            
            lines.append(f"    \\item Set ${n1}$ {rel}.")

    # 2. Triple Intersection
    triple_int = A.intersection(B).intersection(C)
    if not triple_int:
        lines.append(f"    \\item The triple intersection is empty ($ A \\cap B \\cap C = \\emptyset $).")
    else:
        lines.append(f"    \\item The triple intersection $ A \\cap B \\cap C $ contains {len(triple_int)} element(s).")

    lines.append(r"\end{itemize}")
    return "\n".join(lines)

def main():
    # Define your Universal set and subsets here
    U = set(range(1, 10))
    A = {2, 3, 4,}
    B = {2, 3, 4, 8}
    C = {1, 8}
    
    analyze_euler_relationships(U, A, B, C)

    # Generate and print the LaTeX code
    latex_output = get_latex_summary(U, A, B, C)
    
    print("\n\n% --- Copy and Paste the LaTeX code below ---")
    print(latex_output)

if __name__ == "__main__":
    main()
