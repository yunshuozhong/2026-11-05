wall=[45,61,27,38,50,74,63,19,56,62,82,36]
answers=[]
for i in range(len(wall)):
    for j in range(i+1,len(wall)):
        if wall[i]+wall[j]==100:
            answers.append(wall[i])
            answers.append(wall[j])
print(f'密碼:{answers}')