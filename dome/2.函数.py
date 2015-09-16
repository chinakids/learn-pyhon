#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#python 3.4.3,这只是笔记，不代表跑得通.....

#定义函数 def,关键字
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

#空函数使用 pass 占位，不然会报错
def nop():
    pass
#pass可用在其他语句
if <表达式>:
    pass
#函数内参数检查isinstance(<数据>,<数据类型>),if not isinstance((a,b,c),(int,float))
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


#返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y) -[输出]-> 151.96152422706632 70.0
#单一值也可接收，return 对象为 tuple
r = move(100, 100, 60, math.pi / 6)
print(r) -[输出]-> (151.96152422706632, 70.0)
#函数执行完毕也没有return语句时，自动return None。


#函数的缺省默认参数,默认参数必须指向不变对象！
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power(5) -[输出]-> 25
power(5, 2) -[输出]-> 25

#默认参数为可变参可能导致的问题 。eg：
def add_end(L=[]):
    L.append('END')
    return L

add_end() -[输出]-> ['END']
add_end() -[输出]-> ['END', 'END']
add_end() -[输出]-> ['END', 'END', 'END']
#默认参数为可变参可能导致的问题 。解决方法（转变为不可变参） eg:
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#可变参函数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc([1, 2, 3]) -[输出]-> 14
calc((1, 3, 5, 7)) -[输出]-> 84

#将接收的参数作为一个 tuple,(*key)
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2, 3) -[输出]-> 14
calc(1, 3, 5, 7) -[输出]-> 84

nums = [1, 2, 3]
calc(*nums) -[输出]-> 14

#关键字参数(**key)
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing') -[输出]-> name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer') -[输出]-> name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra) -[输出]-> name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


#命名关键字，检查关键字参数的名称
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, 'Beijing', 'Engineer') -[输出]-> <出错>
#关键字参数允许缺省
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer') -[输出]-> Jack 24 Beijing Engineer


#参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。




#递归函数，使用递归函数需要注意防止栈溢出
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

fact(1) -[输出]-> 1
fact(5) -[输出]-> 120
#尾递归调用解决栈溢出
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
