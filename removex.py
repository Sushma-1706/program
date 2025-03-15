n = int(input())  
s = input()  

i = 0
remove_count = 0  

while i < n - 2:
    if s[i] == 'x' and s[i + 1] == 'x' and s[i + 2] == 'x':  
        remove_count += 1  
    i += 1

print(remove_count)  
