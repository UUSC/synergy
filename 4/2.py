a=int(input("Введи пятизначное число"))
b=a//100
a1=b//100
a2=(b//10)%10
a3=b%10
c=a//10
a4=c%10
a5=a%10
rezult=(a4**a5*a3)//(a1-a2)
print(rezult)
