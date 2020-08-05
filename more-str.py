# append str in the middle of another
s1, s2 = 'Ault', 'Kelly'
s3, s4 = list(s1), list(s2)
new_s1, new_s11 = s3[:2], s3[2:]
new_str = new_s1 + s4 + new_s11
now= ' '.join(new_str)
print(now)

x = 123
y=str(x)
print(type(y))