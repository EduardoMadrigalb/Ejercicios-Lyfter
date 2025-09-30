Planets=['Mercury','Venus','earth','mars','jupiter','saturn','uranus','neptune']

def i(a):
    if len(a) > 1:
        a[0], a[-1] = a[-1], a[0]
i(Planets)
print(Planets)
