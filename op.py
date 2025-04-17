import numpy as np
import pyopenephys
import matplotlib.pylab as plt
directory = r'D:\DATA\S01\1\2024-03-01_14-10-40'
file = pyopenephys.File(directory)
# experiment 1 (0 in Python)
# experiment = file.experiments[0]
# # recording 1
# recording = experiment.recordings[0]
#
# print('Duration: ', recording.duration)
# print('Sampling Rate: ', recording.sample_rate)
#
# analog_signals = recording.analog_signals
# events_data = recording.events
# spiketrains = recording.spiketrains
# # tracking_data are accessible only using binary format
# tracking_data = recording.tracking
#
# # plot analog signal of channel 4
# signals = analog_signals[0]
# fig_an, ax_an = plt.subplots()
# ax_an.plot(signals.times, signals.signal[3])
#
# # plot raster for spike trains
# fig_sp, ax_sp = plt.subplots()
# for i_s, sp in enumerate(spiketrains):
#     ax_sp.plot(sp.times, i_s*np.ones(len(sp.times)), '|')
#
# plt.show()