
rec_file = r'D:\DATA\a01\20240419_102825.LFP_nt1000ch1.dat'
# .dat读法
import readTrodesExtractedDataFile3 as trodesReader
data = trodesReader.readTrodesExtractedDataFile(rec_file)
print(data)
print(data['data'].shape)

rec_file2 = r'D:\DATA\a01\20240419_102825.spikes_nt1.dat'
data2 = trodesReader.readTrodesExtractedDataFile(rec_file2)
print(data2)
print(data2['data'].shape)
