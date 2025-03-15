list=[1,2,3,4,5]
large=sec_large=float('-inf')
for i in list:
    if i>large:
        sec_large=large
        large=i
        
    elif i > sec_large and i != large: 
         sec_large=i
print("second largest: ",sec_large)