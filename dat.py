path = 'D:\柔性电极动物实验数据\大鼠64通道\柔性电极-64通道_神经信号_第50天F.dat'

# with open(path, 'rb') as f:
#     data = f.read()
#     print(type(data))

import numpy as np
data = np.fromfile(path, dtype=np.uint8)
print(data.size)
print(data[:100])