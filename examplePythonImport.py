import readTrodesExtractedDataFile3 as trodesReader
rec = 'D:\\DATA\\A01\\raw_data\\20240328_095318nezha.rec'
dat = 'D:\\DATA\\A01\\raw_data\\20240328_095318nezha.time\\20240328_095318nezha.timestamps.dat'
data = trodesReader.readTrodesExtractedDataFile(dat)
print(data['data'].shape)

print(data['data'][1:10])