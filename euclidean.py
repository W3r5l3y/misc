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
print(f"GCD is \033[95m{y}\033[0m")
