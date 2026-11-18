data=[4,1,3,8,2]
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]>data[j]:
            data[i],data[j]=data[j],data[i]
print(data)
