path = 'D:\\DATA\\A01\\raw_data\\20240328_095318nezha.raw\\20240328_095318nezha.timestamps.dat'
raw = 'D:\\DATA\\A01\\raw_data\\20240328_095318nezha.raw\\20240328_095318nezha.raw_group0'
# with open(path, 'rb') as f:
#     data = f.read()
#     print(type(data))

# import numpy as np
# data = np.fromfile(path, dtype=np.uint8)
# print(data.size)
# print(data[:100])

file_path = 'D:\\DATA\\A03\\continuous.dat'
#
# print('chardet')
# import chardet
#
# with open(file_path, 'rb') as f:
#     result = chardet.detect(f.read())  # 读取一定量的数据进行编码检测
#
# print("encode: ", result['encoding'])  # 打印检测到的编码

# import pandas as pd
# df = pd.read_csv(file_path, delimiter='\t')
# print(df.head())

import numpy as np

data = np.fromfile(raw, dtype=np.float32)
print(data.shape)

print(data)
