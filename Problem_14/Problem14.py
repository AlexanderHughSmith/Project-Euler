"""Which starting number, under one million, produces the longest chain?"""
"""More info in Readme.txt"""
def collatz(n):
  amount = 1
  while n != 1:
    amount += 1
    if n%2 != 0:
      n = 3*n +1
    else:
      n = n/2
  return amount

num = 0
cnum = 0

for x in range(1,1_000_000):
  temp = int(collatz(x))
  if temp>cnum:
    num = x
    cnum = temp
print("Answer: "+str(num))

