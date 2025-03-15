n = int(input())  
i = 1 
count = 0  

while n >= (i * (i + 1)) // 2:  
    n -= (i * (i + 1)) // 2
    i += 1
    count += 1

print(count)  
