a = input()
b = input()
a_dec = int(a, 2)
b_dec = int(b, 2)
tong = bin(b_dec + a_dec)
print(tong[2:])