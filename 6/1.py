n = int(input("введи количество чисел:"))
num=0
count=0
for i in range(n):
    print("введи число ", i+1)
    num=int(input())
    if num==0:
        count+=1

print(count)