import json
import mne

data_path = 'D:\\WangYinyanRaw\\术中唤醒\\ECoG_20231030_A_P_1\\ECoG_20231030_A_P_1_Movments_Session_1_datRaw.edf'   # 存放数据的具体位置，需要改成自己数据存放的地方
# data_path = 'D:\\WangYinyanRaw\\短期植入\\20231217 Shandong\\Lishilong_20231215_motor1\\Lishilong_20231215_motor1.edf'


# signal_name  = 'EEG Fpz-Cz'     # 所选的通道名称
raw_data = mne.io.read_raw_edf(data_path, preload=False)
print(raw_data)  # 32 x 244500


# 查看原始edf文件中保存的event id以及events
# events_from_annot, event_dict = mne.events_from_annotations(raw_data)
# print(event_dict)
# print(events_from_annot)
