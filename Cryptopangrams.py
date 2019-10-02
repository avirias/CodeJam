import math

# Function for Calculation
def cal(nos):
    alpha = []
    for i in range(len(nos)):
        if i == 0:
            p = list([(x, nos[i] // x) for x in range(int(math.sqrt(nos[i])))[2:] if not nos[i] % x][0])
            a, b = p[0], p[1]
            alpha.append(b if (nos[i + 1] / a - nos[i + 1] // a) == 0.0 else a)
            alpha.append(a)
        alpha.append(nos[i] // alpha[-1])
    alpha = alpha[1:]
    x = list(dict.fromkeys(alpha))
    x.sort()
    s = ""
    for c in alpha:
        s += chr(x.index(c) + 65)
    return s


sizes = []
ap = []
times = int(input())
for i in range(times):
    sizes.append(input())
    ap.append(input())
for i in range(times):
    nos = [int(x) for x in ap[i].split()]
    print("Case #" + str(i + 1) + ": " + cal(nos))

    # good idea and futher changes can be made to make it better
