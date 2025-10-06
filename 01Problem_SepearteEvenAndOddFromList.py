original_lst=[1,4,7,8,2,3,5,9]
even_lst=[]
odd_lst=[]
for num in original_lst:
    if num%2==0:
        even_lst.append(num)
    else:
        odd_lst.append(num)
print(f"Even numbers from original list is : {even_lst}")
print(f"Odd numbers from original list is : {odd_lst}")
