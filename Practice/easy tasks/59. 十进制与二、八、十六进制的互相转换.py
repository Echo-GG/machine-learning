a = 10
b = bin(a)
c = oct(a)
d = hex(a)

print(b,c,d)
print(type(b))
print(type(c))
print(type(d))

print(int(b,2)) # 二进制转十进制
print(int(c,8)) # 八进制转十进制
print(int(d,16)) # 十六进制转十进制

s1 = format(10,'b') # 纯二进制串(无0b前缀)
s2 = format(10,'08b') # 8位补零
print(s1)
print(s2)

s3 = format(10,'o') # 纯八进制串(无0o前缀)
s4 = format(10,'016o') # 16位补零
print(s3)
print(s4)

s5 = format(10,'x') # 纯十六进制串(无0x前缀)
s6 = format(10,'032x') # 32位补零
print(s5)
print(s6)