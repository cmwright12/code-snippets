G = []
n1 = 4
n2 = 2
for a in range(n1):
    for b in range(n2):
        G.append((a,b))
        
#print(G)

def add(x,y):
    return ((x[0] + y[0]) % 4, (x[1] + y[1]) % 2)


print(f"Inverses for Z{n1} x Z{n2}:\n")
for x in G:
    for y in G:
        if add(x,y) == (0,0):
            print(f"-{x} = {y}")
        
