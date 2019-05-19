# python 提供了time和calender模块用于格式化日期和时间
# 时间间隔是以秒为单位的浮点小数，每个时间戳都以自从1970年1月1日午夜经过了多长时间来表示

import time

ticks = time.time()
print("当前时间戳为：", ticks)

# 很多Python函数用一个元组装起来的9组数字处理时间
# (tm_year, tm_mom, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)

localtime = time.localtime(time.time())
print("本地时间：", localtime)

# 格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H %M %S %Y", time.localtime()))


# 获取某月日历
import calendar

cal = calendar.month(2016,1)
print("以下输出2016年1月的日历：", cal)
