from datetime import datetime, timedelta

import time

# start_time = "2023:10:30:11:44:20"
# end_time = "2020:06:24:15:00:00"
# duration = 488.998
# start_time1 = time.strptime(start_time, "%Y:%m:%d:%H:%M:%S")
# end_time1 = time.strptime(end_time, "%Y:%m:%d:%H:%M:%S")
#
# start_time2 = int(time.mktime(start_time1))
# print(start_time2+duration)


strTime = '2023:10:30:11:44:20'  # 给定一个时间，此是个字符串
# startTime = datetime.strptime(strTime, "%Y:%m:%d:%H:%M:%S")  # 把strTime转化为时间格式,后面的秒位自动补位的
startTime = datetime(2023,10,30,11,44,20)
print(startTime)
# print(startTime.strftime("%Y-%m-%d %H:%M"))  # 格式化输出，保持和给定格式一致
# startTime时间加 一分钟
startTime2 = (startTime + timedelta(seconds=488.988)).strftime("%Y:%m:%d:%H:%M:%S")
print(startTime2)