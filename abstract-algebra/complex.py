# sage: Complex number calculations
z = 12-5*I
w = -2+2*I
zinv = z^-1
print(zinv)
#print(f"{zinv.real()} + {zinv.imag()} * I")

print(z*w)
zw = z*w
zabs = sqrt(z*z.conjugate())
wabs = sqrt(w*w.conjugate())
zwabs = sqrt(zw*zw.conjugate())


print(f"|z|={zabs}, |w|={wabs}")
print(f"|zw|={zwabs}")
