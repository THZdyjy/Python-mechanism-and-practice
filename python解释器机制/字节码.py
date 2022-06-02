"""
理解：代码被执行后，被编译为字节码
常常用于代码的debug，涉及变量定义错误之类的。

"""
import dis


def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1
]

for byte in fib.__code__.co_code:
    print(byte, dis.opname[byte])

print('*'*20)


for type in compile('sum = 1 + 2', '', 'exec').co_code:
    print(dis.opname[type])

print('*'*20)


def sum(x, y):
    return x + y
dis.dis(sum)