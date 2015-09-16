abs(-10) -[输出]-> 10

abs -[输出]-> <built-in function abs>
#abs(-10)是函数调用，而abs是函数本身。
#函数本身也可以赋值给变量，即：变量可以指向函数。
#由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。

#传入函数
f = abs
def add(x, y, f):
    return f(x) + f(y)


#map() ，依照对应函生成映射表
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]) #map(<方法>,<可循环序列>)
list(r) -[输出]-> [1, 4, 9, 16, 25, 36, 49, 64, 81]


#reduce(),按照规则依次计算
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7, 9]) -[输出]-> 25
