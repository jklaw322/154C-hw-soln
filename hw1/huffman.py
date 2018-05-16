import numpy as np

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

f  = lambda a,b: int(100*(a[1]-b[1]))

p = np.random.random(10)*np.arange(10)+0.01
p = p/sum(p)
q = p
p = sorted([(str(x[0]), x[1]) for x in enumerate(p)], key=cmp_to_key(f))

code = { x[0]: '' for x in p}


for k in range(10-1):
    for x in p[0][0]:
        code[x] += '0'
    for x in p[1][0]:
        code[x] += '1'

    p = sorted(p[2:] + [(p[0][0]+p[1][0], p[0][1]+p[1][1])], key=cmp_to_key(f))

print(q)
print(code)
