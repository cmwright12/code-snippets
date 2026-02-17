"""
ADDITIVE Z(n)
"""
n = 5

def _set(x, start="...,", end=", ..."):
    output = "{" + start + str(x[0])
    for i in range(1,len(x)):
        output += ", " + str(x[i])
    output += end + "}"
    return output
    
for a in range(n):
    gen = [k*a % n for k in range(-2,n+2)]
    unique = list(set(gen))
    unique.sort()
    #print("<",a,"> = ",gen)
    #print(_set(gen))
    print(f"<{a}> = " + _set(gen) + " = " + _set(unique,"",""))
  
"""
MULTIPLICATIVE U(n)
"""
import math
n = 5

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

def inverse(a,n):
    for b in range(n):
        if a*b % n == 1:
            return b
    return None



elements = [a for a in range(n) if coprime(a,n)]
print(f"U({n}) = {_set(elements)}")

# need to add inverse and powers of inverse
for a in elements:
    print(f"\na={a}:")
    ainv = inverse(a,n)
    gen = []
    for k in range(0,len(elements)):
        a_k = int(math.pow(a,k)) % n
        print(f"{a}^{k} = {int(math.pow(a,k))} = {a_k} mod {n}")
        #ainv_k = int(math.pow(ainv,k)) % n
        #if (k > 1) and (a_k % n == a):
        #    break
        #else:
        gen.append(a_k)
        #gen.append(ainv_k)
            
    unique = list(set(gen))
    unique.sort()
    print("<", a , "> =", _set(gen), "=", _set(unique) )

"""
Zm x Zn cyclic
"""
m = 2
n = 4

for a in range(m):
    for b in range(n):
        print(f"\n(a,b)=({a},{b}):")
        gen = [(k*a % m, k*b % n) for k in range(1,m*n)]
        for i, g in enumerate(gen):
            print(f"{i+1}*({a} mod {m}, {b} mod {n}) = {g}")
        unique = list(set(gen))
        unique.sort()
        print("<",(a,b),"> =", _set(unique))
