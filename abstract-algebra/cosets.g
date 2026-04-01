#gap
# Cosets: Permutations
s:=(1,2,4,3); H:=[(), (1,4,3), (1,3,4)];
cycle:=[(), s, s^2, s^3];
Print(cycle);
Hsi:=List(H, h -> s^-1 * h);
Print(Hsi);

# Cosets: Matrices
n:=7; 
g:=[[2,0],[1,5]] mod n;
H:=[ [[1,0],[0,1]], [[1,0],[0,-1]]] mod n;

Determinant(g) mod n;
gi:=g^-1 mod n;
C:=List(H, h -> g * h * g^-1 mod n);
C;
