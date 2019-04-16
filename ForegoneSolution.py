import random

times = int(input())
cases = []


def cal(case):
    while True:
        no = random.randint(1, case)
        if '4' not in list(str(no)):
            if '4' not in list(str(case - no)):
                return no


for i in range(times):
    cases.append(int(input()))
for i in range(times):
    no = cal(cases[i])
    print("Case #" + str(i + 1) + ": " + str(no) + " " + str(cases[i] - no))
