
# 打开 .pl2 文件
filename = 'D:\\DATA\\A02\\R902_20240104\\20240104FOF1000R902.pl2'

from NeuroPy import PlexonIO

# 打开 .pl2 文件
reader = PlexonIO(filename)

# 读取数据块
block = reader.read_block()

# 列出所有可用的信号通道
print([signal.name for signal in block.segments[0].analogsignals])

# 获取指定通道的LFP数据
lfp_signal = block.segments[0].analogsignals[0]
print(lfp_signal)

# 获取 spike 数据
spike_trains = block.segments[0].spiketrains
print(spike_trains)

# 获取事件标记
events = block.segments[0].events
print(events)
