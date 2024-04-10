a=int(input("введите а "))
b=int(input("введите b "))
count=""
for i in range(a, b+1):
    if i%2==0:
        count= count + str(i) + " "

print(count)
