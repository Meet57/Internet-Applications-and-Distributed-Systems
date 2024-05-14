def max(d1, d2):
    if d1 < d2:
        return d2
    else:
        return d1


n1 = int(input("Give Number 1: "))
n2 = int(input("Give Number 2: "))

print("Max is: ", max(n1, n2))
