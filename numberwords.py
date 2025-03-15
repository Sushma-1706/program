a = int(input())  
b = int(input()) 

numwords = {
    1: "one", 2: "two", 3: "three",
    4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 0: "zero"
}

for n in range(a, b + 1):
    if 1 <= n <= 9:
        print(numwords[n])
    else:
        if n % 2 == 0:
            print("even")
        else:
            print("odd")
