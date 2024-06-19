import mne

path = 'D:\\柔性电极动物实验数据\\大鼠64通道\\柔性电极-64通道_神经信号_第50天E.ns5'
# ns = mne.io.read_raw_nsx(path)
ns = mne.io.read_raw_nsx('D:\\柔性电极动物实验数据\\猕猴急性记录\\dataset1\\datafile002.ns6')
print(type(ns))
print('ns.ch_names:', ns.ch_names)
# print(ns.n_times)
print(ns)

