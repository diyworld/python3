"""
    ref: https://www.runoob.com/python3/python3-date-time.html
"""
import time
import calendar

# 获取时间戳
ticks = time.time()
print("当前时间戳为:", ticks)

# 转换为时间元组
# 时间元组组成: {year, mon, mday, hour, min, sec, wday, yday, isdst}
localtime = time.localtime(ticks)
print("时间元组:", localtime)

# 格式化时间
formattime = time.asctime(localtime)
print("格式化时间:", formattime)

# 格式化日期
formatdate_1 = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
formatdate_2 = time.strftime("%a %b %d %H:%M:%S %Y", localtime)
print("格式化日期1:", formatdate_1)
print("格式化日期2:", formatdate_2)

# 将格式字符串转换为时间戳
strp = time.strptime(formatdate_2, "%a %b %d %H:%M:%S %Y")
ticks_2 = time.mktime(strp)
print("转换时间戳为", ticks_2)

# 获取某月日历
cal = calendar.month(2021, 2)
print("2021年2月份日历:")
print(cal)

# 延时
print("Start:", time.ctime())
time.sleep(1)
print("End  :", time.ctime())

# 系统运行的时间总和，包括睡眠时间，必须连续调用的结果之差才有意义
print("Start:",time.perf_counter())
time.sleep(1)
print("End  :",time.perf_counter())
# 进程执行的时间总和，不包括睡眠时间，必须连续调用的结果之差才有意义
print("Start:",time.process_time())
time.sleep(1)
print("End  :",time.process_time())

"""
%y      两位数的年份表示（00-99）
%Y      四位数的年份表示（000-9999）
%m      月份（01-12）
%d      月内中的一天（0-31）
%H      24小时制小时数（0-23）
%I      12小时制小时数（01-12）
%M      分钟数（00=59）
%S      秒（00-59）
%a      本地简化星期名称
%A      本地完整星期名称
%b      本地简化的月份名称
%B      本地完整的月份名称
%c      本地相应的日期表示和时间表示
%j      年内的一天（001-366）
%p      本地A.M.或P.M.的等价符
%U      一年中的星期数（00-53）星期天为星期的开始
%w      星期（0-6），星期天为星期的开始
%W      一年中的星期数（00-53）星期一为星期的开始
%x      本地相应的日期表示
%X      本地相应的时间表示
%Z      当前时区的名称
%%      %号本身
"""