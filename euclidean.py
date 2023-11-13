x, y = 101, 203
if x < y:
    replace = x
    x = y
    y = replace

r = x % y
while r > 0:
    print(x, y, r)
    x = y
    y = r
    r = x % y

print(x, y, r)
print("GCD is", y)
