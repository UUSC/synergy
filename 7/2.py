string=input("введи строку")
i=0
nach=0
con=0
while i<len(string):
    if string[i]==" " and string[i-1]==" ":
        nach=i
        while string[i]==" ":
            i+=1
        con=i
        print(nach, con)
        string=string[:nach]+string[con:]
    else:
        i+=1

print(string)