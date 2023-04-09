#输入年份
year = int(input("请输入年份:"))

#用一个布尔量输出结果,弃用
#print((year%400 == 0 and year%100 ==0) or (year%400 != 0 and year%4 == 0))

#判断年份是不是100的倍数
if(year%100 == 0):
    print("闰年判断结果是:",year%400 == 0)
else:
    print("闰年判断结果是:",year%4 == 0)