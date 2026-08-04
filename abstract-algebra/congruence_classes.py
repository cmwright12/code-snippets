n = 5
for i in range(n):
    
    c = [i+n*k for k in [-2,-1,0,1,2]]
    c.insert(0,'...')
    c.append('...')

    
    print(f"[{i}] = {c}")
