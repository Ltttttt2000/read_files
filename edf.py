import json
import mne

data_path = r'D:\DATA\运动术中唤醒\M_A_20231030_01_motor\ECoG_20231030_A_P_1_Movments_Session_1_datRaw.edf'
# signal_name  = 'EEG Fpz-Cz'     # 所选的通道名称
raw_data = mne.io.read_raw_edf(data_path, preload=False)
print(raw_data.info)  # 32 x 244500
print(raw_data.n_times / raw_data.info['sfreq'])
# for ch in raw_data.ch_names:
#     print(ch)
# tmp = raw_data.to_data_frame()
# print(tmp['POL 1'])
# print(tmp['POL-1'])

# # # plot
# import matplotlib.pyplot as plt
# for i in range(1,32):
#     plt.subplot(4,8,i)
#     plt.plot(tmp.values[:,i])
#     # plt.plot(tmp.values[:,32])
# plt.show()

