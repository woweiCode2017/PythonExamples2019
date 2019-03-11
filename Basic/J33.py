people={}
for i in range(1,31):
    people[i]=1

check=0
i=1
j=0

while i<=31:
    if i==31:
        i=1
    elif j==15:
        break
    else:
        if people[i]==0:
            i+=1
            continue
        else:
            check+=1
            if check==9:
                people[i]=0
                check=0
                print("{}号下船了。".format(i))
                j+=1
            else:
                i+=1
                continue
