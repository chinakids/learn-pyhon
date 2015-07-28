#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#python 3.4.3,这只是笔记，不代表跑得通.....


#1.切片(范围取值)
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

L[0:2] >>> ['Michael', 'Sarah']  #0-1的数据
L[:2] >>> ['Michael', 'Sarah']  #0-1的数据
L[1:3] >>> ['Sarah', 'Tracy'] #0-2的数据
L[-2:-1] >>> ['Bob'] #-2的数据

L = list(range(100))
L[:10:2] >>> [0, 2, 4, 6, 8]  #前十个每两个取一个
L[::5] >>> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95] #索油数每五个取一个

L[:] #完整拷贝

#tuple 可以切片
(0,1,2,3,4,5,6,7,8)[0:3] >>> (0,1,2)

#字符串也可以切片
'ABCDEFG'[:3] >>> 'ABC'
'ABCDEFG'[::2] >>> 'ACEG'


#迭代，list，dict，tuple，字符串都可以迭代,dict迭代出的是 key，其他都是对应键值数据
for key in <迭代对象>
    print(key)

#判断数据是否可以迭代，Iterable
isinstance('abc', Iterable) >>> True
isinstance(123, Iterable) >>> False

#迭代下标
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
>>>
0 A
1 B
2 C

#多变量循环
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
>>>
1 1
2 4
3 9


#列表生成
list(range(10)) >>> [0,1,2,3,4,5,6,7,8,9]
list(range(1,11)) >>> [1,2,3,4,5,6,7,8,9,10]

list(x * x for x in range(1, 11)) >>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list(x * x for x in range(1, 11) if x % 2 == 0) >>> [4, 16, 36, 64, 100]

list(m + n for m in 'ABC' for n in 'XYZ') >>> ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

d = {'x': 'A', 'y': 'B', 'z': 'C' }
list(k + '=' + v for k, v in d.items()) >>> ['y=B', 'x=A', 'z=C']

L = ['Hello', 'World', 'IBM', 'Apple']
list(s.lower() for s in L) >>> ['hello', 'world', 'ibm', 'apple']


#生成器generator（保存的是算法）
g = (x * x for x in range(10))
g >>> <generator object <genexpr> at 0x1022ef630>
#通过 next()调用下一次的返回值(越界后会报错)
next(g) >>> 0
next(g) >>> 1
next(g) >>> 4
next(g) >>> 9
...
next(g) >>> 81
next(g)
>>>
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
#一般会通过 for in 来迭代generator而非 next()
g = (x * x for x in range(10))
for n in g:
    print(n)


#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#斐波拉契数列的 generator 写法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield d
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
f >>> <generator object fib at 0x104feaaa0>
#最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
>>>
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done


#杨辉三角
def triangles():
    l = []
    while True:
        n = 1
        px = 1
        for x in l[1:]:
            l[n] = px + x
            px = x
            n = n + 1
        l.append(1)
        yield l
n=0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


#可迭代元素
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以使用isinstance()判断一个对象是否是Iterable对象：
isinstance(<被检查元素>, Iterable)
