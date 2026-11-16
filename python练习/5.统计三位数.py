count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                print(i,j,k)
                count+=1
print(f"共有{count}种三位数")