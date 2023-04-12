number = input("请输入一个四位数:")
boolean1 = number[0] == number[3]
boolean2 = number[1] == number[2]
if(boolean1 and boolean2):
    print(int(number),"是回文数")
else:
    print(int(number),"不是回文数")