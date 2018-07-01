# -*- coding: utf-8 -*-
# Author: lzjiang
# What is pythonic or non-pythonic?

# import this

# 链式表达

Chain = ['A', 'B', 'C', 'D']

if Chain.index('A') < Chain.index('B') < Chain.index('C'):
    print('Yes')
else:
    print('No')

# 置换变量

A = u'我爱你'
B = u'你爱我'

A, B = B, A

print(A, B)

# 迭代数组

TmpA = ['A', 'B', 'C', 'D']

for i, j in enumerate(TmpA):
    '''enumerate中start默认为0，计数默认从0开始'''
    print(i, j)

# 字符串拼接
# Note 对比列表，字符串，元组，字典的join实现区别
String = '_'.join(Chain)
print(String)

# 列表生成
Number = [1, 2, 3, 4, 5, 6]
result = [i * 2 for i in Number if i % 2 == 0]
print(result)

# 布尔判断
name = 'lzjiang'
if name.endswith('jiang'):
    print('Hello lzjiang!')
else:
    print('Hello Stranger')

if A and B:
    print('A and B exists')
else:
    print('error')

print(bool(A))

# zip建字典
Value = [1, 2, 3, 4]
D = dict(zip(Chain, Value))
print(D)

# 三目运算符
temp = 'Hello lzjiang' if len(name) > 3 else 'Hello Stranger'
print(temp)

# 字典计数 字典的get方法
chart_demo = u'1237894567'
count = {}
for i in chart_demo:
    count[i] = count.get(i, 0) + 1
print(count)

# list反向遍历
for i in reversed(Value):
    print(i)

# for else 语法
for i in Value:
    if 5 == i:
        print('5 found')
        break
else:
    print('There is not 5 in Value')

# lambda函数
p = lambda x: x * x
print(p(2))

# map函数
Value2 = map(p, Value)
Value3 = map(lambda x, y: (x, y, x * y, x + y), Value, [1, 2, 3])
for i in Value3:
    print(i)

Value4 = map(int, ['1234', '234'])
for i in Value4:
    print(i)

# filter
Value5 = filter(lambda x: x if x == 'A' else None, TmpA)

for i in Value5:
    print(i)

# reduce
from functools import reduce

Value6 = reduce(lambda x, y: x + y, Value, 0)
Value7 = sum(Value)
print(Value6)
print(Value7)
