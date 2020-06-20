class A: pass
x = A()
if *:
    y = x
else:
    y = A()
y.a = 2
z = x.a
'''
PycharmProjects\project1\practice\.pytest_cache\rr.py:8: error: "A" has no attribute "a"
PycharmProjects\project1\practice\.pytest_cache\rr.py:11: error: "A" has no attribute "a"
'''
