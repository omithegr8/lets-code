num = int(input("enter a number u want to reverse : "))
rev = 0

while num>0:
  rem = num%10
  num = num//10
  rev = rev*10+rem
print(rev)