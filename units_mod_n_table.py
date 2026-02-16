from sage.matrix.operation_table import OperationTable
for n in srange(1,50):
    if euler_phi(n) > 4 and euler_phi(n) < 10:
        print(n, euler_phi(n))

n = 18
Un = [Integers(n)(a) for a in srange(n) if Mod(a,n).is_unit()]
# with letters
OperationTable(Un, operation=operator.mul)
# with Numbers
OperationTable(Un, operation=operator.mul, names='elements')
