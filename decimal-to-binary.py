x = int(input(" enter a number : "))
i = 0
lst = list()

while x > 0:
  i = x % 2
  x = x // 2
  # print(i)
  lst.append(i)


for num in reversed(lst):
  print(num)