import mne

nsx_path = r'D:\DATA\120-29-10W\120-29-10W.ns6'
# ns = mne.io.read_raw_nsx(path)
ns = mne.io.read_raw_nsx(nsx_path)
# print(ns.info)


print(ns.n_times / ns.info['sfreq'])
print(ns.info['meas_date'])
print(ns.info['nchan'])