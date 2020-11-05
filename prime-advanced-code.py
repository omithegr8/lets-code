start = 0
end = int(input("enter a number : "))

for i in range(start,end):
    if i > 1:
        for o in range(2,i):
            if i % o == 0:
                break
        else:
            print(i)