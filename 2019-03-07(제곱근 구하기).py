x = 16
g = 3
while not (abs(g*g-x) < 0.01):
    g = (g+x/g)/2
print(g)
