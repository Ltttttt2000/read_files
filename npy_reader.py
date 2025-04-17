import numpy as np

# path = 'D:\\DATA\\A01\\kilo_shank_0\\sorter_output\\template_feature_ind.npy'
path = r'D:\DATA\术后植入\pre_data\sub001\word\data.npy'

path2 = r'D:\DATA\术后植入\pre_data\sub001\word\data_uncorr.npy'
#导入npy文件路径位置
test = np.load(path)
test2 = np.load(path2)
# M个采样点: 70481957, 2000Hz
print(test.shape, test2.shape)
print(test[0])
print(test2[0])