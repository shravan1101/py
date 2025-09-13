# def doulble (x):
#  return x*2


def apply_logic(fx, val):
    return 1 + fx(val)


double = lambda x: x * 2
cube = lambda y: y*y*y
avg = lambda x, y, z: (x + y + z) / 3

print(double(2))
print(cube(2))
print(avg(2, 3, 4))
print(apply_logic(cube,2))
