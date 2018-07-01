# -*- coding: utf-8 -*-
# Author: lzjiang

# 位置参数 默认参数(默认参数必须放在必选参数后)
# Example: power(x)


def power(a, x=2):
    '''
    :param a: 底数
    :param x: 幂，default=2
    :return: out
    '''

    s = 1
    while x > 0:
        x = x - 1
        s = s * a
    return s


#  默认参数尤其需要引起注意点
def add_end(L=None):
    '''
    :param L: Nore：如果设定L为空列表，则默认参数会被修改，由此默认参数设为None，若成立则令L为空列表，默认参数不会被改变
    :return:
    '''
    if L is None:
        L = []
    L.append('End')
    return L


# 可变参数
# example: 计算a*a + b*b + c*c + ......
def calc(*numbers):
    '''
    *numbers作用
    令函数内部接收到一个numbers传入的tuple，无需引入tuple或者list数据结构
    另一方面，对于已有的List与Tuple数据结构也可以通过该方式转成可变参数传入函数
    calc([1,2,3])=>calc(1,2,3,4)
    '''
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
L = [1, 2, 3, 4]
print(calc(*L))


# 关键字参数 拓展函数功能
def person(name, age, **kw):
    '''关键字参数与可变参数类似，可变参数在函数内部自动组装成Tuple，而关键参数则自动组装成dict'''
    print('name:', name, 'age:', age, 'other:', kw)


print(person('lzjiang', 25, city='shenzhen'))
