"""

pythond的动态语言特性使得
其在运行的过程中，可以更改自身的代码。可以用来监视代码的执行次数。
"""
import re

__called_time = 27

for i in range(__called_time):
    print(i)

lines = []
with open(__file__) as f:
    for line in f.read().split('\n'):
        num = re.findall('called_time .* (\d+)', line)
        if num:
            num = num[0]
            line = re.sub('\d+', str(int(num) + 1), line)

        lines.append(line)

with open(__file__, 'w') as f:
    for line in lines:
        f.write(line + '\n')




