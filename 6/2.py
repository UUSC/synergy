x=int(input("введи число:"))
count=0
for i in range(1,20000000000):
    if x%i==0:
        count+=1
#в случае если счетчик зайдет за 2 млрд выйти из цикла
    if i>=x:
        break
print(count)