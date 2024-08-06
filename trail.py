import mne
rec_file = 'D:\\DATA\\A01\\raw_data\\20240328_095318nezha.raw\\20240328_095318nezha.raw_group0.dat'
data = mne.io.read_raw(rec_file)
print(data)