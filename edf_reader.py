import json
import mne

data_path = ''
# signal_name  = 'EEG Fpz-Cz'     # 所选的通道名称
raw_data = mne.io.read_raw_edf(data_path, preload=False)
print(raw_data)  # 32 x 244500

tmp = raw_data.to_data_frame()
print(tmp)

# # plot
# import matplotlib.pyplot as plt
# for i in range(1,32):
#     plt.subplot(4,8,i)
#     plt.plot(tmp.values[:,i])
#     # plt.plot(tmp.values[:,32])
# plt.show()

