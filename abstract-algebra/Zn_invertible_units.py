a = 3
n = 13

def products(a,n):
    for b in range(n):
        print(a,"*",b,"=", a*b % n)

def inverse(a,n):
    for b in range(n):
        if a*b % n == 1:
            return b
    return None

def inverses(n):
    inverse_list = []
    for a in range(n):
        for b in range(n):
            if a*b % n == 1:
                inverse_list.append((a,b))
    k = [x[0] for x in inverse_list]
    print(f"U({n}) = Units in Z({n}): \n{k}\n")
    for x in inverse_list:
        print("{}^-1 = {} mod {}".format(x[0],x[1],n))


#a_inv = inverse(a,n)
#print("{}^-1 mod {} = {}.".format(a,n,a_inv))

inverses(n)
