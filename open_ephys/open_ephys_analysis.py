'''
Open-ephys有三种数据形式
https://github.com/open-ephys/open-ephys-python-tools/blob/main/src/open_ephys/analysis/README.md

'''

from open_ephys.analysis import Session

# 在Record Node的父目录
directory = r''
session = Session(directory)

print(session.recordnodes[0])

recording = session.recordnodes[0].recordings[0]
print(recording)
print(recording.info)

recording = session.recordnodes[0].recordings[0]
data = recording.continuous[0].get_samples(start_sample_index=0, end_sample_index=1000)
print(data.shape)