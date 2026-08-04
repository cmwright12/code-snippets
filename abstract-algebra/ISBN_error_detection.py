# Error Checking ISBN Codes

rawusercode=input("Input a 10 digit code: ")
usercode=rawusercode.replace('-', '')
usercode=usercode.replace(' ', '')
print(usercode)


code = list(usercode)
for i in range(len(code)):
    if code[i] == "X" or code[i] == "x":
        code[i] = "10"
d = [int(a) for a in code]
w = [10,9,8,7,6,5,4,3,2,1]

v = [d[i]*w[i] for i in range(10)]
print(f"d.w = {sum(v)} ≡ {sum(v) % 11} mod 11")
if sum(v) % 11 == 0:
    print(rawusercode, "is a valid ISBN code")
else:
    print(rawusercode, "is an invalid ISBN code")
