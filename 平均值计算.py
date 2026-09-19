total=0
count=0
print("请输入要求平均值的数字：")
u=input()
while u!= "q":
     num = float(u)
     total+=num
     count+=1
     u=input("请输入数字")
if count == 0:
   print("0")     
else:
     print("得到的平均值为" + str(total/num))
