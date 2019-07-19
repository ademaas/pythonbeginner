#find a number which is divisible by 7 but not multiple of 5
#between 2000 and 3200
count=[]
for x in range(2000,3201):
    if (x%7==0) and (x%5!= 0):
        count.append(str(x))
print(','.join(count))
        
