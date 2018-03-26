a = 0
num=int(input("enter your input"))
temp = num
while temp>0:
   digit = temp % 10
   a = a+digit ** 3
   temp =temp// 10
if num == a:
   print(num,"is an Armstrong number")
else:
  print(num,"is not an Armstrong number")
