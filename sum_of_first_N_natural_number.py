#using formula

def sum_of_N_natural_number(n):
   return n*(n+1)//2

num=int(input("Enter a number:"))
res=sum_of_N_natural_number(num)
print(f"Sum of {num} natuaral number is: {res}")
#----------------------------------------------------------

#using loop

def sum_of_N_natural_number(n):
    sum=0
    if n<1:
        return 0
    else:
        for i in range(1,n+1):
            sum+=i
        return sum

num=int(input("Enter a number:"))
res=sum_of_N_natural_number(num)
print(f"Sum of {num} natuaral number is: {res}")
#--------------------------------------------------------------

#using recursion

def sum(n):
   if n==0:
      return 0
   elif n==1:
      return 1
   else:
      return n+sum(n-1)

num=float(input("Enter a number:"))
res=sum(num)
print(f"Sum of {num} natuaral number is: {res}")