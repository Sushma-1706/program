x=input("enter number: ").lower()
count=0
for char in x:
    if char in 'aeiou' :
        count+=1
print(count)