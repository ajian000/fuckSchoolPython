number = input("请输入一个四位数:")
boolean1 = number[0] == number[3]
boolean2 = number[1] == number[2]
if(boolean1 and boolean2):
    print(int(number),"是回文数")
else:
    print(int(number),"不是回文数")
    
#以下为该问题的另一种解法实现
number = int(input("请输入一个四位数"))
#a，b，c，d分别代表该数的千，百，十，个位
a = number//1000
b = (number%1000)//100
c = ((number%1000)%100)//10
d = ((number%1000)%100)%10
if(a==d and b==c):
    print(number,"是回文数")
else:
    print(number,"不是回文数")
