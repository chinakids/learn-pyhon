#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#python 3.4.3,这只是笔记，不代表跑得通.....

#整形
1,2300,-122,0

#浮点型
1.2,-0.0,1.2e9,1.2e-5

#字符串(转义与其他语言规则同理)
'这是个"python"字符串'
"这是个'python'字符串"
'这是个\'python\'字符串'

r"///////"  #字符串前置 r 表示字符串不含转义

'''...''' #多行


#布尔值(首字母大写)
True
False

and,or,not #逻辑运算，分别等价&&,||,!=


#空值(0不是空值)
None

#变量(变量名必须是大小写英文、数字和_的组合，且不能用数字开头)
a = 1
a = 'string'
a = False

#常量(全部大写,书写习惯,本质为变量)
PI = 3.14159265359

#除法
10/3  >>>  3.33333333 #精确
10//3 >>>  3 #取整(地板除)
10%3 >>> 1  #取余


#编码（默认 unicode）

#获取字符编码
ord('A') >>> 65
ord('中') >>> 20013
#从编码获取字符串
chr(65) >>> 'A'
chr(20013) >>> '中'

'\u4e2d\u6587' >>> '中文'

#传输需要使用 bytes 类型数据
x = b'Abc'   #转为 bytes 类型数据
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
#编码：
'ABC'.encode('ascii')  >>>  b'ABC'
'中文'.encode('utf-8') >>>  b'\xe4\xb8\xad\xe6\x96\x87'
#'ascii'编码不包含中文
#反编码：
b'ABC'.decode('ascii') >>> 'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') >>> '中文'

#计算 str 字符长度，btyes 类型下为字节长度(python2.*以下例子貌似跑不通..待测)
len('abc') >>> 3
len('中文') >>> 2

len(b'ABC') >>> 3
len(b'\xe4\xb8\xad\xe6\x96\x87') >>> 6
len('中文'.encode('utf-8')) >>> 6


#解释器声明以及编码声明
#     #!/usr/bin/env python3
#     # -*- coding: utf-8 -*-


#数据格式化
'Hello, %s' % 'world' >>>  'Hello, world'
'Hi, %s, you have $%d.' % ('Michael', 1000000) >>> 'Hi, Michael, you have $1000000.'
'%2d-%02d' % (3, 1) >>> ' 3-01'
'%.2f' % 3.1415926 >>> '3.14'

#%s永远起作用，它会把任何数据类型转换为字符串
#用%%来表示一个%
'growth rate: %d %%' % 7 >>> 'growth rate: 7 %'
#占位符
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数


#数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。类似 js 的数组
classmates = ['Michael', 'Bob', 'Tracy']
classmates >>> ['Michael', 'Bob', 'Tracy']
len(classmates) >>> 3
classmates[0] >>> 'Michael'
classmates[-1] >>> 'Tracy'
classmates.append('Adam') #尾部追加
classmates >>> ['Michael', 'Bob', 'Tracy', 'Adam']
classmates.insert(1, 'Jack') #插入到指定位置
classmates >>> ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
classmates.pop() >>> 'Adam' #删除并返回被删除元素
classmates >>> ['Michael', 'Jack', 'Bob', 'Tracy']
classmates.pop(1) >>> 'Jack' #删除指定位置并返回被删除元素
classmates >>> ['Michael', 'Bob', 'Tracy']
classmates[1] = 'Sarah' #替换
classmates >>> ['Michael', 'Sarah', 'Tracy']
#存储不同类型
L = ['Apple', 123, True]
#多维
S = ['python', 'java', ['asp', 'php'], 'scheme']
len(s) >>> 4
#空 list 的 len 为0


#元组，tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
#因为()也能表示运算符，所以单个元素的 tuple 需要增加逗号
classmates = ('Michael', )
#“可变的”tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
t >>> ('a', 'b', ['X', 'Y'])


#条件判断(注意语句后冒号)
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if x :
    True


#输入input
birth = input('birth: ')
birth = int(s)  #int()方法将输入值转为 int 类型，输入值必须为可转为数字的数字字符串
if birth < 2000:
    print('00前')
else:
    print('00后')


#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#生成 list
list(range(5)) >>> [0, 1, 2, 3, 4] #rang(x)会生成0到 x-1的数字序列（range(0,x-1)），list()会将此序列转为 list
#计算0-100的数字之和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#条件循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


#字典dict，key-value的储存方式
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael'] >>> 95
#判断 key 是否存在
'Thomas' in d  >>> False
#get()方法取值
d.get('Thomas',<自定义不存在时返回的值>) #返回None的时候Python的交互式命令行不显示结果。
d['Thomas']  #直接取值，不存在会报错..推荐 get()
#删除，pop(key)
d.pop('Bob') >>> 75
d >>> {'Michael': 95, 'Tracy': 85}


#set类型，一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3])
s >>> {1, 2, 3}
#自动过滤重复
d = set([1, 1, 2, 2, 3, 3])
d >>> {1, 2, 3}
#添加方法 add(),可重复添加，但没什么卵用....
s.add(4)
s >>> {1, 2, 3, 4}
s.add(4)
s >>> {1, 2, 3, 4}
#删除方法 remove()
s.remove(4)
s >>> {1, 2, 3}
#可做交集并集操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2 >>> {2, 3}
s1 | s2 >>> {1, 2, 3, 4}
