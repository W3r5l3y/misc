"""Expresses the GCD of a pair of integers as a linear combination"""


class BColors:
    """Contains text colour codes"""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# INPUT NUMBERS HERE IN FORM x, y
x, y = 101, 203


def find_gcd(x, y):
    """Progressively finds possible GCD of x and y"""
    xfactors = []
    yfactors = []

    for i in range(1, x + 1):
        if x % i == 0:
            xfactors.append(i)

    for i in range(1, y + 1):
        if y % i == 0:
            yfactors.append(i)

    # print(xfactors)
    # print(yfactors)

    gcd = int(max(set(xfactors).intersection(yfactors)))
    print("GCD =", gcd)

    compare, xcount, ycount = 0, 0, 0

    while compare != gcd:
        if xcount * x <= ycount * y:
            xcount += 1
        else:
            ycount += 1
        compare = (xcount * x) - (ycount * y)
        # print(compare, xcount, ycount)
    return xcount, ycount


gcd1 = list(find_gcd(x, y))
gcd2 = list(find_gcd(y, x))

if sum(gcd1) < sum(gcd2):
    xcount = gcd1[0]
    ycount = gcd1[1]
    print(
        f"{BColors.ENDC}Answer = {BColors.HEADER}{xcount}{BColors.ENDC} * {x} {BColors.HEADER}- {ycount}{BColors.ENDC} * {y}"
    )
else:
    xcount = gcd2[0]
    ycount = gcd2[1]
    print(
        f"{BColors.ENDC}Answer = {BColors.HEADER}- {ycount}{BColors.ENDC} * {x} {BColors.HEADER}+ {xcount}{BColors.ENDC} * {y}"
    )
