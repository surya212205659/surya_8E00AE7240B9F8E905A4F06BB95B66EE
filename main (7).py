#factorial of a given number using recursive function

def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
num=int(input("Enter a number:"))
res=fact_rec(num)
print("the factorial {} is {}.".format(num,res))

