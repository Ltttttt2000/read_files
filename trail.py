import mne
rec_file = 'D:\\20240305_143425.rec'
data = mne.io.read_raw(rec_file)
print(data)