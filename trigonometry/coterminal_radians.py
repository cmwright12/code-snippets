# generating reduced fractions where the numerator 
# is less than twice the denominator (1 < a/b < 2)
for _ in range(30):
    a = randrange(5,20)
    b = randrange(2,15)

    if a/b > 1 and a/b < 2 and gcd(a,b) == 1:
        pass
        #print(a,b)
        
# generating reduced fractions where the numerator 
# is more than twice the denominator (a/b > 2)
for _ in range(30):
    a = randrange(5,20)
    b = randrange(2,15)

    if a/b > 2 and a != b and gcd(a,b) == 1:
        print(a,b)
