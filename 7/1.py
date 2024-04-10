string=input("введи строку:")
flag=0
i=0
while i<len(string):
    if string[i]!=string[-i-1]:
        flag=1
    i+=1
if flag==1:
    print("не палиндром")
else:print("палиндром")

