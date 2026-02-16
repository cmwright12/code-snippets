# https://doc.sagemath.org/html/en/thematic_tutorials/group_theory.html#groups-of-small-order-as-permutation-groups
# groups of order 8
G = DihedralGroup(4) 
G = CyclicPermutationGroup(8)
print(G.cayley_table())

G1 = CyclicPermutationGroup(8)                   #Cyclic

D1 = CyclicPermutationGroup(4)
D2 = CyclicPermutationGroup(2)
G2 = direct_product_permgroups([D1,D2])      #Abelian, non-cyclic

D1 = CyclicPermutationGroup(2)
D2 = CyclicPermutationGroup(2)
D3 = CyclicPermutationGroup(2)
G3 = direct_product_permgroups([D1,D2,D3])   #Abelian, non-cyclic

G4 = DihedralGroup(4)                            #Non-abelian

G5 = QuaternionGroup()                           #Quaternions, also DiCyclicGroup(2)

for G in [G1,G2,G3,G4,G5]:
    print(G.cayley_table())
