# 打开文件
with open('D:\柔性电极动物实验数据\大鼠256通道\Day-07\Ch.001~064.btn', 'rb') as file:
    # 逐字节读取
    print(type(file))

    # byte = file.read(1)
    # while byte:
    #     # 处理字节
    #     print(byte)
    #     # 继续读取下一个字节
    #     byte = file.read(1)
